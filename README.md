# Sparkify
## Intro
sparkify is a music application where we can access records of users and their activity listening to music, the analytical goal is to be able to have insights on users behaviour in a specific session, are they paying customers? what artists are they usually listening to? when do they tend to use the app? a lot of questions could be addressed in this dataset
## Python scripts
It's so simple running the python scripts, just run "python create_tables.py" to create the tables and "python etl.py" to run the ETL process

## Design
Star schema have been used for this project with a fact table of songplays where we have session data for users, and a number of dimension tables including:
> -  songs table with all songs data (id , duration, name, etc..)
> -  artists table with all artists data (id, name, location, etc..)
> -  user table with all users data (id, name, level,etc..)
> -  time table for start of session segmented in different blocks to be used for analytical purposes (hour, day, week, month, year, etc..)