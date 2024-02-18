SELECT tv_shows.title
FROM tv_shows
LEFT JOIN (
    SELECT show_id
    FROM tv_show_genres
    WHERE genre_id = (
            SELECT id
            FROM tv_genres
            WHERE name = 'Comedy'
	)
 ) AS comedy_shows ON tv_shows.id = comedy_shows.show_id
 WHERE comedy_shows.show_id IS NULL
 ORDER BY tv_shows.title ASC;
