web: gunicorn --chdir etestbackend etestbackend.wsgi:application --log-file - 
celeryd: celery --workdir etestbackend -A etestbackend.celery worker -E -B --loglevel=INFO
