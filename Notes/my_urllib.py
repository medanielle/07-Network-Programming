
"""
>>> import urllib
>>> import requests
>>> link = 'http://www.google.com'
>>> linkRequest = urllib.request.urlopen(link) #open link
>>> print(type(linkRequest))
<class 'http.client.HTTPResponse'>
>>> linkResponse = urllib.request.urlopen(link).read()
>>> #open link and read the content
... 
>>> print(type(linkResponse))
<class 'bytes'>

"""


"""
>>> linkRequest.getcode() # can also use it as linkRequest.code or linkRequest.status
200 
>>> linkRequest.code() 
Traceback (most recent call last):     
  File "<stdin>", line 1, in <module>  
TypeError: 'int' object is not callable
>>> linkRequest.code  
200 
>>> linkRequest.geturl() # can also use linkRequest.url
'http://www.google.com'
>>> linkRequest._method
'GET'
>>> linkRequest.getheaders()
[('Date', 'Wed, 18 Dec 2019 16:14:09 GMT'), ('Expires', '-1'), ('Cache-Control', 'private, max-age=0'), ('Content-Type', 'text/html; charset=ISO-8859-1'), ('P3P', 'CP="This is not a P3P policy! See g.co/p3phelp for more info."'), ('Server', 'gws'), ('X-XSS-Protection', '0'), ('X-Frame-Options', 'SAMEORIGIN'), ('Set-Cookie', '1P_JAR=2019-12-18-16; expires=Fri, 17-Jan-2020 16:14:09 GMT; path=/; domain=.google.com'), ('Set-Cookie', 'NID=193=gUpbxoKylUciFbJkKOfwy2vVK_Nis143oxqhnsB_cSj51kzs5-6Imdcjk_Xv-fiABaAA5atfriDlYSX2rQeMLjyVu1ldsFEMTE_z5zT85_dmFAcucMpozM-EA1hArPqMpEk50FoMjPFOdLFgXwHulPtQHzxmRwf5yriYgppR5sU; expires=Thu, 18-Jun-2020 16:14:09 GMT; path=/; domain=.google.com; HttpOnly'), ('Accept-Ranges', 'none'), ('Vary', 'Accept-Encoding'), ('Connection', 'close')]
>>> linkRequest.getheader("Content-Type")
'text/html; charset=ISO-8859-1'
>>> linkRequest.info()['Content-Type']
'text/html; charset=ISO-8859-1'
"""
"""
CHECK AGAIN!!!:::
>>> import urllib.request as request 
>>> import urllib.error as error
>>> try: # attempt an error case
...     request.urlopen('http://www.python.ogr') #wrong url
... except error.URLError as e: 
...     print("Error Occurrrd", e.reason)
... 
<http.client.HTTPResponse object at 0x0000023163E43E20>
>>> 

"""

"""
>>> import urllib.parse as urlparse
>>> print(dir(urlparse)) # list feastures from urllib.parse
['DefragResult', 'DefragResultBytes', 'MAX_CACHE_SIZE', 'ParseResult', 'ParseResultBytes', 'Quoter', 'ResultBase', 'SplitResult', 'SplitResultBytes', '_ALWAYS_SAFE', '_ALWAYS_SAFE_BYTES', '_DefragResultBase', '_NetlocResultMixinBase', '_NetlocResultMixinBytes', '_NetlocResultMixinStr', '_ParseResultBase', '_ResultMixinBytes', '_ResultMixinStr', '_SplitResultBase', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_asciire', '_checknetloc', '_coerce_args', '_decode_args', '_encode_result', '_hexdig', '_hextobyte', '_hostprog', '_implicit_encoding', '_implicit_errors', '_noop', '_parse_cache', '_portprog', '_safe_quoters', '_splitattr', '_splithost', '_splitnetloc', '_splitnport', '_splitparams', '_splitpasswd', '_splitport', '_splitquery', '_splittag', '_splittype', '_splituser', '_splitvalue', '_to_bytes', '_typeprog', 'clear_cache', 'collections', 'namedtuple', 'non_hierarchical', 'parse_qs', 'parse_qsl', 'quote', 'quote_from_bytes', 'quote_plus', 're', 'scheme_chars', 'splitattr', 'splithost', 'splitnport', 'splitpasswd', 'splitport', 'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'sys', 'to_bytes', 'unquote', 'unquote_plus', 'unquote_to_bytes', 'unwrap', 'urldefrag', 'urlencode', 'urljoin', 'urlparse', 'urlsplit', 'urlunparse', 'urlunsplit', 'uses_fragment', 'uses_netloc', 'uses_params', 'uses_query', 'uses_relative', 'warnings']
>>>
"""

"""
>>> amazonUrl = 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks-intl-ship&field-keywords=Pearson+Books'  
>>> print(urlparse.urlsplit(amazonUrl).scheme)
https
>>> print(urlparse.urlsplit(amazonUrl))       
SplitResult(scheme='https', netloc='www.amazon.com', path='/s/ref=nb_sb_noss', query='url=search-alias%3Dstripbooks-intl-ship&field-keywords=Pearson+Books', fragment='')
>>>

"""
"""
>>> data = {'param1': 'value1', 'param2': 'value2'}
>>> urlparse.urlencode(data)
'param1=value1&param2=value2'
>>> urlparse.parse_qs(urlparse.urlencode(data))
{'param1': ['value1'], 'param2': ['value2']}
>>> urlparse.urlencode(data).encode('utf-8')
b'param1=value1&param2=value2'
"""

"""
>>> urlparse.urljoin('http://localhost:8080/~cache/', 'data file') 
'http://localhost:8080/~cache/data file'
"""

"""
BROKE!!!!!!
>>> import urllib.robotparser as robot
>>> par = robot.RobotFileParser()
>>> par.set_url('https://www.samsclub.com/robot.txt')
>>> par.read()
>>> print(par)
>>> par.can_fetch('*', 'https:/www.samsclub.com/friend')
True
>>> par.can_fetch('*', 'https://www.samsclub.com/friend') 
False
"""

def my_robot():
    import urllib.robotparser as robot
    par = robot.RobotFileParser()
    par.set_url('https://www.samsclub.com/robots.txt')
    par.read() # reading the URL content
    print('~'*20)
    print(par)
    print('~'*20)
    print(par.can_fetch('*', 'https:/www.samsclub.com/friend'))
    print(par.can_fetch('*', 'https://www.samsclub.com/friend'))

# my_robot()

def my_error():
    import urllib.request as request
    import urllib.error as error
    
    try:
        request.urlopen('https://www.python.org/f')
        print('Success')
    except error.URLError as e:
        print('Error Occured: ', e.reason)

my_error()
