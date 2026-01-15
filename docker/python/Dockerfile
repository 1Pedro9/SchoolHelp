FROM python:3.13

WORKDIR /var/www/html

COPY ./app .

RUN pip install uv
RUN uv sync

EXPOSE 8080
CMD ["uv", "run", "app.py", "0.0.0.0:8080"]
