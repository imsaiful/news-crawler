# -*- coding: utf-8 -*-
import scrapy


class NewsfetchItem(scrapy.Item):
    headline = scrapy.Field()
    link = scrapy.Field()


class FirstpostSpider(scrapy.Spider):
    name = "firstpost"
    allowed_domains = ["www.firstpost.com"]
    start_urls = ['http://www.firstpost.com/']

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
                        # print(headline.encode('utf-8'))
                        # print(href)
                        # print('\n\n')

            list2 = response.xpath('//div//a[@href]//h1')

            for li in list2:
                headline = li.xpath('.//text()').extract_first()
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
            list3 = response.xpath('//div//a[@href]//h2')

            for li in list3:
                headline = li.xpath('.//text()').extract_first()
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
