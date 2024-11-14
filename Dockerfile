FROM python:3.10

WORKDIR /code

COPY ./requirments.txt /code/requirments.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirments.txt

COPY ./app /code/app

CMD ["fastapi", "run", "app/main.py", "--port", "80"]