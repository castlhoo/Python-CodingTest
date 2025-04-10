# 180. Consecutive Numbers
# Solved
# Medium
# Topics
# Companies
# SQL Schema
# Pandas Schema
# Table: Logs

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | num         | varchar |
# +-------------+---------+
# In SQL, id is the primary key for this table.
# id is an autoincrement column starting from 1.
 

# Find all numbers that appear at least three times consecutively.

# Return the result table in any order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Logs table:
# +----+-----+
# | id | num |
# +----+-----+
# | 1  | 1   |
# | 2  | 1   |
# | 3  | 1   |
# | 4  | 2   |
# | 5  | 1   |
# | 6  | 2   |
# | 7  | 2   |
# +----+-----+
# Output: 
# +-----------------+
# | ConsecutiveNums |
# +-----------------+
# | 1               |
# +-----------------+
# Explanation: 1 is the only number that appears consecutively for at least three times.

import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs = logs.astype({"num" : "int64"})
    answer = logs["num"].tolist()
    n = len(answer)

    result = set()

    for i in range(n - 2):
        if answer[i] == answer[i+1] == answer[i+2]:
            result.add(answer[i])
    return pd.DataFrame({"ConsecutiveNums" : sorted(result)})