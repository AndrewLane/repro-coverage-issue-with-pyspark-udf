
import pytest
from pyspark import SparkConf
from pyspark.sql import SparkSession

@pytest.fixture(name="spark_session", scope="session")
def spark_session_fixture(request):
    """
        fixture for creating a spark session
    Args:
        request: pytest.FixtureRequest object
    """
    spark_conf = (
        SparkConf()
        .setMaster("local[*]")
        .setAppName("pytest-pyspark2-local-testing")
        .set("spark.driver.host", "127.0.0.1")
        .set("spark.driver.bindAddress", "127.0.0.1")
    )
    spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()

    return spark
