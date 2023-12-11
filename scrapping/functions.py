import requests

def export_articles_bm(string_search):
    url = "https://www.blogdumoderateur.com/?s=%"%(string_search)
    response = requests.get(url)


