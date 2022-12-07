# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "drop table if exists songs"
artist_table_drop = 'DROP TABLE IF EXISTS artists'
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE if not exists songplays (
        songplay_id SERIAL primary key,
        start_time timestamp not null ,
        user_id int not null,
        level text not null,
        song_id text ,artist_id text  ,
        session_id text not null,
        location text not null,
        user_agent text not null)
    """)

user_table_create = ("""
    CREATE TABLE users ( 
        user_id int primary key,
        first_name text,
        last_name text,
        gender text,
        level text UNIQUE NOT NULL)
    """)

song_table_create = (""" 
    CREATE TABLE songs (
        song_id text primary key,
        title text not null,
        artist_id text not null,
        year int not null,
        duration float not null)
    """)

artist_table_create = ("""
    CREATE TABLE if not exists artists (
        artist_id text primary key,
        name text not null,
        location text,
        latitude float,
        longitude float )
    """)

time_table_create = ("""
    CREATE TABLE time (
        start_time timestamp primary key,
        hour int,
        day int,
        week int,
        month int,
        year int,
        weekday int )
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (
        songplay_id ,
        start_time ,
        user_id, 
        level ,
        song_id ,
        artist_id  ,
        session_id ,
        location ,
        user_agent ) 
            values (DEFAULT,%s,%s,%s,%s,%s,%s,%s,%s) 
            on conflict(songplay_id) do nothing
""") 

user_table_insert = ("""
    INSERT INTO users (
        user_id ,
        first_name ,
        last_name , 
        gender , 
        level )
            values (%s,%s,%s,%s,%s) 
                on conflict(Level) do update 
                SET level=EXCLUDED.level
""")

song_table_insert = ("""
    INSERT INTO songs (
        song_id,
        title,
        artist_id,
        year,
        duration) 
            values (%s,%s,%s,%s,%s)  
                on conflict(song_id) do nothing
""")

artist_table_insert = ("""
    INSERT INTO artists (
        artist_id   ,
        name ,
        location , 
        latitude , 
        longitude  )
            values (%s,%s,%s,%s,%s) 
                on conflict(artist_id) do nothing
""")


time_table_insert = (""" 
    INSERT INTO time (
        start_time , 
        hour ,
        day ,
        week ,
        month ,
        year , 
        weekday ) 
            values (%s,%s,%s,%s,%s,%s,%s) 
                on conflict(start_time) do nothing
    """)

# FIND SONGS

song_select = (""" 
    SELECT artists.artist_id, songs.song_id 
    FROM artists 
    JOIN songs 
    ON artists.artist_id=songs.artist_id 
    WHERE (songs.title= %s AND artists.name= %s AND songs.duration= %s)
    """)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]