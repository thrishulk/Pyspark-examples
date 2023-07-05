from pyspark import SparkConf,SparkContext
from pyspark.sql import SparkSession


def get_spark_context():
    spark_conf = SparkConf()
    return SparkContext("local[2]", "Test", spark_conf)


def get_spark_session():
    return SparkSession.builder.master("local[2]").appName("test").getOrCreate()

