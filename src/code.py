from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType

def translate(english):
    if english == "1":
        return "uno"
    elif english == "2":
        return "dos"
    else:
        return f"Cannot translate {english}"


translation_udf = udf(lambda english: translate(english), StringType())

def transform_data(df):
    return df.withColumn("spanish", translation_udf(col("english")))