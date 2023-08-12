FROM python:3.9-slim
WORkDIR /app
RUN apt update && pip3 install django 
COPY . .
RUN python3 manage.py makemigrations && python3 manage.py migrate
EXPOSE 8080
CMD ["python3","manage.py","runserver","0.0.0.0:8080"] 


