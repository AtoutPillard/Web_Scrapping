"""Web scrapping and data integration to the database"""

from urllib.request import urlopen
import json
import controller as ctrl
import pandas as pd

# Connect to the mongoDB database
db = ctrl.init_collection()

def get_all_pages():
  """
  Get all the links in order to get articles and return a list of them
  """

  urls = []
  for page in range(10):
    url = f"https://techcrunch.com/wp-json/tc/v1/magazine?page={page}&_embed=true&cachePrevention=0"
    urls.append(url)
  return urls

def get_article(result):
  """
  Create a dictionnary containing web scrapped data
  """

  article = {
      'category'  : result.get('parsely-section').lower().replace("amp;", ''),
      'title'     : result.get('parsely-title'),
      'author'    : result.get('parsely-author'),
      'date'      : result.get('parsely-pub-date').split("T")[0],
      'link'      : result.get('parsely-link'),
  }
  return article

def data_integration():
  """
  Parse all articles and integrate data to mongoDB database
  """
  list_article = []
  pages = get_all_pages()
  for page in pages:
    # Get all articles from techcrunch requests
    response = urlopen(page).read().decode("utf-8")
    dic = json.loads(response)
    print(f'Scrapping all article from {page}')
    # Create a dictionnary for all article in a request
    for i in range(len(dic)):
      article_data = dic[i-1]['parselyMeta']
      article = get_article(article_data)
      list_article.append(article)
  # Delete all duplicate articles
  list_unique = pd.DataFrame(list_article).astype(str).drop_duplicates().to_dict('records')
  # Insert articles in the mongoDB database
  x = db.insert_many(list_unique)
  return

data_integration()