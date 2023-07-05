import PySpark.spark as spark
from pyspark.sql import SparkSession


sc = spark.get_spark_context()
ss = SparkSession(sc)


def emp_rdd():

    emprdd = sc.textFile("G:\\Projects\\PySpark\\data\\input\\Employee\\EmployeeDetails.txt")
    print(emprdd.take(10))
    emprdd_split = emprdd.map(lambda x: x.split(",")).map(lambda x: (x[0], x[1], x[2], x[3]))
    print(emprdd_split.take(10))
    print(hasattr(emprdd_split, "toDF"))
    schema_emp = ["emp_id", "emp_name", "emp_sal", "dep_id"]
    emp_df = emprdd_split.toDF(schema_emp)
    emp_df.show()


def list_rdd():
    vals = [1, 2, 3]
    rdd = sc.parallelize(vals)
    print(rdd.take(2))


if __name__ == '__main__':
    emp_rdd()
    # list_rdd()
