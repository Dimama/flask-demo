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
