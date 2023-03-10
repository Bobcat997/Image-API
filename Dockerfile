FROM python:3.11.2-slim

WORKDIR /usr/src/app

COPY . ./
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]