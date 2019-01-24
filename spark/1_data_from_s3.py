from pyspark.sql import SQLContext
import pyspark
from pyspark import SparkContext, SparkConf
conf = SparkConf()
sc = SparkContext(conf = conf)

sql = SQLContext(sc)
data = sql.read.json("s3a://reviews0121/reviews_Amazon_Instant_Video.json.gz")

data.printSchema()

### Reviews data
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


# ### Metadata
#  |-- asin: string (nullable = true)
#  |-- categories: array (nullable = true)
#  |    |-- element: array (containsNull = true)
#  |    |    |-- element: string (containsNull = true)
#  |-- price: double (nullable = true)
#  |-- related: struct (nullable = true)
#  |    |-- also_viewed: array (nullable = true)
#  |    |    |-- element: string (containsNull = true)


# Next steps
# 1. randomly select a column within the review dataset, push this column to PostgreSQL, query the first ten contents and push to Flask (dashboard)
# 2. Spark preprocessing data including calculations, word counts etc
# 3. Build a relational database with decribe table like this:

# ----------------------------------------------------------------------------------------
# | Product ID | Product Name | Reliable Ratio | Reviewer ID | Review Contexts| Category |
# ----------------------------------------------------------------------------------------

# 4. Query top 10 reliable data (group by product id) and push the outputs to Flask
