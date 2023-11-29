import requests
import threading

# Replace 'YOUR_API_ENDPOINT' and 'YOUR_API_TOKEN' with the actual API endpoint and token
API_ENDPOINT = 'http://localhost:3000/api/scenario/320/0/get_resources/'
API_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDEyNTQ3MTAsImlhdCI6MTcwMTI0NzUxMCwic2NvcGUiOiJhY2Nlc3NfdG9rZW4iLCJkYXRhIjp7InVzZXJfaWQiOjEsInVzZXJfdHlwZSI6MCwidXNlcm5hbWUiOiJzdUBnbWFpbC5jb20iLCJ1c2VyX3R5cGVfdGV4dCI6IkFkbWluIiwibWVudSI6W3sidGl0bGUiOiJTeXN0ZW0iLCJjaGlsZHJlbiI6W3sidGl0bGUiOiJVc2VycyIsInVybCI6Ii91c2VycyIsImljb24iOiJ1c2VyIiwia2V5IjoiMC0wLTAifSx7InRpdGxlIjoiSW5zdHJ1Y3RvciIsInVybCI6Ii90cmFpbmVycyIsImljb24iOiJ0cmFpbmVycyIsImtleSI6IjAtMC0xIn0seyJ0aXRsZSI6IlN0dWRlbnRzIiwidXJsIjoiL3N0dWRlbnRzIiwiaWNvbiI6InN0dWRlbnRzIiwia2V5IjoiMC0wLTIifSx7InRpdGxlIjoiUGVybWlzc2lvbnMiLCJ1cmwiOiIvcGVybWlzc2lvbnMiLCJpY29uIjoicGVybWlzc2lvbnMiLCJrZXkiOiIwLTAtMyJ9LHsidGl0bGUiOiJBY2NvdW50IFNldHRpbmdzIiwidXJsIjoiL2FjY291bnRfc2V0dGluZ3MiLCJpY29uIjoiZWZmZWN0Iiwia2V5IjoiMC0wLTQifV0sImljb24iOiJzeXN0ZW0iLCJrZXkiOiIwLTAifSx7InRpdGxlIjoiRXF1aXBtZW50cyIsImNoaWxkcmVuIjpbeyJ0aXRsZSI6IkRldmljZSBNYW51ZmFjdHVyZXIiLCJ1cmwiOiIvZGV2aWNlX21hbnVmYWN0dXJlciIsImljb24iOiJkZXZpY2VNZW51ZmFjdHVyZXIiLCJrZXkiOiIwLTEtMCJ9LHsidGl0bGUiOiJBY2Nlc3NvcmllcyIsImNoaWxkcmVuIjpbeyJ0aXRsZSI6IlBvd2VyIFNvdXJjZSIsInVybCI6Ii9wb3dlcl9zb3VyY2UiLCJpY29uIjoicG93ZXJTb3VyY2UiLCJrZXkiOiIwLTEtMS0wIn0seyJ0aXRsZSI6IkFudGVubmFzIiwidXJsIjoiL2FudGVubmFzIiwiaWNvbiI6ImFudGVubmFzIiwia2V5IjoiMC0xLTEtMSJ9XSwiaWNvbiI6ImVxdWlwQWNjIiwia2V5IjoiMC0xLTEifSx7InRpdGxlIjoiV2lyZWxlc3MiLCJjaGlsZHJlbiI6W3sidGl0bGUiOiJXaXJlbGVzcyBFcXVpcG1lbnRzIiwidXJsIjoiL3dsX2NvbW1fZXF1aXBfb3V0bGluZXMiLCJpY29uIjoid2xPdXRsaW5lIiwia2V5IjoiMC0xLTItMCJ9LHsidGl0bGUiOiJFcXVpcG1lbnRzIExpc3QiLCJ1cmwiOiIvd2xfZXF1aXBtZW50cyIsImljb24iOiJlcXVpcG1lbnRzIiwia2V5IjoiZXF1aXBtZW50cyJ9LHsidGl0bGUiOiJBZGQgRXF1aXBtZW50IiwidXJsIjoiL3dsX2VxdWlwbWVudHMvYWRkIiwiaWNvbiI6ImFkZEVxdWlwbWVudCIsImtleSI6IjAtMS0yLTEifV0sImljb24iOiJtYXAiLCJrZXkiOiIwLTEtMiJ9LHsidGl0bGUiOiJXaXJlZCIsImNoaWxkcmVuIjpbeyJ0aXRsZSI6IlRvb2xzIiwidXJsIjoiL3dpcmVfdG9vbHMiLCJpY29uIjoid3JkX21vZGVsIiwia2V5IjoiMC0xLTMtMCJ9LHsidGl0bGUiOiJCcmFuZCIsInVybCI6Ii93aXJlX2JyYW5kIiwiaWNvbiI6IndyZF9tb2RlbCIsImtleSI6IjAtMS0zLTEifSx7InRpdGxlIjoiTW9kZWwiLCJ1cmwiOiIvd2lyZV9tb2RlbCIsImljb24iOiJ3cmRfbW9kZWwiLCJrZXkiOiIwLTEtMy0yIn0seyJ0aXRsZSI6IkVxdWlwbWVudHMgTGlzdCIsInVybCI6Ii93aXJlX2NvbW1fZXF1aXBtZW50cyIsImljb24iOiJ3cmRfZXF1aXBtZW50cyIsImtleSI6IjAtMS0zLTMifSx7InRpdGxlIjoiQWRkIEVxdWlwbWVudCIsInVybCI6Ii93aXJlX2NvbW1fZXF1aXBtZW50cy9hZGQiLCJpY29uIjoiYWRkRXF1aXBtZW50Iiwia2V5IjoiMC0xLTMtNCJ9XSwiaWNvbiI6Im1hcCIsImtleSI6IjAtMS0zIn1dLCJpY29uIjoibWFwIiwia2V5IjoiMC0xIn0seyJ0aXRsZSI6IkVmZmVjdHMiLCJjaGlsZHJlbiI6W3sidGl0bGUiOiJOYXR1cmFsIEVmZmVjdCIsInVybCI6Ii9zZXR0aW5ncyIsImljb24iOiJhcnRpZmljaWFsIiwia2V5IjoiMC0yLTAifSx7InRpdGxlIjoiRGV2aWNlIFNldHRpbmdzIiwidXJsIjoiL2hmX3JhZGlvIiwiaWNvbiI6ImRldmljZSIsImtleSI6IjAtMi0xIn1dLCJpY29uIjoiZWZmZWN0Iiwia2V5IjoiMC0yIn0seyJ0aXRsZSI6IlRyYWluaW5nIiwiY2hpbGRyZW4iOlt7InRpdGxlIjoiQ291cnNlIExpc3QiLCJ1cmwiOiIvY291cnNlcyIsImljb24iOiJjb3Vyc2UiLCJrZXkiOiIwLTMtMCJ9LHsidGl0bGUiOiJBY3RpdmUgQ291cnNlcyIsInVybCI6Ii9hY3RpdmVfY291cnNlcyIsImljb24iOiJhY3RpdmVDb3Vyc2UiLCJrZXkiOiIwLTMtMSJ9LHsidGl0bGUiOiJTY2VuYXJpb3MiLCJ1cmwiOiIvc2NlbmFyaW9zIiwiaWNvbiI6ImFjdGl2ZUNvdXJzZSIsImtleSI6IjAtMy0yIn0seyJ0aXRsZSI6IlRyYWluaW5nIiwidXJsIjoiL3RyYWluaW5nIiwiaWNvbiI6ImluZGl2aWR1YWwiLCJrZXkiOiIwLTMtMyJ9LHsidGl0bGUiOiJEZXZpY2UgVXNlcyIsInVybCI6Ii9kZXZpY2VfdXNlcyIsImljb24iOiJpbmRpdmlkdWFsIiwia2V5IjoiMC0zLTQifSx7InRpdGxlIjoiQ29tcGFyaXNpb24gUmVwb3J0IiwidXJsIjoiL2NvbXBhcmlzaW9uX3JlcG9ydCIsImljb24iOiJpbmRpdmlkdWFsIiwia2V5IjoiMC0zLTUifV0sImljb24iOiJ0cmFpbmluZyIsImtleSI6IjAtMyJ9XX19.hR8NhtmLl0TEWBO09wHwqw77OwngDcIu15JlAxSbuug'

# Number of concurrent requests
NUM_REQUESTS = 10

# Barrier token to synchronize threads
barrier = threading.Barrier(NUM_REQUESTS)

def api_request(index):
    print(f"Thread {index} started")
    
    # Replace 'Authorization' with the actual header key required for token authentication
    headers = {'Authorization': f'Bearer {API_TOKEN}'}

    # Make the API request
    response = requests.get(API_ENDPOINT, headers=headers)
    print(response)
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
print(f'Total Success: {success}')
print(f'Total Failed: {failed}')
