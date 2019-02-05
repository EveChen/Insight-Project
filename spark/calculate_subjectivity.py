# Test how to calculate subjectivity from Amazon reviews using TextBlob package

# Packages
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, SparkSession
from textblob import TextBlob

def subjectivity(reviewText):
    sentiment = TextBlob(reviewText).sentiment
    return sentiment.subjectivity

# Load test data
path = "s3a://amazon-reviews-insight/reviews_Amazon_Instant_Video.json"
conf = SparkConf().setAppName("ReadJson")
sc = SparkContext(conf = conf)

sqlContext = SQLContext(sc)
review_content = sqlContext.read.json(path).select("reviewText")

# Extract subjectivity
sentiment = subjectivity(review_content)
sentiment.show()

