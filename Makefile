all:
	python manage.py makemigrations
	python manage.py migrate
	python loaddata data.json
	black .
	isort .


code-format:
	black .
	isort .

migrate:
	python manage.py makemigrations
	python manage.py migrate

loaddata:
	python loaddata data.json