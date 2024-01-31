-- Left Join
SELECT sh.title, gen.genre_id
FROM tv_shows sh
LEFT JOIN tv_show_genres gen
ON sh.id = gen.show_id
ORDER BY title, genre_id;
