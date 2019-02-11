# Test if I could import data from AWS S3 to Spark

# Packages
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, SparkSession

# Import data from AWS S3
path = "s3a://amazon-reviews-insight/reviews_Amazon_Instant_Video.json"
conf = SparkConf().setAppName("ReadJson")
sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)

# Only select column "asin"
df = sqlContext.read.json(path).select("asin")

# Show the data (i.e. only asin)
df.show()
