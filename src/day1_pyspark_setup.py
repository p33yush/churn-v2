from pyspark.sql import SparkSession
import os
import time

def main():
    print("="*50)
    print(" DAY 1: PySpark Setup & Big Data Loading ")
    print("="*50)
    
    # 1. Initialize PySpark Session
    print("\n[1/4] Initializing PySpark Session...")
    # Allocating 4GB to driver and executor to comfortably handle the 10M rows dataset locally
    spark = SparkSession.builder \
        .appName("CustomerChurnAnalyticsV2") \
        .config("spark.driver.memory", "4g") \
        .config("spark.executor.memory", "4g") \
        .getOrCreate()
        
    print(f"PySpark Version: {spark.version}")
        
    # 2. Define data path
    print("\n[2/4] Validating data path...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, '..', 'data', 'raw', 'customer_churn_10M.csv')
    
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found.")
        print("Please run 'python generate_10m_data.py' first to generate the dataset!")
        spark.stop()
        return

    # 3. Load the 10M dataset
    print(f"\n[3/4] Loading 10M dataset from {data_path}...")
    start_time = time.time()
    
    # Using PySpark's DataFrame API to read CSV
    df = spark.read.csv(
        data_path,
        header=True,
        inferSchema=True
    )
    
    load_time = time.time() - start_time
    print(f"Data loaded in {load_time:.2f} seconds.")
    
    # 4. Basic exploration
    print("\n[4/4] Exploring Dataset...")
    
    print("\nDataset Schema:")
    df.printSchema()
    
    print("Calculating Total Rows (This triggers a Spark Action)...")
    action_start = time.time()
    count = df.count()
    action_time = time.time() - action_start
    print(f"Total Rows: {count:,} (Count took {action_time:.2f} seconds)")
    
    print("\nFirst 5 Rows:")
    df.show(5, truncate=False)
    
    print("\n" + "="*50)
    print(" SUCCESS: PySpark setup complete and working successfully! ")
    print("="*50)
    
    # Stop session to free up resources
    spark.stop()

if __name__ == "__main__":
    main()
