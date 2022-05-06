from tests.test_spark import spark_session_fixture
from src.code import transform_data

def test_function(spark_session):
    input_df = spark_session.createDataFrame(
        [
            ("1",),
            ("2",),
            ("3",),
        ],
        ["english"],
    )
    output_df = transform_data(input_df)
    expected_df = spark_session.createDataFrame(
        [
            ("1","uno"),
            ("2","dos"),
            ("3","Cannot translate 3"),
        ],
        ["english", "spanish"],
    )
    assert expected_df.sort(["english"]).collect() == output_df.sort(["english"]).collect()
