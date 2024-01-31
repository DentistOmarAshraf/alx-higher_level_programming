-- Left Join
SELECT sh.title, gen.genre_id
FROM tv_shows sh
LEFT JOIN tv_show_genres gen
ON sh.id = gen.show_id
WHERE gen.show_id IS NULL ORDER BY title, genre_id;
