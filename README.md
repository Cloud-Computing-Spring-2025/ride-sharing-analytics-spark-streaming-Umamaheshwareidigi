# ride-sharing-spark-streaming
Spark structured streaming example
This project builds a real-time analytics pipeline for a ride-sharing platform using Apache Spark Structured Streaming. It processes streaming data, performs real-time aggregations, and analyzes trends over time.

## Prerequisites

Ensure you have the following installed:
- Python 3.x
- Apache Spark
- PySpark
- Faker (for generating sample data)

Install the required packages:
```sh
pip install pyspark 
```
```bash
pip install faker
```

## Project Structure

The project consists of three main tasks:
1. **Ingest and Parse Real-Time Ride Data**
2. **Perform Real-Time Aggregations on Driver Earnings and Trip Distances**
3. **Analyze Trends Over Time Using a Sliding Time Window**

## Task 1: Basic Streaming Ingestion and Parsing

### Steps:
1. Create a Spark session.
2. Read streaming data from a socket (localhost:9999).
3. Parse JSON messages into a structured DataFrame.
4. Print the parsed data to the console.

### Sample Input:
```json
{"trip_id": "7aa62e6e-cf96-4088-a8c7-bcdc2e5be135", "driver_id": 94, "distance_km": 46.63, "fare_amount": 83.06, "timestamp": "2025-04-02 19:13:52"}
```

### Sample Output:
```csv
trip_id,driver_id,distance_km,fare_amount,timestamp
bd340ace-feee-4a5d-b0ea-dcb62f71f18f,71,25.1,81.75,2025-04-01 17:45:51
```
Execute the script with:
```sh
spark-submit task1.py
```

## Task 2: Real-Time Aggregations (Driver-Level)

### Steps:
1. Reuse the parsed DataFrame from Task 1.
2. Group by `driver_id` and compute:
   - Total fare amount (`SUM(fare_amount) as total_fare`)
   - Average distance (`AVG(distance_km) as avg_distance`)
3. Output the aggregations to the console and store them in a CSV file.

### Sample Output:
```csv
driver_id,total_fare,avg_distance
73,134.86,34.25
3,122.71,17.47
```
Execute the script with:
```sh
spark-submit task2.py
```
## Task 3: Windowed Time-Based Analytics

### Steps:
1. Convert `timestamp` column to `TimestampType`.
2. Perform a 5-minute windowed aggregation on `fare_amount`, sliding by 1 minute.
3. Output the windowed results to a CSV file.

### Sample Output:
```csv
window_start,window_end,total_fare
2025-04-02T19:11:00.000Z,2025-04-02T19:16:00.000Z,9340.97
```

## Execution Commands


### Run the Spark Streaming Script
Execute the script with:
```sh
spark-submit task3.py
```

This will process the real-time ride-sharing data and generate analytics outputs.

## Conclusion
By completing this project, you gain hands-on experience with:
- Apache Spark Structured Streaming
- Real-time data processing
- Aggregation and window functions in Spark

