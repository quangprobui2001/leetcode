--
-- @lc app=leetcode id=1280 lang=mysql
--
-- [1280] Students and Examinations
--

-- @lc code=start
# Write your MySQL query statement below
SELECT s.student_id, s.student_name, su.subject_name, 
(SELECT COUNT(1) 
	FROM Examinations 
	WHERE student_id = s.student_id 
	AND subject_name = su.subject_name) AS attended_exams
FROM Students s
JOIN Subjects su
 ORDER BY s.student_id, su.subject_name
-- @lc code=end

