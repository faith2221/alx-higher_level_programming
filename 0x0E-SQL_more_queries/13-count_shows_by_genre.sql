-- Script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each

SELECT genre, COUNT(*) AS number_of_shows
FROM shows
WHERE genre IS NOT NULL AND genre != ""
GROUP BY genre
ORDER BY number_of_shows DESC;
