import json
import requests

url='https://apihouse.herokuapp.com/credsapi/?search=django_blog'

headers={
    "Authorization":"Token a1c6d310cfe6ef987e66394bc86c63066dd22160"
}

r=requests.get(url=url,headers=headers)

json_data=r.json()
for data in json_data:
    secret_key=data['secret_key']
    host=data['database_host']
    user=data['database_user']
    password=data['database_password']
    name=data['database_name']
