import json
import urllib.request

url = 'http://jonghyup.com/tmp/data.json'
data = urllib.request.urlopen(url).read().decode('utf-8')
data = json.loads(data)
print(data)
print('이름순')
for d in sorted(data['items'], key=lambda x: x['name']):
    print('name:', d['name'],',','age:', d['age'],',','email:', d['email'])

print('나이순')
for d in sorted(data['items'], key=lambda x: x['age']):
    print('name:', d['name'],',','age:', d['age'],',','email:', d['email'])
