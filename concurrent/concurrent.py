import threading

import requests

API_ENDPOINT = 'http://192.168.100.10/api/scenario/320/0/get_resources/'

API_TOKEN = ''

# Number of concurrent requests
NUM_REQUESTS = 1000
# Barrier token to synchronize threads
barrier = threading.Barrier(NUM_REQUESTS)

    
def api_request(index):
    print(f"Thread {index} started")
    headers = {'Authorization': f'Bearer {API_TOKEN}'}
    response = requests.get(API_ENDPOINT, headers=headers)
    # Synchronize threads at the barrier
    barrier.wait()
    
    success = 0
    failed = 0
    if response.status_code ==200:
        print(f"Thread {index} completed with status code: {response.status_code}")
        success = success + 1
    else:
        print(f"Thread {index} failed status code: {response.status_code}")
        failed =  failed + 1  
        
# Create and start threads
threads = []
for i in range(NUM_REQUESTS):
    thread = threading.Thread(target=api_request, args=(i,))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads have completed.")

