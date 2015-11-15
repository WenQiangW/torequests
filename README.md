# trequests
####Using tomorrow to make requests async
https://github.com/madisonmay/Tomorrow

Obviously, use it like :
```python
from trequests import tPool as Pool

requests = Pool(30)
...
```
then use requests.get/post/put/head/delete/ as usual.
so, this does not support Session...

curio sames awosome and difficult，multiprocessing.dummy and pool.map is non-3rd-library but I don't like it even using it much time，requests said never support async（such like asyncio）， aiohttp not easy like requests, gevent hates Windows, twisted hard to study and no good for py3, grab seems good, scrapy seems to abandon py3, god ,I have try so much and deserve so many failures.........


##一句话，就是给requests简单异步包装一下
####用法：
```python
from trequests import Pool
requests = Pool(30)
```
###然后requests正常用就行了，支持Session什么的，就只是简单的requests.get加几个参数，可以命名成trequest，和原生requests分开混着用，原生的requests就用multiprocessing.dummy吧。。。（后来把tomorrow包装的叫tPool，multiprocessing.dummy包装的叫mPool，后者只是多线程处理下urls。。。)

#Example：

## new usage of requests
```python
#!python3
from trequests import tPool as Pool
import time
aa=time.time()
requests = Pool(50)
ss=[requests.get('http://p.3.cn/prices/mgets?skuIds=J_1273600')]*500
print([len(i.text) for i in ss])
print(time.time()-aa,'s')


```
>[51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51]

>0.16710209846496582 s

## Session:
```python
#!python3
from trequests import Pool
import time
import requests
aa = time.time()
s = requests.Session()
requests = Pool(50, session=s)
ss = [requests.get('http://p.3.cn/prices/mgets?skuIds=J_1273600')] * 5000
ss = [i.text for i in ss]
print(ss[-10:])
print(time.time() - aa, 's')
```
>['[{"id":"J_1273600","p":"16999.00","m":"16999.00"}]\n', '[{"id":"J_1273600","p":"16999.00","m":"16999.00"}]\n', '[{"id":"J_1273600","p":"16999.00","m":"16999.00"}]\n', '[{"id":"J_1273600","p":"16999.00","m":"16999.00"}]\n', '[{"id":"J_1273600","p":"16999.00","m":"16999.00"}]\n', '[{"id":"J_1273600","p":"16999.00","m":"16999.00"}]\n', '[{"id":"J_1273600","p":"16999.00","m":"16999.00"}]\n', '[{"id":"J_1273600","p":"16999.00","m":"16999.00"}]\n', '[{"id":"J_1273600","p":"16999.00","m":"16999.00"}]\n', '[{"id":"J_1273600","p":"16999.00","m":"16999.00"}]\n']
0.18413066864013672 s

## multi-threads:
```python
from trequests import mPool as Pool
import time
aa = time.time()
requests = Pool(50)
ss=requests.get(['http://p.3.cn/prices/mgets?skuIds=J_1273600']*100)
print([len(i.text) for i in ss])
print(time.time() - aa, 's')
```
>[51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51, 51]
1.218897819519043 s
