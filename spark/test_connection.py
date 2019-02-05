# Test if I could connect Spark with MySQL database
# Before this step, you should download a JDBC driver corresponds with your MySQL/Python versions
# I choose this JDBC version: https://mvnrepository.com/artifact/mysql/mysql-connector-java/8.0.15
# Need to install this JDBC connector to all master & workers node.

# Packages
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, SparkSession

spark = SparkSession.builder.appName('ReadData').getOrCreate()
df = spark.read.format("jdbc").options(
    url='jdbc:mysql://ec2-54-212-162-51.us-west-2.compute.amazonaws.com:3306/my_db',
    driver = 'com.mysql.cj.jdbc.Driver',
    dbtable = '(SELECT * FROM reviews) as reviews',
    user = 'newuser',
    password = 'Xiavi293@').load()
df.show()

# Finally, run "spark-submit --jars /path/mysql-connector-java-8.0.15.jar my_python_codes.py"
