-- Script that lists all Comedy shows in the database hbtn_0d_tvshows

SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_genres.id= tv_show_genres.genre_id
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.name = "Comedy"
ORDER BY tv_genres.title;
