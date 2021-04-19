import requests

def get_data(title, url, description, body, datePublished):
  url = 'https://pokeapi.co/api/v2/pokemon?limit=100&offset=200 '
  params = {"autoCorrect": "true", "pageNumber": "1", "pageSize": "10", "q": "police", "safeSearch": "true" }
  r = requests.get(url, params=params)
  data = r.json()
  article_data = {'data': data['value']}
  return article_data