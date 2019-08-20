import requests

def count_word(url):
    r  = requests.get(url)
    return len(r.content.strip().split())
