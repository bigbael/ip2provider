import ipaddress
import requests
from bs4 import BeautifulSoup as bs

# https://www.cloudflare.com/en-ca/ips/
# Texts lists 404, must be scraped

def update():
	results = []

	#response = requests.get('https://www.cloudflare.com/en-ca/ips/')
    response = requests.get('https://www.cloudflare.com/ips-v4')

	if response.status_code != 200:
		return False

	soup = bs(response.text, features='html.parser')
	#elements = soup.find('h5',string='IPv4').parent.find_all('li')
    elements = soup.text
    
	for elem in elements.split("\n"):
		#cidr = elem.text
		cidr = elem
        results.append("%s %s unknown unknown" % (cidr, 'cloudflare'))

	# Write results to file
	with open('data/cloudflare.txt', 'w') as f:
		f.write("\n".join(results))
		f.close()

	return len(results)
