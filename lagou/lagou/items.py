# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #pass
    #area=scrapy.Field()
    job=scrapy.Field()

    tech_area=scrapy.Field()
    job_name=scrapy.Field()
