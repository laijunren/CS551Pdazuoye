# MusicCulturalProject

>Student ID:52211518
>
>Full Name:Junren Lai
>
>Project Url:

### Project introduction:

This project is to explore the relationship between the styles of many music artists and the popular elements of their times, and then analyze which style the public prefer.

### Data sources：

Data from http://millionsongdataset.com/pages/getting-dataset/，

[SQLite database](http://www.ee.columbia.edu/~thierry/artist_term.db) linking artist ID to the tags (Echo Nest and musicbrainz ones)

The data is filtered here. 2000 data in the artist term table, 1997 data in the artist mbtag, and 717 data in the artists table are retained

## Technology selection:

Back-end: flask network framework, sqlite3 data storage

Template：jinjia2

### Project structure：

`dataset`: Store public data directory

​	`mbtag.csv`: 1997 data of mbtag and artist_id

​	`term.csv`: 2000 term and artist_id data

`features`: behave test

​	`driver`:  chrome driver

​		`chromedriver.exe`: chrome driver

​	`steps`: testing procedure

​		`customers.py` testing procedure

​	`customers.feature`: feature

​	`enviroment.py`: enviroment

`templates`: Directory where the web page template is stored

​	`index.html`: Website homepage file

​	`artist_term.html`: term page file

​	`artist_mbtag.html`: mbtag page file

`.gitignore`:gitIgnore uploaded files

`app.py`:Project entry file

`artist_style.db`:Database file

`setup_db.py`: Initialize site database script file

`requirements.txt`: Virtual environment dependency package file

`git-log.txt`:gitSubmit record documents

### Database design：

Table structure design of sqlite3 database used in this project：

`artist` table:Table for storing artist_id

​	artist_id: artist_id

`mbtag_artist`:Table storing the corresponding relationship between artist_id and mbtag

​	artist_id: artist_id

​	mbtag: mbtag

`term_artist`:A table storing the corresponding relationship between artist_id and term

​	artist_id: artist_id

​	term: term

### Function realization：

Visit the home page to get the data volume statistics of the three tables in the database, and jump to the mbtag statistics page or term statistics page

Visit the mbtag page to get the number and specific content of the de-duplicated mbtag in the database, and make statistics on the maximum associated amount of mgtag and the associated amount of artists

Visit the term page to get the number of terms in the database after duplication removal and the specific content, and make statistics on the maximum number of terms associated with artists

Provide a script to import csv data into the database



