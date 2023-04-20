FROM python:3.10

WORKDIR ./app

COPY requirements.txt .

COPY . .

RUN pip install -r requirements.txt

ENV PORT 8080

EXPOSE 8080

CMD sleep 5; python manage.py makemigrations ; python manage.py migrate ; python3 create_superuser.py;  python manage.py runserver 0.0.0.0:8080








#CMD python manage.py makemigrations ; python manage.py migrate ; python manage.py createsuperuser ; admin; vouka7@mail.ru; 12345qwert ; python manage.py runserver 0.0.0.0:8080
#CMD python3 create_superuser.py; python manage.py makemigrations ; python manage.py migrate ;  python manage.py runserver 0.0.0.0:8080
#CMD  python manage.py runserver 0.0.0.0:8080
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]

