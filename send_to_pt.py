import requests, json

API_KEY = '-YOUR API KEY-'

def classify(value):
  url = 'https://www.passivetotal.org/api/v1/classification'
  params = {'api_key': API_KEY, 'query': value, 'classification': 'targeted'}
  response = requests.get(url, params=params)
  json_response = json.loads(response.content)
  return json_response['success']

def tag(value):
  url = 'https://www.passivetotal.org/api/v1/user/tag/add'
  params = {'api_key': API_KEY, 'query': value, 'tag': 'hackingteam'}
  response = requests.post(url, data=params)
  json_response = json.loads(response.content)
  return json_response['success']
  
for item in [ x.strip() for x in open('hackingteam_vps.txt', 'r').readlines() ]:
  print "Classifying", item, classify(item)
  print "Tagging", item, tag(item)
