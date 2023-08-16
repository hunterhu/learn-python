#!/bin/python3

import requests

def search_word(word:str, source:str): 
    print(f"{word}: {source.count(word)}")
    
url = "https://www.google.com"
response = requests.get(url)
if response.status_code == 200:
    page_contents = response.text
    search_word("Google", page_contents)
else:
    print(f"Failed to retrieve the page, Status Code: {response.status_code}")
