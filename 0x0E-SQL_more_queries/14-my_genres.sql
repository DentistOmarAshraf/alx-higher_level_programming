-- Find Genre of movie
SELECT tg.name AS name
FROM tv_shows sh
INNER JOIN tv_show_genres gen ON sh.id=gen.show_id
INNER JOIN tv_genres tg ON gen.genre_id=tg.id
WHERE sh.title='Dexter' ORDER BY tg.name ASC;
