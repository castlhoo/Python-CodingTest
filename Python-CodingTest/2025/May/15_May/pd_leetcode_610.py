# 610. Triangle Judgement
# Solved
# Easy
# Topics
# Companies
# SQL Schema
# Pandas Schema
# Table: Triangle

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | x           | int  |
# | y           | int  |
# | z           | int  |
# +-------------+------+
# In SQL, (x, y, z) is the primary key column for this table.
# Each row of this table contains the lengths of three line segments.
 

# Report for every three line segments whether they can form a triangle.

# Return the result table in any order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Triangle table:
# +----+----+----+
# | x  | y  | z  |
# +----+----+----+
# | 13 | 15 | 30 |
# | 10 | 20 | 15 |
# +----+----+----+
# Output: 
# +----+----+----+----------+
# | x  | y  | z  | triangle |
# +----+----+----+----------+
# | 13 | 15 | 30 | No       |
# | 10 | 20 | 15 | Yes      |
# +----+----+----+----------+

import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    cond1 = triangle['x'] + triangle['y'] > triangle['z']
    cond2 = triangle['x'] + triangle['z'] > triangle['y']
    cond3 = triangle['z'] + triangle['y'] > triangle['x']

    valid = cond1 & cond2 & cond3

    triangle['triangle'] = np.where(valid, 'Yes', 'No')
        
    return triangle