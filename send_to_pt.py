import requests, json

API_KEY = '9ebc7389571ea27228f6945532087e49b0f9cd13397f67ef23008c8ad1c54e82'

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
  
for item in [ x.strip() for x in open('hackingteam_vps', 'r').readlines() ]:
  print "Classifying", item, classify(item)
  print "Tagging", item, tag(item)
