# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS times;"

# CREATE TABLES
# Create statement for songplays fact table. Primary key is songplay_id which is generated when record is inserted
songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(songplay_id SERIAL PRIMARY KEY ,
                                                                     start_time timestamp,
                                                                     user_id int REFERENCES users(user_id),
                                                                     level varchar, 
                                                                     song_id varchar REFERENCES songs(song_id), 
                                                                     artist_id varchar REFERENCES artists(artist_id), 
                                                                     session_id int, 
                                                                     location varchar, 
                                                                     user_agent varchar                                                                     
                                                                     );
""")

# Create statement for user dimension table. Contains all information related to Users. Primary Key is user_id
user_table_create = ("""CREATE TABLE IF NOT EXISTS users(user_id int NOT NULL,
                                                            first_name varchar,
                                                            last_name varchar,
                                                            gender varchar, 
                                                            level varchar, 
                                                            CONSTRAINT pk_on_user_id PRIMARY KEY(user_id));
""")

# Create statement for songs dimension table. Contains all information related to songs. Primary Key is song_id
song_table_create = ("""CREATE TABLE IF NOT EXISTS songs(song_id varchar NOT NULL,
                                                            title varchar,
                                                            artist_id varchar,
                                                            year int, 
                                                            duration NUMERIC(10,5),
                                                            CONSTRAINT pk_on_song_id PRIMARY KEY(song_id));
""")

# Create statement for artist dimension table. Contains all information related to artists. Primary Key is artist_id
artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists(artist_id varchar NOT NULL,
                                                              name varchar,
                                                              location varchar,
                                                              latitude NUMERIC(10,5),
                                                              longitude NUMERIC(10,5),
                                                              CONSTRAINT pk_on_artist_id PRIMARY KEY(artist_id));
""")

# Create statement for time dimension table. Contains all information related to time. Primary Key is start_time
time_table_create = ("""CREATE TABLE IF NOT EXISTS time(start_time timestamp NOT NULL,
                                                           hour int,
                                                           day int, 
                                                           week int,
                                                           month int, 
                                                           year int, 
                                                           weekday int,
                                                           CONSTRAINT pk_on_start_time PRIMARY KEY(start_time)
                                                           );
""")

# # INSERT RECORDS

# Insert statement for songplay fact table
songplay_table_insert = ("""INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                               VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""")

# Insert statement for user dimension table. Added conflict on user_id to handle the two records which has free and paid account. updates the record with later value for lebel column 
user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level """)

# Insert statement for song dimension table. Added conflict on song_id to handle the duplicate records 
song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO NOTHING """)

# Insert statement for artist dimension table. Added conflict on artist_id to handle the duplicate records 
artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING """)

# Insert statement for time dimension table. Added conflict on time_id to handle the duplicate records 
time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) DO NOTHING """)

# # FIND SONGS
# to get the song_id and artist_id to insert into songplay table
song_select = ("""select s.song_id,a.artist_id from songs s join artists a on s.artist_id = a.artist_id where s.title = %s and a.name = %s and s.duration = %s""")


# QUERY LISTS

create_table_queries = [ user_table_create, song_table_create, artist_table_create, time_table_create,songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]