-- genres
SELECT name FROM tv_genres 
JOIN tv_show_genres ON id=tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id=tv_shows.id
where tv_shows.title="Dexter" ORDER BY name;
