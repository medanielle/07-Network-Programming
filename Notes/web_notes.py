"""
>>> import requests
>>>link = "http://www.python-requets.org"
>>> r = request.get(link)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'request' is not defined
>>> r = requests.get(link)
>>> dir(r)
['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']
>>> print(type(r))
<class 'requests.models.Response'>


>>> r.url #URL of repsonse object
'https://2.python-requests.org/en/master/'
>>> r.status_code # status code
200 
>>> r.history # status code of history event
[<Response [301]>, <Response [302]>]
>>> r.headers # response headers with info about server, date, etc... 
{'Date': 'Wed, 18 Dec 2019 14:44:33 GMT', 'Content-Type': 'text/html', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Last-Modified': 'Sat, 23 Nov 2019 02:51:33 GMT', 'Vary': 'Accept-Encoding', 'X-Cname-TryFiles': 'True', 'X-Served': 'Nginx', 'X-Deity': 'web02', 'CF-Cache-Status': 'DYNAMIC', 'Expect-CT': 'max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"', 'Server': 'cloudflare', 'CF-RAY': '5471ea5bfb9258e9-DFW', 'Content-Encoding': 'gzip'}        
>>> r.headers['Content-Type'] # specific header information grab
'text/html'
>>> r.request.headers # request - related header (rather than response above) 
{'User-Agent': 'python-requests/2.22.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Cookie': '__cfduid=d9d725ac1610fba7a45bd8e1334c543fc1576680272'}
>>> r.encoding # response encoding
'ISO-8859-1'
>>> r.content[0:400] # 400 bytes of characters
b'\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n\n<html xmlns="http://www.w3.org/1999/xhtml" lang="en">\n  <head>\n    <meta http-equiv="X-UA-Compatible" content="IE=Edge" />\n    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n   
 <title>Requests: HTTP for Humans\xe2\x84\xa2 &#8212; Requests 2.22.0 documentation'
>>> r.text[0:400] # sub string that is 400 string characters from the response
'\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n\n<html xmlns="http://www.w3.org/1999/xhtml" lang="en">\n  <head>\n    <meta http-equiv="X-UA-Compatible" content="IE=Edge" />\n    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n    
<title>Requests: HTTP for Humansâ\x84¢ &#8212; Requests 2.22.0 documentation'



>>> link = "https://feeds.citibikenyc.com/stations/stations.json" 
>>> response = requests.get(link).json() 


>>> for i in range(10): # read 10 stationName from JSON response
...     print('Station: ', response['stationBeanList'][i]['stationName'])
... 
Station:  Grand Army Plaza & Central Park S
Station:  E 47 St & Park Ave
Station:  E 53 St & Lexington Ave
Station:  6 Ave & Canal St
Station:  Broadway & E 22 St
Station:  Water - Whitehall Plaza
Station:  W 52 St & 6 Ave
Station:  W 52 St & 11 Ave
Station:  Franklin St & W Broadway
Station:  St James Pl & Pearl St
"""
"""
FROM WEBSITE: ()

>>> r = requests.get('https://api.github.com/user', auth=('myemailid.mail.com', 'password'))
>>> r.status_code
200
>>> r.url
u'https://api.github.com/user'
>>> r.request
<PreparedRequest [GET]>
"""
"""
MY FAILED LOGIN ATTEMPT:
>>> r = requests.get('https://api.github.com/user', auth=('medanielle@gmail.com', 'dan1elle'))    
>>> r.status_code
401
>>> r.url
'https://api.github.com/user'
>>> r.request
<PreparedRequest [GET]>
>>> print(r) 
<Response [401]>
"""


""" EXAMPLE FROM GITHUB

>>> url = 'http://www.columbia.edu/~fdc/sample.html'
>>> response = requests.get(url)
>>> response.status_code
200
>>> response.text

    OMG ALL THE WORDS!!!

>>> response.request.headers
{'User-Agent': 'python-requests/2.22.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
>>> response.headers
{'Date': 'Wed, 18 Dec 2019 15:15:50 GMT', 'Server': 'Apache', 'Last-Modified': 'Wed, 11 Dec 2019 12:46:44 GMT', 'Accept-Ranges': 'bytes', 'Vary': 'Accept-Encoding,User-Agent', 'Content-Encoding': 'gzip', 'Content-Length': '10127', 'Keep-Alive': 'timeout=15, max=84', 'Connection': 'Keep-Alive', 'Content-Type': 'text/html', 'Set-Cookie': 'BIGipServer~CUIT~www.columbia.edu-80-pool=1764244352.20480.0000; expires=Wed, 18-Dec-2019 21:15:50 GMT; path=/; Httponly'}


>>> response.request
<PreparedRequest [GET]>
>>> response.request.url
'http://www.columbia.edu/~fdc/sample.html'
"""

def get_headers():
    #!/usr/bin/env python3

    import requests
    response = requests.get('http://github.com')
    try:
        for key,value in response.headers.items():
            print('%s: %s' % (key, value))
    except Exception as error:
        print('%s' % (error))

def check_SQL():
    import requests

    url = "http://127.0.0.1/SQL/sqli-labs-master/Less-1/index.php?id="
    initial = "'"
    print("Testing" + url)
    first = requests.post(url+initial)

    if "mysql" in first.text.lower(): 
        print("Injectable MySQL detected")
    elif "native client" in first.text.lower():
        print("Injectable MSSQL detected")
    elif "syntax error" in first.text.lower():
        print("Injectable PostGRES detected")
    elif "ORA" in first.text.lower():
        print("Injectable Oracle detected")
    else:
        print("Not Injectable J J")

check_SQL()
