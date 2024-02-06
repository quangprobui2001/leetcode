--
-- @lc app=leetcode id=1084 lang=mysql
--
-- [1084] Sales Analysis III
--

-- @lc code=start
# Write your MySQL query statement below
SELECT DISTINCT p.product_id, p.product_name
FROM Product p JOIN Sales s USING(product_id)
WHERE sale_date BETWEEN "2019-01-01" AND "2019-03-31"
AND p.product_id NOT IN (
    SELECT p2.product_id FROM Product p2 JOIN Sales s2 USING(product_id)
    WHERE sale_date > "2019-03-31" OR sale_date < "2019-01-01")
ORDER BY p.product_id
;
-- @lc code=end

