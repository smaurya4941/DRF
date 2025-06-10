import requests
import json
URL="http://127.0.0.1:8000/studentapi/"


#function to get data(Read)

def get_data(id=None):
    params = {}
    if id is not None:
        params['id'] = id
    response = requests.get(url=URL, params=params)
    data = response.json()
    print("JSON Data:", data)

    
# get_data(1) #get data for id 1
# get_data() #get all data
        




#function to post data(Create)
def post_data():
    data={
        'name':'Prince',
        'roll':120,
        'city':'Azamgarh',
    }
    try:
        # data = r.json()
        r=requests.post(url=URL,json=data) #post request
        print("Status Code:", r.status_code)
        print("JSON Data:", data)
    except requests.exceptions.JSONDecodeError:
        print("❌ Server response is not JSON.")
# post_data()
        
#function to update data(Update)
def update_Data():
    data={
        'id':2,
        'name':'Mithilesh',
        'roll':98,
        'city':'Chauri CHaura',
    }
    try:
        # data = r.json()
        r=requests.put(url=URL,json=data) #post request
        print("Status Code:", r.status_code)
        print("JSON Data:", data)
    except requests.exceptions.JSONDecodeError:
        print("❌ Server response is not JSON.")
update_Data()




#function to update data(Update)
def delete_Data():
    data={
        'id':3,
    }
    try:
        r=requests.delete(url=URL,json=data) #post request
        print("Status Code:", r.status_code)
        print("JSON Data:", data)
    except requests.exceptions.JSONDecodeError:
        print("❌ Server response is not JSON.")
# delete_Data()