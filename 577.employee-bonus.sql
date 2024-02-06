--
-- @lc app=leetcode id=577 lang=mysql
--
-- [577] Employee Bonus
--

-- @lc code=start
# Write your MySQL query statement below
select name, bonus
from employee
left join bonus on employee.empid=bonus.empid
where bonus is null or bonus<1000
-- @lc code=end

