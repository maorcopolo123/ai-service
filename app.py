from flask import Flask
import time
import datetime
import logging

app = Flask(__name__)


@app.route("/")
def hello_world():
    a = datetime.datetime.now()
    print("开始工作{}".format(a))
    time.sleep(5)
    now = datetime.datetime.now()
    return "<p>现在时间:{}</p>".format(now)


def main():
    app.run()


if __name__ == '__main__':
    main()
