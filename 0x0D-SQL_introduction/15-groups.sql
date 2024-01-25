-- Grouping
SELECT score, count(name) AS number FROM second_table GROUP BY score
ORDER BY score DESC;
