FROM python:3

EXPOSE 8000

ENV DIRWORK /home/sources

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        && rm -rf /var/lib/apt/lists/*


RUN mkdir $DIRWORK

WORKDIR $DIRWORK

COPY requirements.txt .

RUN pip install -r $DIRWORK/requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
