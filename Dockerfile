FROM python:3.6-alpine3.7 as build
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY web.py ./
CMD [ "python", "./web.py"]
EXPOSE 80