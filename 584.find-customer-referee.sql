--
-- @lc app=leetcode id=584 lang=mysql
--
-- [584] Find Customer Referee
--

-- @lc code=start
# Write your MySQL query statement below
select name
from customer
where referee_id != 2 or referee_id is NULL
-- @lc code=end

