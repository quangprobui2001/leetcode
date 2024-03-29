--
-- @lc app=leetcode id=607 lang=mysql
--
-- [607] Sales Person
--

-- @lc code=start
# Write your MySQL query statement below
select name
from salesperson 
where name not in 
(select sp.name
from salesperson sp
join orders o on sp.sales_id=o.sales_id
join company c on o.com_id=c.com_id
where c.name='Red')
-- @lc code=end

