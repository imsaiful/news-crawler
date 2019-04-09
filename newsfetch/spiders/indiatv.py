# -*- coding: utf-8 -*-
import scrapy

class NewsfetchItem(scrapy.Item):
    headline = scrapy.Field()
    link = scrapy.Field()


class IndiatvSpider(scrapy.Spider):
    name = "indiatv"
    allowed_domains = ["www.indiatvnews.com"]
    start_urls = ['http://www.indiatvnews.com/']

    def parse(self, response):
        list1 = (response.xpath('//h2/a[@href]'))
        list2 = (response.xpath('//h3/a[@href]'))
        list3 = response.xpath('//h1[@class="caption"]/..')
        list4 = response.xpath('//h2[@class="caption"]/..')
        list = []
        
        for li in list3:
            headline = li.xpath('.//h1/text()').extract_first()
            href = li.xpath('.//@href').extract_first()
            if type(headline) is str and headline not in list1:
                    if (len(headline)>15):
                        list.append(headline)
                        indiatvitem = NewsfetchItem(headline= headline,link=href)
                        yield indiatvitem



        for li in list4:
            headline = li.xpath('.//h2/text()').extract_first()
            href = li.xpath('.//@href').extract_first()
            if type(headline) is str and headline not in list1:
                    if (len(headline)>15):
                        list.append(headline)
                        indiatvitem = NewsfetchItem(headline= headline,link=href)
                        yield indiatvitem

        for li in list1:
            headline = li.xpath('.//text()').extract_first()
            href = li.xpath('.//@href').extract_first()
            if type(headline) is str and headline not in list1:
                    if (len(headline)>15):
                        list.append(headline)
                        indiatvitem = NewsfetchItem(headline= headline,link=href)
                        yield indiatvitem

            # print(headline)
            # print(href)
            # print('\n\n')
        for li in list2:
            headline = li.xpath('.//text()').extract_first()
            href = li.xpath('.//@href').extract_first()
            if type(headline) is str and headline not in list1:
                    if (len(headline)>15):
                        list.append(headline)
                        indiatvitem = NewsfetchItem(headline= headline,link=href)
                        yield indiatvitem


            # print(headline)
            # print(href)
            # print('\n\n')

            # print(headline)
            # print(href)
            # print('\n\n')



            # print(headline)
            # print(href)
            # print('\n\n')
