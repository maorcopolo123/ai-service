FROM python:3.8-slim
WORKDIR /app
RUN pip install -r requirements.txt -i https://pypi.douban.com/simple/

ADD . /app

EXPOSE 6666
CMD ["python","app.py"]
