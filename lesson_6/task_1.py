import requests

data_list = []
url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
req = (el for el in requests.get(url).text.strip().split('\n'))
for el in req:
    el = el.split(' ')
    remote_addr = el[0]
    request_type = el[5][1:]
    requested_resource = el[6]
    data_list.append((remote_addr, request_type, requested_resource))

print(data_list)
