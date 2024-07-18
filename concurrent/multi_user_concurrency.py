import json
import threading

import requests

#change to your base url or hosting address of your server
BASE_URL = 'http://localhost:9000/' 
# create a users array with username and password
USER_ARRAY = [
    {"username": "atec-1@gmail.com","password": "1234"},
    {"username": "atec-2@gmail.com","password": "1234"},
    {"username": "atec-3@gmail.com","password": "1234"},
    {"username": "atec-4@gmail.com","password": "1234"},
    {"username": "atec-5@gmail.com","password": "1234"},
    {"username": "atec-6@gmail.com","password": "1234"},
    {"username": "atec-7@gmail.com","password": "1234"},
    {"username": "atec-8@gmail.com","password": "1234"},
    {"username": "atec-9@gmail.com","password": "1234"},
    {"username": "atec-10@gmail.com","password": "1234"},
    {"username": "atec-11@gmail.com","password": "1234"},
    {"username": "atec-12@gmail.com","password": "1234"},
    {"username": "atec-13@gmail.com","password": "1234"},
    {"username": "atec-14@gmail.com","password": "1234"},
    {"username": "atec-15@gmail.com","password": "1234"},
    {"username": "atec-16@gmail.com","password": "1234"},
    {"username": "atec-17@gmail.com","password": "1234"},
    {"username": "atec-18@gmail.com","password": "1234"},
    {"username": "atec-19@gmail.com","password": "1234"},
    {"username": "atec-20@gmail.com","password": "1234"},
    {"username": "atec-21@gmail.com","password": "1234"},
    {"username": "atec-22@gmail.com","password": "1234"},
    {"username": "atec-23@gmail.com","password": "1234"},
    {"username": "atec-24@gmail.com","password": "1234"},
    {"username": "atec-25@gmail.com","password": "1234"},
]


NUM_REQUESTS = len(USER_ARRAY)
# Barrier token to synchronize threads
barrier = threading.Barrier(NUM_REQUESTS)
ACCESSTOKEN_ENDPOINT = BASE_URL+'o/accesstoken/'
LOGIN_ENDPOINT = BASE_URL+'o/login/'
# this api is the most operation and memory intensive api endpoint. If you want to test another api point just change the prefix url
FINAL_ENDPOINT = BASE_URL+'api/scenario/197/0/load_scenario_configs/' 

def accesstoken_request(API_ENDPOINT):
    headers = {
        'Content-Type': 'application/json',
    }

    data = {
        
        "client_id": "09d25e094faa6ca2556c818166b7a9563a33f7099f6f0f4caa6cf63b88e8d3e7",
        "client_secret": "09d25e094faa6ca2556c818177b7a9563a33f7099f6f0f4caa6cf63b88e8d3e7"
    }
    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code ==200:
        print(f"Accesstoken status code: {response.status_code}")
        response_data = response.json()
        return response_data['token']
    else:
        print(f"Accesstoken status code: {response.status_code}")
        return False
        

def user_login_request(API_ENDPOINT, USER):
    access_token = accesstoken_request(ACCESSTOKEN_ENDPOINT)
    if access_token:
        headers = {
            'Content-Type': 'application/json',
            'accesstoken': access_token,
        }

        data = USER
        response = requests.post(LOGIN_ENDPOINT, headers=headers, data=json.dumps(data))

        if response.status_code ==200:
            print(f"Login status code: {response.status_code}")
            response_data = response.json()
            return response_data['access_token']
        else:
            print(f"Login status code: {response.status_code}")
            return False
        
    else:
        return False
    
def api_request(index, API_ENDPOINT, user):
    jwt_token = user_login_request(LOGIN_ENDPOINT, user)
    print(user['username'])
    if jwt_token:
        print(f"Thread {index} started")
        headers = {'Authorization': f'Bearer {jwt_token}'}
        response = requests.get(API_ENDPOINT, headers=headers)
        # Synchronize threads at the barrier
        barrier.wait()
        
        success = 0
        failed = 0
        if response.status_code ==200:
            print(f"Thread: {index}. User: {user['username']}. Completed with status code: {response.status_code}")
            success = success + 1
        else:
            print(f"Thread: {index}.User: {user['username']}. Failed status code: {response.status_code}")
            failed =  failed + 1  
    else:
        print(f"Thread: {index}. JWT Error!")
        return False



def concurrent_calls(USER_ARRAY):
    count = 1
    threads = []
    for user in USER_ARRAY:
        thread = threading.Thread(target=api_request, args=(count, FINAL_ENDPOINT, user))
        thread.start()
        threads.append(thread)
        count +=1
        
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
        
    print("All concurrent calls have completed.")

concurrent_calls(USER_ARRAY)