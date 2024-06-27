FROM python:3.9

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENV HOST_SERVICE=0.0.0.0
ENV PORT_SERVICE=8000
ENV SECRET_KEY $SECRET_KEY
ENV DEBUG=False

ENV DB_USER $DB_USER
ENV DB_PASSWORD $DB_PASSWORD
ENV DB_HOST $DB_HOST
ENV DB_PORT $DB_PORT
ENV DB_NAME $DB_NAME

COPY ./ /service
RUN rm /service/Dockerfile

WORKDIR /service/app
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--workers=10", "--port", "80", "--host", "0.0.0.0"]
