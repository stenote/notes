FROM django:1.10

WORKDIR /usr/src/app
COPY . .

EXPOSE 80
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
