import requests
import time

import random

def vreq(url:str):
    proxy = {
        "http": "http://127.0.0.1:9876",
        "https": "http://127.0.0.1:9876"
    }
    ua = {
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
    }
    headers ={
        "User-Agent": random.choice(ua),
    }
    try:
        response = requests.get(url,proxies=proxy,headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.content
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def to_timestamp(date_str: str) -> int:
    from datetime import datetime
    try:
        # Parse the date string into a datetime object
        dt =  time.strptime(date_str,"%a, %d %b %Y %H:%M:%S -0000")
        # Convert the datetime object to a timestamp
        return int(time.mktime(dt))
    except ValueError as e:
        print(f"Error parsing date string '{date_str}': {e}")
        return 0
