--
-- @lc app=leetcode id=620 lang=mysql
--
-- [620] Not Boring Movies
--

-- @lc code=start
# Write your MySQL query statement below
SELECT *
FROM cinema
WHERE id MOD 2 <> 0 AND description <> "boring"
ORDER BY rating DESC
-- @lc code=end

