import requests
import configparser

config_file = configparser.RawConfigParser()   
configFilePath = r'config.txt'
config_file.read(configFilePath)

zone_id = config_file.get('config', 'zone_id')
dns_record_id = config_file.get('config', 'dns_record_id')

name_list = ['an', '*', 'drewku.com', 'feed', 'tube']

# Get current IP 
external_ip = requests.get('https://checkip.amazonaws.com').text.strip()
print("Your External IP is: " + external_ip)


headers = {'Content-Type': 'application/json', 'X-Auth-Email' : config_file.get('config', 'auth_email') , 'X-Auth-Key': config_file.get('config', 'api_key')}

data = {
  'content': external_ip,
  'name': '',
  'proxied': True,
  'type': 'A',
  'comment': 'Domain verification record',
  'id': '023e105f4ecef8ad9ca31a8372d0c353',
  'tags': [],
  'ttl': 3600
}



url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{dns_record_id}'

r = requests.put(url, headers=headers, data=data)
print(r.json())
