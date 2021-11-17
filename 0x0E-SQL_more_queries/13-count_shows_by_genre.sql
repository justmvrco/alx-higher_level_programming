-- lists all shows in hbtn_0d_tvsows that have at least 1 genre linked
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_shows
       FROM tv_show_genres
       INNER JOIN tv_genres
       ON tv_genres.id = tv_show_genres.genre_id
       GROUP BY tv_genres.name
       ORDER BY number_shows DESC;

