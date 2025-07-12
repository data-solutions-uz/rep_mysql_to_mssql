# type: ignore
# spark_utils.py

from pyspark.sql import SparkSession
from pyspark.sql import SQLContext 

def get_spark():
    """Create and return a SparkSession."""
    return SparkSession \
        .builder \
        .master("spark://spark-master:7077") \
        .appName("Pipezone") \
        .getOrCreate()

spark = get_spark()
# sqlContext = SQLContext(spark)