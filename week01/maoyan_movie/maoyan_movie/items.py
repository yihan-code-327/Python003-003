# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    c_name = scrapy.Field()
    e_name = scrapy.Field()
    on_date = scrapy.Field()
    movie_types = scrapy.Field()
    
