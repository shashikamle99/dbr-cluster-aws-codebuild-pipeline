# Filename: test_addcol.py
import pytest
from pyspark.sql import SparkSession
from dabdemo.addcol import *

class TestAppendCol(object):

  def test_with_status(self):
    spark = SparkSession.builder.getOrCreate()

    source_data = [
      ("paula", "white", "paula.white@example.com"),
      ("john", "baer", "john.baer@example.com")
    ]

    source_df = spark.createDataFrame(
      source_data,
      ["first_name", "last_name", "email"]
    )

    actual_df = with_status(source_df)

    expected_data = [
      ("paula", "white", "paula.white@example.com", "checked"),
      ("john", "baer", "john.baer@example.com", "checked")
    ]
    expected_df = spark.createDataFrame(
      expected_data,
      ["first_name", "last_name", "email", "status"]
    )

    assert(expected_df.collect() == actual_df.collect())
