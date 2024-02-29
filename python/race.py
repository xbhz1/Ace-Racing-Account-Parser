import requests
import json
import os

url = "http://comp-sync.webapp.163.com//comp-sync.webapp.163.com/h65login_role_list/free_convey?sdk_uid="
id = input("请输入ID，id请自行获取：")
formatted_url = url + id
response = requests.get(formatted_url)

if response.status_code == 200:
    data = response.json()
    if not data["roles"]:
        print("请检查你输入的id是否正确，检测到输入异常正在退出")
        exit()
    file_name = data["roles"][0]["name"] + ".json"
    os.makedirs("data", exist_ok=True)
    with open("data" + file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("数据已保存到文件：", "data/" + file_name)
else:
    print("请求失败，状态码：", response.status_code)
