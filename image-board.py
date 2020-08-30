import webbrowser
import requests
from bs4 import BeautifulSoup

path_to_firefox = 'path'
board = 'board'
search_string = 'board'
api_url = 'api_url'
web_url = 'web_url'

catalog_api = '/'.join((api_url,board,'catalog.json'))

response = requests.get(catalog_api)

threads=[thread for page in response.json() for thread in page['threads']]


def correct_thread(thread,search_string):
    if 'sub' in thread.keys():
        return search_string in thread['sub']
    else:
        return False
    
threads = [thread for thread in threads if correct_thread(thread)]

thread_no = threads[0]['no']

thread_url = '/'.join((web_url,board,'thread',str(thread_no)))

webbrowser.register('firefox',
	None,
	webbrowser.BackgroundBrowser(path_to_firefox))

webbrowser.get('firefox').open(thread_url)
