# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field,Item


class TianMaoItem(Item):
    id = Field()
    url = Field()
    img = Field()
    price = Field()
    title = Field()
    valume = Field()
    pass
