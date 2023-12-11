import requests
from bs4 import BeautifulSoup

class GetArticlesBySearchBM:
    def __init__(self, string_search):
        self.url = "https://www.blogdumoderateur.com/?s=%s" % string_search
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        # self.max_pages = self.get_max_pages()
        self.max_pages = 10
        self.actual_page = 0
        self.string_search = string_search

    def get_max_pages(self):
        max_pages = self.soup.find_all('a', {'class': 'page'})[-1].text
        return max_pages

    def get_articles_by_content(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        articles = soup.find_all('article')
        return [
            {
                'category': article.find('span', {'class': 'favtag'}).text if article.find('span', {'class': 'favtag'}) else 'No category',
                'datetime': article.find('time').get('datetime').split('T') if article.find('time') else '',
                'img': article.find('img').get('src') if article.find('img') else '',
                'name_article': article.find('h3').text if article.find('h3') else '',
                'description': soup.find_all("div", {"class": "entry-excerpt"}),
                'key': article.get('id'),
            } for article in articles
        ]


    def get_articles_by_pages(self):
        data = {}
        while self.actual_page < int(self.max_pages):
            self.actual_page += 1
            if (self.actual_page == 1):
                actual_url = self.url
            else:
                actual_url = 'https://www.blogdumoderateur.com/page/%s/?s=%s' % (self.actual_page, self.string_search)
            actual_response = requests.get(actual_url)
            articles = self.get_articles_by_content(actual_response.text)
            data[self.actual_page] = articles

        return data



scrap_bm = GetArticlesBySearchBM('test')
exported_data = scrap_bm.get_articles_by_pages()



