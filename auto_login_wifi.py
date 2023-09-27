import requests
import subprocess
import time

# 定义常量
BASE_URL = "http://192.168.2.253:8080" # 这里写网关地址
CODE = "xxx" # 这里写卡号用户名
PWD = "xxx" # 这里填写密码
target_ssid = 'TZTSG'

def check_wifi_connection(target_ssid):
    while True:
        result = subprocess.run(['networksetup', '-getairportnetwork', 'en0'], text=True, capture_output=True)
        if target_ssid in result.stdout:
            print(f'Connected to {target_ssid}')
            connect_wifi()
            break
        else:
            print('Not connected')
        time.sleep(5)  # adjust polling interval as necessary

def connect_wifi():
  # 设置请求参数
  url = BASE_URL + "/api/tztsg/wifi-auth"
  params = {
      "code": CODE,
      "pwd": PWD,
  }

  # 设置防真请求信息
  headers = {
      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
      "Referer": BASE_URL + "/wifiauth",
      "Dnt": "1",
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "gzip, deflate",
      "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
      "Connection": "keep-alive",
      "Cookie": "_ga=GA1.1.1192614528.1695689014; username="+CODE+"; password="+PWD+"; rememberMe=true; _ga_GDWQY4XZV0=GS1.1.1695689014.1.1.1695689447.0.0.0",
  }

  # 发送请求
  response = requests.get(url, params=params, headers=headers)
  print(response)

  # 处理响应
  if response.status_code == 200:
      print("登录成功")
  else:
      print("登录失败")

def main():
    check_wifi_connection(target_ssid)
    input("按任意键退出...")

if __name__ == "__main__":
    main()

# 使用如下脚本导出exe
# pip install pyinstaller
# pyinstaller -F login_wifi.py
