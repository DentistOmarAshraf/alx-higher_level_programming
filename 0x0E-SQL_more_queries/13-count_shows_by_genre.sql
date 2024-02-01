-- Show Inner JOIN
SELECT gen.name AS genre, count(shg.genre_id) AS number_of_shows
FROM tv_genres gen JOIN tv_show_genres shg ON gen.id=shg.genre_id
GROUP BY genre_id
ORDER BY count(shg.genre_id) DESC
