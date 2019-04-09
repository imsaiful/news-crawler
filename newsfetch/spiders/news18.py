# -*- coding: utf-8 -*-
import scrapy
import re


class NewsfetchItem(scrapy.Item):
    headline = scrapy.Field()
    link = scrapy.Field()


class News18Spider(scrapy.Spider):
    name = "news18"
    allowed_domains = ["https://www.news18.com"]
    start_urls = ['https://www.news18.com//']

    def parse(self, response):
        list = response.xpath('//li/a[@href]')
        list1 = []
        try:
            for li in list:
                headline = li.xpath('.//text()').extract_first()
                href = li.xpath('.//@href').extract_first()

                if type(headline) is str and headline not in list1:

                    if(len(headline) > 22):

                        list1.append(headline)
                        news18item = NewsfetchItem(
                            headline=headline, link=href)
                        yield news18item
                        # print(headline)
                        # print(href)
                        # print('\n\n')

            list2 = response.xpath('//div[@class="lead-story"]//a[@href]')

            for li in list2:
                headline = li.xpath('.//h1/text()').extract_first()
                href = li.xpath('.//@href').extract_first()

                if type(headline) is str and headline not in list1:

                    if(len(headline) > 22):

                        list1.append(headline)
                        news18item = NewsfetchItem(
                            headline=headline, link=href)
                        yield news18item
                        # print(headline.encode('utf-8'))
                        # print(href)
                        # print('\n\n')

        except Exception as ex:
            print(ex)
