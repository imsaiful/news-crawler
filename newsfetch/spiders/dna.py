# -*- coding: utf-8 -*-
import scrapy

# //h3/a[@href]
# //a[@href]/h3


class NewsfetchItem(scrapy.Item):
    headline = scrapy.Field()
    link = scrapy.Field()


class DnaSpider(scrapy.Spider):
    name = "dna"
    allowed_domains = ["www.dnaindia.com"]
    start_urls = ['http://www.dnaindia.com/']

    def parse(self, response):
        list = response.xpath('//h3/a[@href]')
        list1 = []
        try:
            for li in list:
                headline = li.xpath('.//text()').extract_first()
                href = li.xpath('.//@href').extract_first()
                href = "www.dnaindia.com" + href

                if type(headline) is str and headline not in list1:

                    if(len(headline) > 22):

                        list1.append(headline)
                        dnaitem = NewsfetchItem(
                            headline=headline, link=href)
                        yield dnaitem
                        # print(headline.encode('utf-8'))
                        # print(href)
                        # print('\n\n')

            list2 = response.xpath('//a[@href]/h3')

            for li in list2:
                headline = li.xpath('.//text()').extract_first()
                href = li.xpath('..//@href').extract_first()
                href = "www.dnaindia.com" + href

                if type(headline) is str and headline not in list1:

                    if(len(headline) > 22):

                        list1.append(headline)
                        dnaitem = NewsfetchItem(
                            headline=headline, link=href)
                        yield dnaitem
                        # print(headline.encode('utf-8'))
                        # print(href)
                        # print('\n\n')

        except Exception as ex:
            print(ex)
