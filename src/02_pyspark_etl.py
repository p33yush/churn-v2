import os
import pandas_gbq
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

# Point to your downloaded Google Cloud key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google_key.json"

print(" Starting PySpark ETL Pipeline...")

# 1. Initialize Spark (Pure PySpark, no external Java downloads!)
spark = SparkSession.builder \
    .appName("CustomerChurnV2_ETL") \
    .config("spark.driver.memory", "4g") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")
input_path = "../data/raw/customer_churn_1M.csv"

# 2. Extract
print(" Extracting 1M row dataset...")
df = spark.read.csv(input_path, header=True, inferSchema=True)

# 3. Transform
print(" Engineering new business features...")
df_cleaned = df.withColumn("totalcharges", col("totalcharges").cast("double")) \
               .fillna({"totalcharges": 0.0})

df_transformed = df_cleaned \
    .withColumn(
        "is_high_value",
        when(col("monthlycharges") > 70.0, 1).otherwise(0)
    ) \
    .withColumn(
        "tenure_group",
        when(col("tenure") <= 12, "0-1 Year")
        .when((col("tenure") > 12) & (col("tenure") <= 24), "1-2 Years")
        .when((col("tenure") > 24) & (col("tenure") <= 48), "2-4 Years")
        .otherwise("4+ Years")
    )

print("\n Converting PySpark to Pandas to bypass Windows Hadoop bug...")
df_pandas = df_transformed.toPandas()

# 4. Load (BigQuery via Pandas Bridge)
PROJECT_ID = "churn-v2"  # Your project ID
TABLE_ID = "churn_data.customer_features"

print(f" Uploading to Google BigQuery ({PROJECT_ID}.{TABLE_ID})...")
pandas_gbq.to_gbq(
    df_pandas, 
    TABLE_ID, 
    project_id=PROJECT_ID, 
    if_exists="replace"
)

print(f"SUCCESS! 1M rows loaded into BigQuery!")
