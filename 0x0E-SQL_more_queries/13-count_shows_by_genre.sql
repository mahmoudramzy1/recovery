-- geners.
SELECT name AS genre, COUNT(*) AS number_of_shows FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id=tv_genres.id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
