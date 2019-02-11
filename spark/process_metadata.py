# Write product metadata (11 GB) from Spark to MySQL

# Import packages
import re
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, functions
from pyspark.sql.types import FloatType, ArrayType, StringType, IntegerType
from textblob import TextBlob

# Get metadata from AWS S3
path = "s3a://bucketname/filename"
conf = SparkConf().setAppName("ReadJson")
sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)

# Read a json file
data = sqlContext.read.format('json').\
            options(header='true', inferSchema='true').\
            load(path)
data = data.withColumn("category", data.categories[0][0])

# Select certain columns we want
results = data.select("asin", "title", "price", "category", "imUrl")


# Write the metadata to MySQL
results.write.format("jdbc").options(
    url='jdbc:mysql://public_DNS:3306/database_name',
    driver = 'com.mysql.cj.jdbc.Driver',
    dbtable = 'table_name',
    user = 'username',
    password = 'password').mode('append').save()
