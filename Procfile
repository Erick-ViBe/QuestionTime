web: gunicorn QuestionTime.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate
web: python manage.py runserver 0.0.0.0:1234
