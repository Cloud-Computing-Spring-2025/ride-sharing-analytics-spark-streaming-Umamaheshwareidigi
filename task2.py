from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, sum, avg
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

# Initialize Spark session
spark = SparkSession.builder \
    .appName("RideSharingStreamingAggregation") \
    .getOrCreate()

# Define schema for the incoming data
schema = StructType([
    StructField("trip_id", StringType(), True),
    StructField("driver_id", IntegerType(), True),
    StructField("distance_km", FloatType(), True),
    StructField("fare_amount", FloatType(), True),
    StructField("timestamp", StringType(), True)
])

# Ingest data from socket
ride_data_stream = spark.readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()

# Parse the incoming JSON data into columns
ride_events = ride_data_stream.select(from_json(col("value"), schema).alias("data")).select("data.*")

# Perform real-time aggregations
aggregated_data = ride_events.groupBy("driver_id") \
    .agg(
        sum("fare_amount").alias("total_fare"),
        avg("distance_km").alias("avg_distance")
    )

# Output the aggregation result to a CSV file
query = aggregated_data.writeStream \
    .outputMode("append") \
    .format("csv") \
    .option("path", "output/aggregated_data") \
    .option("checkpointLocation", "checkpoint_aggregated") \
    .trigger(processingTime="10 seconds") \
    .start()

query.awaitTermination()
