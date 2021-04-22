FROM python:3.8-alpine

RUN pip install tableauserverclient==0.15
ADD https://raw.githubusercontent.com/tableau/rest-api-samples/master/python/version.py version.py
ADD ./publish_workbook.py publish_workbook.py
ADD ./publish_datasource.py publish_datasource.py

ENTRYPOINT ["python"]
