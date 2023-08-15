-- displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(value) as avg_temp
WHERE month = "July" AND "August"
GROUP BY city
ORDER BY temp DESC
LIMIT 3
