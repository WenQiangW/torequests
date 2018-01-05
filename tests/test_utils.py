#! coding:utf-8
import time
from torequests.utils import *
import requests

### with capsys.disabled():

def test_curlparse_get():
    '''  test_dummy_utils '''
    cmd = '''curl 'http://httpbin.org/get?test1=1&test2=2' -H 'Pragma: no-cache' -H 'DNT: 1' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.8' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' -H 'Cache-Control: no-cache' -H 'Connection: keep-alive' --compressed'''
    args = curlparse(cmd)
    resp = requests.request(**args)
    rj = resp.json()
    assert rj['url'] == 'http://httpbin.org/get?test1=1&test2=2' and rj['args']['test1'] == '1', 'test fail: curlparse get'


def test_curlparse_post():
    '''  test_dummy_utils '''
    cmd = '''curl 'http://httpbin.org/post' -H 'Pragma: no-cache' -H 'Origin: null' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.8' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' -H 'Cache-Control: no-cache' -H 'Connection: keep-alive' -H 'DNT: 1' --data 'test1=%E6%B5%8B%E8%AF%95&test2=%E4%B8%AD%E6%96%87' --compressed'''
    args = curlparse(cmd)
    resp = requests.request(**args)
    rj = resp.json()
    assert rj['form']['test1'] == u'测试', 'test fail: curlparse post & urlencode'


def test_slice_by_size():
    assert list(slice_by_size(range(10), 6)) == [(0, 1, 2, 3, 4, 5), (6, 7, 8, 9)], 'test fail: slice_by_size'

def test_slice_into_pieces():
    assert list(slice_into_pieces(range(10),3))==[(0, 1, 2, 3), (4, 5, 6, 7), (8, 9)], 'test fail: slice_into_pieces'

def test_ttime_ptime():
    assert time.time() - ptime(ttime(tzone=0),tzone=0) < 2, 'fail: ttime / ptime'

def test_escape_unescape():
    assert escape('<>')=='&lt;&gt;' and unescape('&lt;&gt;')=='<>', 'fail: escape'

def test_counts():
    c = Counts()
    [c.x for i in range(10)]
    assert c.c == 11, 'fail: test_counts'

def test_unique():
    assert list(unique(list(range(4,0,-1))+list(range(5))))==[4, 3, 2, 1, 0]

def test_regex():
    reg = Regex()

    @reg.register_function('http.*cctv.*')
    def mock():
        pass

    reg.register('http.*HELLOWORLD', 'helloworld', flags=re.I)
    reg.register('http.*HELLOWORLD2', 'helloworld2', flags=re.I)

    assert (reg.search('http://cctv.com'))
    assert (reg.match('http://helloworld')==['helloworld'])
    assert (reg.match('non-http://helloworld')==[])
    assert (reg.search('non-http://helloworld')==['helloworld'])
    assert (len(reg.search('non-http://helloworld2'))==2)


def test_clean_request():
    from torequests.crawlers import CleanRequest
    request = ('''curl 'http://www.ip138.com/ips1388.asp?ip=123.125.114.144&action=2' -H 'Pragma: no-cache' -H 'DNT: 1' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.9' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' -H 'Cache-Control: no-cache' -H 'Referer: http://www.ip138.com/ips138.asp?ip=39.75.221.132&action=2' -H 'Cookie: ASPSESSIONIDSQRRSADB=MLHDPOPCAMBDGPFGBEEJKLAF' -H 'Connection: keep-alive' --compressed''')

    c = CleanRequest(request)
    assert (c.x == {'url': 'http://www.ip138.com/ips1388.asp?ip=123.125.114.144&action=2', 'method': 'get'})


def test_failure():
    from torequests.exceptions import FailureException
    assert bool(FailureException(BaseException()))==False