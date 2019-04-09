# -*- coding: utf-8 -*-
import scrapy

class NewsfetchItem(scrapy.Item):
    headline = scrapy.Field()
    link = scrapy.Field()

class ThehinduSpider(scrapy.Spider):
    name = "thehindu"
    allowed_domains = ["www.thehindu.com"]
    start_urls = ['http://www.thehindu.com/']

    def parse(self, response):
      list = response.xpath('//a[@href]')
      list1 = []

      for li in list:
            headline = li.xpath('.//text()').extract_first()
            href = li.xpath('.//@href').extract_first()



            if type(headline) is str and headline not in list1:
                headline1 = headline.strip()
                if(len(headline1)>22 and headline1 != "web.thehindu@thehindu.co.in" and "The Hindu Crossword " not in headline1):

                    list1.append(headline1)
                    thehinduitem = NewsfetchItem(headline= headline1,link=href)
                    yield thehinduitem
                    # print(headline1)
                    # print(href)
                    # print('\n\n')
