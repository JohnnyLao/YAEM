code-format:
	black .
	isort .

migrate:
	python manage.py makemigrations
	python manage.py migrate

dumpdata:
	python manage.py dumpdata > data.json

loaddata:
	python manage.py loaddata data.json