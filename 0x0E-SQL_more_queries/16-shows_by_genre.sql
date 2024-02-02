-- list all shows and all genere linked to show
SELECT sh.title, tg.name
FROM tv_shows sh
LEFT JOIN tv_show_genres ge ON sh.id=ge.show_id
LEFT JOIN tv_genres tg ON tg.id=ge.genre_id
ORDER BY sh.title, tg.name;
