import sqlite3
"""Just testing out some functions."""

conn = sqlite3.connect('chinook.db')

conn.row_factory = sqlite3.Row

curs = conn.cursor()

query = "SELECT * FROM artists LIMIT 10;"

# query = 'SELECT COUNT(*) FROM armory_item;'

# curs.execute(query)

query = """
SELECT
	 artists.ArtistId
	,artists.Name
	,count(distinct tracks.TrackId) as track_count
	-- ,tracks.Name
	-- ,albums.AlbumId
	-- ,albums.Title
FROM tracks
JOIN albums on albums.AlbumId = tracks.AlbumId
JOIN artists on artists.ArtistId = albums.ArtistId
group by artists.ArtistId
"""

results = curs.execute(query).fetchall()

breakpoint()
