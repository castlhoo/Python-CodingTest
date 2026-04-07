# 176. Second Highest Salary
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
 

# Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

# The result format is in the following example.

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee['rank'] = employee['salary'].rank(method='dense', ascending=False)
    result = employee.loc[employee["rank"]==2, 'salary']

    value = result.iloc[0] if not result.empty else float('nan')
    output = pd.DataFrame({"SecondHighestSalary" : [value]})
    return output