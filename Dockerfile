FROM python
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -r requirements.txt

COPY . .

# для деплоя
#FROM python
#ENV PYTHONUNBUFFERED=1
#COPY requirements.txt ./
#RUN pip install -r requirements.txt
#RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
#
#COPY . .
#
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8003"]
