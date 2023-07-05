###### Spark Base Objects
1. Create Spark Context Object

        from pyspark import SparkConf,SparkContext
        
        spark_conf = SparkConf()
        spark_context = SparkContext("local[2]", "Test", spark_conf)   

2. Create SparkSession
        
        from pyspark.sql import SparkSession
        
        SparkSession.builder.master("local[2]").appName("test").getOrCreate()
        
###### RDD Operations

1. Creating RDD from list

        vals = [1, 2, 3]
        list_rdd = sc.parallelize(vals)
        
2. Create from text file
        
        emprdd = sc.textFile("G:\\Projects\\PySpark\\data\\input\\Employee\\EmployeeDetails.txt")
        
##### Transformations
1. Map

        emprdd = sc.textFile("G:\\Projects\\PySpark\\data\\input\\Employee\\EmployeeDetails.txt")
        emprdd_split = emprdd.map(lambda x: x.split(",")).map(lambda x: (x[0], x[1], x[2], x[3]))
        
##### Create DataFrame from rdd
1. Create using DF
    
        from pyspark import SparkConf,SparkContext
        from pyspark.sql import SparkSession
        
        sc = SparkContext("local[2]", "Test", SparkConf())
        emprdd = sc.textFile("G:\\Projects\\PySpark\\data\\input\\Employee\\EmployeeDetails.txt")
        emprdd_split = emprdd.map(lambda x: x.split(",")).map(lambda x: (x[0], x[1], x[2], x[3]))
        
        spark_session = SparkSession(sc)
        schema_emp = ["emp_id", "emp_name", "emp_sal", "dep_id"]
        emp_df = emprdd_split.toDF(schema_emp)
