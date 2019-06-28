
# Project Name: Data Modeling with Postgres

<H2> Project Overview: </H2>
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app.The analytics team is particularly interested in understanding  what songs users are listening to. All the activity of the users and the metadata of the songs available in the app are listed in json files at location with directory name as "data". 

<H2>Project Aim: </H2>
Sparkify like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis. The role of a data engineer is mainly to determine what data model to use and create a data model specific database schema and also appropriate ETL pipeline to bring the data from json files to postgres database tables for sparkify to do their required analysis. 

<H2> Project Description</H2>
After thoroughly reading through the requirement and understanding the data and needs of sparkify, for analysis team to understand the user activity on the app they need necessary statistics of the activities and the results that are retrieved should be fast and accurate. The primary reason dimensional modeling is its ability to allow data to be stored in a way that is optimized for information retrieval once it has been stored in a database.Dimensional models are specifically designed for optimized for the delivery of reports and analytics.It also provides a more simplified structure so that it is more intuitive for business users to write queries. Tables are de-normalized and are few tables which will have few joins to get the results with high performance. 

<H2>Dimensional Modelling: </H2>
A dimensional model is also commonly called a star schema.The core of the star schema model is built from fact tables and dimension tables. It consists, typically, of a large table of facts (known as a fact table), with a number of other tables surrounding it that contain descriptive data, called dimensions. 

<H2>Fact Table: </H2>
The fact table contains numerical values of what you measure. Each fact table contains the keys to associated dimension tables. Fact tables have a large number of rows.The information in a fact table has characteristics. It is numerical and used to generate aggregates and summaries. All facts refer directly to the dimension keys. Fact table that is determined after carefull analysis which contains the information.Fact table will have data where page column listed as "NextSong" 

<H2>Tables (Facts) </H2>
Table Name: Songplay(fact)
Column Names: songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent


<H2> Dimension Tables: </H2>
The dimension tables contain descriptive information about the numerical values in the fact table. 

<H2>Tables ( Dimensions )</H2>

Table Name:Songs (Song Dimension)
Column Names: song_id, title, artist_id, year, duration

Table Name: Artists (Artist Dimension)
Column Names: artist_id, name, location, lattitude, longitude

Table Name:Users (User Dimension)
Column Names: user_id, first_name, last_name, gender, level

Table Name: Time (Time Dimension)
Column Names: start_time, hour, day, week, month, year, weekday


<H2> Database creation Approach: </H2>
Implement all the database DDL and DML statements in the sql_queries.py that create all the dimension tables and fact tables with all necessary columns. Build an ETL pipeline to extract data from the Json files from the local directory and  push the data into necessary dimensions and fact tables. 

 
<H2> Database Design scripts : </H2>
create_tables.py : This is the first script that need to be executed. The main purpose of this script is to connect to postgres as an admin user and creates a database "sparkifydb" with UTF8 encoding. Then it takes all the Drop table variables list and drops the tables if exists and creates the tables with the help of DDL statements that are imported from sql_queries.py file. 

sql_queries.py: This file contains all the DDL and DML statements that are necessary to drop,create tables and Insert data when it is being retrived form the json file and being pushed to the tables in ETL pipeline.

<H2> Unit Test approach: </H2>
etl.ipynb: This is the script which get all the file names and process through single file and loads the data into the dimension tables and fact tables. Once the dry run is complete , then update the main etl script that completes all the processing of the files and loads entire dataset.

<H2> Test Script </H2> 
test.ipynb: This script is used to validate the data that is being loaded into the tables as part of unit testing and also as part of main data load. 

<H2>ETL Pipeline Script:</H2>
etl.py: This is the next script that is executed which grabs each file and process it and loads data into songs, artists, users dimensions. Then the time dimension is being loaded using the time stamp column. Fact tables are loaded finally to the complete the whole loading process.

<H1> SQL queries for Analysis: </H1>

Scenario 1: Sparkify want to analyse how many users are paid and free please find the Query to get the results. 

SELECT u.level, count(distinct u.user_id) Account_type  
FROM songplays sp join users u on sp.user_id = u.user_id 
group by u.level

Scenario 2: sparkify want to analyse how many times the user accessed the apps, to get the activity count please use below query

SELECT u.level, u.first_name,u.last_name , count(distinct session_id) user_activity  
FROM songplays sp join users u on sp.user_id = u.user_id 
group by u.level,u.first_name,u.last_name

Scenario 3 : sparkify want to analyse how many uses are accessing the app on the monthly and weekly basis. 

SELECT t.month , count(distinct u.user_id) user_activity  
FROM songplays sp join users u on sp.user_id = u.user_id  join time t on sp.start_time = t.start_time 
group by t.month


SELECT t.month,t.week , count(distinct u.user_id) user_activity  
FROM songplays sp join users u on sp.user_id = u.user_id  join time t on sp.start_time = t.start_time 
group by t.month,t.week





