import pandas as pd
import numpy as np
import duckdb

# Read and load data 
df = pd.read_csv("C:/Users/lenovo/Downloads/soccer_heights_sample.csv", sep = ',')
heights = pd.DataFrame(df)
print(heights)
heights.isna().sum()

def summary_statistic(df):
    return heights.describe()

print(summary_statistic(heights))

position_counts = heights['position'].value_counts()
print(position_counts)




def missing_value_count(df):
    missing_values_count = df.isnull().sum()
    return missing_values_count
print(missing_value_count(heights))

# 13 missing values for foot


def means_for_position():
    position_means = duckdb.sql("""
    SELECT position,avg(height_in_cm) as mean_height
    FROM heights
    GROUP BY position
    """).to_df()
    return position_means
print(means_for_position())


  
position_value = duckdb.sql("""
      select case when position = 'Goalkeeper' then height_in_cm end as Goalkeeper,
             case when position = 'Defender' then height_in_cm end as Defender,
             case when position = 'Midfield' then height_in_cm end as Midfield,
             case when position = 'Attack' then height_in_cm end as Attack 
      from heights
  """).to_df()
print(position_value)



