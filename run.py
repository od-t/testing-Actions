import requests

response = requests.get("https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json")
if response.status_code == 200:
  print("Successful")
else:
  print("cannot obtain list")
