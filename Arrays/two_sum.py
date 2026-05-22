# Two Sum
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[num] = i
SQL/employees_highest_salary.sql
SELECT e1.name AS Employee
FROM Employee e1
JOIN Employee e2
ON e1.managerId = e2.id
WHERE e1.salary > e2.salary;
README.md
# LeetCode Solutions 🚀

This repository contains my LeetCode problem solutions.

## Languages
- Python
- SQL

## Topics
- Arrays
- Strings
- SQL Queries

## Profile
- LeetCode: https://leetcode.com/
- GitHub: https://github.com/Rakesh051204
leetcode-solutions/
│
├── Arrays/
│   ├── two_sum.py
│   ├── best_time_to_buy_sell_stock.py
│
├── Strings/
│   ├── longest_palindromic_substring.py
│
├── SQL/
│   ├── employees_highest_salary.sql
│
├── README.md
