# WatchInSGE
SGE open source

## Intallation

### Backend

* Make python virtualenv

```
	mkvirtualenv intranet --python=/usr/bin/python3
```

* Intall requirements

```
	pip install -r requirements.txt
```

* Make migrations for django and load initial data

```
	python manage.py makemigrations utils company users
```

```
    python manage.py migrate  
```

```
    python manage.py loaddata fixtures/initial_data_groups.json fixtures/initial_data_user.json fixtures/initial_data_sorter.json
```

* Run project

```
	python manage.py runserver
```

### Frontend

* Install

```
	cd frontend/
	npm install
```

* Run

```
	npm run serve
```

User: admin
pass: watchin123456