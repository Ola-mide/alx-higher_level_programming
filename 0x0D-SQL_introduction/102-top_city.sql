-- a script that displays the top 3 of cities temperature during
-- July and August ordered by temperature (descending)

WITH temporary AS (
	SELECT * FROM temperatures
	WHERE month BETWEEN 7 AND 8)
SELECT city, AVG(value) AS avg_temp FROM temporary GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
