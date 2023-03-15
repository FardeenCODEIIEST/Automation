import webbrowser  #for accessing web-browser module of python
import sys  #for retrieving arguments from terminal

# MacOS
# chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

# Linux
# chrome_path = '/usr/bin/google-chrome %s'

url = 'https://www.google.com/search?q='

valid_sites = [
    'github.com', 'stackoverflow.com', 'stackexchange.com', 'medium.com',
    'leetcode.com', 'cp-algorithms.com', 'geeksforgeeks.org', 'reddit.com',
    'developer.mozilla.org'
]


def filter():
    ans = '('
    for count, sites in enumerate(valid_sites):
        ans += 'site:' + sites
        if (count == len(valid_sites) - 1):
            ans += ')'
        else:
            ans += 'OR'
    return ans


def query_create():
    query = sys.argv[1:]
    return ' '.join(query)


def create_url():
    if (len(sys.argv[1:]) == 0):
        print('Error! Enter a non-empty search query')
    else:
        final_url = url + query_create() + filter()
        webbrowser.get(chrome_path).open(final_url)


create_url()
