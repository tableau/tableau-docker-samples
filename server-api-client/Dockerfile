FROM python:3.7.0

RUN pip install tableauserverclient==0.7
ADD https://raw.githubusercontent.com/tableau/rest-api-samples/master/python/version.py version.py
ADD ./publish_workbook.py publish_workbook.py
ADD ./publish_datasource.py publish_datasource.py

ENTRYPOINT ["python"]