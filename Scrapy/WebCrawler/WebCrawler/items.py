# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyAnimeListItem(scrapy.Item):
    title = scrapy.Field()
    img = scrapy.Field()
    desc = scrapy.Field()