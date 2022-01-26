import requests
import threading

def req(a):
    print("开始请求")
    res = requests.get("http://127.0.0.1:5000/").text
    print(res)


for i in range(100):
    t = threading.Thread(target=req, args=(i,))  # 注意传入的参数一定是一个元组!
    t.start()