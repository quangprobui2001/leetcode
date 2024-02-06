--
-- @lc app=leetcode id=197 lang=mysql
--
-- [197] Rising Temperature
--

-- @lc code=start
# Write your MySQL query statement below
select a.id as "Id"
from weather a, weather b
where dateDiff(a.recordDate , b.recordDate) = 1 
      and a.temperature > b.temperature
-- @lc code=end

