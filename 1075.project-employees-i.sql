--
-- @lc app=leetcode id=1075 lang=mysql
--
-- [1075] Project Employees I
--

-- @lc code=start
# Write your MySQL query statement below
select project_id , round(avg(experience_years), 2) as average_years
from project as p
left join employee as e
on p.employee_id = e.employee_id
group by project_id
-- @lc code=end

