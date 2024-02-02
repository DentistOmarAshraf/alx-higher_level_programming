-- Show all shows (comedy)
SELECT sh.title
FROM tv_genres gen
INNER JOIN tv_show_genres tg ON gen.id = tg.genre_id
INNER JOIN tv_shows sh ON tg.show_id=sh.id
WHERE name='Comedy'
ORDER BY sh.title;
