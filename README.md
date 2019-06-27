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

* Make migrations for djangop

```
	python manage.py makemigrations
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
