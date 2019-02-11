# Calculate the adjusted ratings based on the sentiments of each Amazon reviews

# Import packages
import re
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, functions
from pyspark.sql.types import FloatType, ArrayType, StringType, IntegerType
from textblob import TextBlob

# Load data from AWS S3
path = "s3a://bucketname/filename"
conf = SparkConf().setAppName("ReadJson")
sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)
data = sqlContext.read.json(path).select("asin", "reviewText", "overall")

# Calculations for the Adjusted ratings

# 1. Scale: Change the range of the original ratings from 0~5 to 0~1
scale_ratings_function = functions.udf(lambda overall : overall / 5, FloatType())

# 2. Get the subjectivity from each reviews, range 0~1 which 0 means objective and 1 means subjective
subjectivity_function = functions.udf(lambda reviewText: TextBlob(reviewText).sentiment.subjectivity, FloatType())

# 3. Transfer the subjectivity to the weight. For example:
# (a.) If a review has 0.8 subjectivity (i.e. too subjective), I give it 1.5-0.8 = 0.7 weight as a penalty
# (b.) If a review has 0.2 subjectivity (i.e. more objective), I give it 1.5 - 0.2 = 1.3 weight as a reward
weight_function = functions.udf(lambda subjectivity: 1.5 - subjectivity, FloatType())

# 4. Raw adjusted ratings by multiply the scale rating (i.e. 1st function) with the weight (i.e. 3rd function)
raw_ratings_function = functions.udf(lambda scale_ratings, weight: scale_ratings * weight, FloatType())

# 5. Transfer the adjusted ratings from range 0~1 to range 0~5
ratings_function = functions.udf(lambda raw_ratings : raw_ratings * 5, FloatType())

# 6. If the adjusted rating is over 5, modify it as 5 to fit the range
adj_ratings_function = functions.udf(lambda adjusted_ratings_raw: adjusted_ratings_raw if adjusted_ratings_raw <= 5.0 else 5.0, FloatType())

# 7. Add the label to name if the overall product's reviews is more subjective or objective
label_function = functions.udf(lambda average_subjectivity : "Subjective" if average_subjectivity >= 0.5 else "Objective", StringType())


# Start applying those functions to the data
data = data.withColumn("scale_ratings", scale_ratings_function(data.overall))
data = data.withColumn("subjectivity", subjectivity_function(data.reviewText))
data = data.withColumn("weight", weight_function(data.subjectivity))
data = data.withColumn("raw_ratings", raw_ratings_function(data.scale_ratings, data.weight))
data = data.withColumn("ratings_wo_avg", ratings_function(data.raw_ratings))

# Groupby "asin" to calculate each product's original ratings, adjusted ratings and adjusted subjectivitiy
new_data = data.groupby("asin").agg(functions.avg("overall").alias("original_ratings"), functions.avg("ratings_wo_avg").alias("adjusted_ratings_raw"), functions.avg("subjectivity").alias("average_subjectivity"))
new_data = new_data.withColumn("adjusted_ratings", adj_ratings_function(new_data.adjusted_ratings_raw)).withColumn("label", label_function(new_data.average_subjectivity))

# Select the columns we want
results = new_data.select("asin", "original_ratings", "adjusted_ratings", "average_subjectivity", "label")

# Write final outputs to MySQL
results.write.format("jdbc").options(
    url='jdbc:mysql://publicDNS:3306/database_name',
    driver = 'com.mysql.cj.jdbc.Driver',
    dbtable = 'table_name',
    user = 'username',
    password = 'password').mode('append').save()


