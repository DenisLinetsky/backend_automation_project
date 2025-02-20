import requests

def send_config(config, worker_endpoint):
    response = requests.post(worker_endpoint, json=config)
    if response.status_code == 200:
        print("Config sent successfully")
    else:
        print("Failed to send config")

if __name__ == '__main__':
    config = {
        "daily_limit": "250 GB",
        "accepted_data_formats": ["csv", "json"]
    }
    worker_endpoint = 'http://worker:5001/config'
    send_config(config, worker_endpoint)
