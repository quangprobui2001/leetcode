--
-- @lc app=leetcode id=596 lang=mysql
--
-- [596] Classes More Than 5 Students
--

-- @lc code=start
# Write your MySQL query statement below
select `class` 
from (select `class`, count(distinct `student`) as `num`
     from `courses`
     group by `class`) as `tmp_table` 
where `num` >= 5;
-- @lc code=end

