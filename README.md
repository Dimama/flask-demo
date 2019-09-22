# flask-demo

### Requirements
- Python 3.6
- PostgreSQL/SQLite

### [PostrgeSQL setup](https://www.postgresql.org/docs/10/tutorial-install.html)
```
$ psql -h localhost -U postgres
> CREATE database flaskdemo;
> CREATE role program WITH password 'password';
> GRANT ALL PRIVILEGES ON database flaskdemo TO program;
> ALTER role program WITH login;
> \q
$ psql -h localhost -U program flaskdemo
```

### Setup
- `pip install -r requirements.txt`

### Run
- `python app.py`

### API
| URI| METHOD| Description | PARAMS|
| :---:              | :---:|    :---:      |:---: |
|/artist| POST | create artist| Required: name, genre | 
|/artist| GET | get all artists| - |
|/artist/<artist_id>| GET | get artist| artist_id |
|/artist/<artist_id>| DELETE | delete artist| artist_id |
|  | |  | |
|/track| POST | create track| Required: artist, name | 
|/track/<track_id>| GET | get track| track_id |
|/track/<track_id>| DELETE | delete track| track_id | 