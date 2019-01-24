from pyspark.sql import SQLContext
import pyspark
from pyspark import SparkContext, SparkConf
conf = SparkConf()
sc = SparkContext(conf = conf)

sql = SQLContext(sc)
data = sql.read.json("s3a://reviews0121/reviews_Amazon_Instant_Video.json.gz")

data.printSchema()

#  |-- asin: string (nullable = true)
#  |-- helpful: array (nullable = true)
#  |    |-- element: long (containsNull = true)
#  |-- overall: double (nullable = true)
#  |-- reviewText: string (nullable = true)
#  |-- reviewTime: string (nullable = true)
#  |-- reviewerID: string (nullable = true)
#  |-- reviewerName: string (nullable = true)
#  |-- summary: string (nullable = true)
#  |-- unixReviewTime: long (nullable = true)
