# Write data to MySQL table
# Notes: I've already created a MySQL table with the same data schema

# Packages
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, SparkSession

# Load data from AWS S3 to Spark
path = "s3a://amazon-reviews-insight/reviews_Amazon_Instant_Video.json"
conf = SparkConf().setAppName("ReadJson")
sc = SparkContext(conf = conf)

###spark = SparkSession.builder.appName("Overwrite").getOrCreate()

sqlContext = SQLContext(sc)
df = sqlContext.read.json(path).select("asin", "overall", "reviewTime", "reviewText")

# Append data from Spark to MySQL table (table name is "reviews")
df.write.format("jdbc").options(
    url='jdbc:mysql://public_DNS:3306/database_name',
    driver = 'com.mysql.cj.jdbc.Driver',
    dbtable = 'table_name',
    user = 'username',
    password = 'password').mode('append').save()

