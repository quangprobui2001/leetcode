--
-- @lc app=leetcode id=181 lang=mysql
--
-- [181] Employees Earning More Than Their Managers
--

-- @lc code=start
# Write your MySQL query statement below
select a.Name as `Employee`
from `Employee` as a join `Employee` as b
on a.ManagerId = b.Id
and a.Salary > b.Salary
-- @lc code=end

