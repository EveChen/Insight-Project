from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, SparkSession
import os

def get_s3_data(bucket_name, file_name = None):
    path = 's3a://{}/'.format(bucket_name)
    if file_name is not None:
        path += '{}/'.format(file_name)

    return path

bucket = "amazon-reviews-insight"
path = get_s3_data(bucket, "reviews_Amazon_Instant_Video.json")

conf = SparkConf().setAppName("AmazonReviewDashboard") 
sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)
df = sqlContext.read.format('json').load(path)



#PostgreSQL


properties = {'user': config["user"], 'password': config["password"], 'driver': 'org.postgresql.Driver'}
mode = "overwrite"
ip_address = config["ip_address"]
url = "jdbc:postgresql://ip_address:5432/my_db"

try:
    df.write.jdbc(url = url, table="fulldata", mode = mode, properties = properties)
    print("If you see this line, it means the jdbc write function did not crash")
except Exception as e:
    print(e)
