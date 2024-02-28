code-format:
	black --skip-string-normalization .
	isort .

migrate:
	python manage.py makemigrations
	python manage.py migrate

dumpdata:
	python manage.py dumpdata > data.json

loaddata:
	python manage.py loaddata data.json

tests:
	python manage.py test