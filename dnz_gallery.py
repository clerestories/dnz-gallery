import json, urllib2, urlparse
from bottle import route, run, request, redirect, static_file, template

'''
INSTRUCTIONS FOR USE
1) Open a new terminal:
e.g. on mac: CMD + Space to open spotlight. Then type 'terminal' and press enter.

2) Change into the right directory
e.g. cd web/dnz_gallery

OPTIONAL. Check what files and directories are in a directory by typing: ls 

3) Start the app
python dnz_gallery.py

4) Visit: http://localhost:8080/

'''

#static content
STATIC_PATH = 'static/'
API_KEY = 'XXXXXXXXXXXX' #Put your digitalNZ API key here: http://digitalnz.org/
PER_PAGE = 100 #Control the number of items to show per page

def get_data(search_text, page):
    url = 'http://api.digitalnz.org/v3/records.json?api_key=%s&text=%s&per_page=%s&page=%s&category=Images' % (
        API_KEY, search_text, PER_PAGE, page
        )
    data = urllib2.urlopen(url)
    response = json.loads(data.read())
    return response

@route('/search', method='POST')
def search():
    search_text = request.forms.get('search')
    url = '/search/%s/1' % search_text.replace(' ', '+')
    redirect(url)

@route('/search/:search_text/:page', method='GET')
def gallery(search_text, page):
    js = get_data(search_text, page)
    data = []
    for result in js['search']['results']:
        if not result['thumbnail_url']:
            continue
        data.append({
            'id':result['id'],
            'thumbnail_url':result['thumbnail_url'],
            'title':result['title'],
            })
    return template('views/gallery', search_text=search_text.replace('+', ' '), data=data, page=page)

@route('/', method='GET')
def home():
    return template('views/home')

@route('/static/<filepath:path>')
def server_static(filepath):
    import os
    print os.getcwd()
    return static_file(filepath, root=STATIC_PATH)

run(host='localhost', port=8080)