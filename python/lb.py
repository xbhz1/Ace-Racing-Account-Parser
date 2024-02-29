import os
import requests
import json
from concurrent.futures import ThreadPoolExecutor

def read_ids_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        ids = [line.strip() for line in f.readlines()]
    return ids

url = "http://comp-sync.webapp.163.com//comp-sync.webapp.163.com/h65login_role_list/free_convey?sdk_uid="
output_folder = "output"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def fetch_data(id):
    formatted_url = url + id
    response = requests.get(formatted_url)
    if response.status_code == 200:
        data = response.json()
        if not data["roles"]:
            print("没有数据，跳过：", id)
            return
        file_name = os.path.join(output_folder, data["roles"][0]["name"] + ".json")
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("数据已保存到文件：", file_name)
    else:
        print("请求失败，状态码：", response.status_code)

file_path = input("请输入txt文件的路径：")
ids = read_ids_from_file(file_path)

with ThreadPoolExecutor() as executor:
    executor.map(fetch_data, ids)
