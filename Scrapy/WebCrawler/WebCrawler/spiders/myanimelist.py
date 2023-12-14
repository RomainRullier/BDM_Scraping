import scrapy
from scrapy import Request
from WebCrawler.items import MyAnimeListItem
from WebCrawler.pipelines import *

class MyAnimeListSpider(scrapy.Spider):
    name = 'myanimelist'
    allowed_domains = ['myanimelist.net']
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    start_urls = ['https://myanimelist.net/manga.php?letter={letter}'.format(letter=letter) for letter in letters]
    database = DataBase('myanimelist')

    # Create table
    try:
      database.create_table('myanimelist',
        title = db.String,
        img = db.String,
        desc = db.String,
      )
    except:
      pass

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_myanimelist)

    def parse_myanimelist(self, response):
        # Liste des animés en ignorant le premier tr
        list_anime = response.css('div.js-categories-seasonal table tr')[1:]

        for anime in list_anime:
            item = MyAnimeListItem()

            # Nom de l'animé
            try:
              item['title'] = anime.css('a strong::text').get()
            except:
              item['title'] = 'None'

            # Image de l'animé
            try:
              item['img'] = anime.css('div.picSurround img::attr(data-src)').get()
            except:
              item['img'] = 'None'

            # Description de l'animé
            try:
              item['desc'] = anime.css('div.pt4::text').get()
            except:
              item['desc'] = 'None'

            self.database.add_row('myanimelist', 
              title = item['title'],
              img = item['img'],
              desc = item['desc'],
            )

            yield item