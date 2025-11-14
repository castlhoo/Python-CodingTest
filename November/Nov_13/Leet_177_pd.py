# 177. Nth Highest Salary
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# SQL Schema
# Pandas Schema
# Table: Employee

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | salary      | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains information about the salary of an employee.
 

# Write a solution to find the nth highest distinct salary from the Employee table. If there are less than n distinct salaries, return null.

# The result format is in the following example.

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee[['salary']].drop_duplicates()
    employee['rank'] = employee['salary'].rank(method='dense', ascending = False)
    result = employee.loc[employee['rank'] == N, 'salary']

    value = result.iloc[0] if not result.empty else float('nan')
    output = pd.DataFrame({f"getNthHighestSalary({N})" : [value]})
    return output