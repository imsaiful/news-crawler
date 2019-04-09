# -*- coding: utf-8 -*-
import scrapy

class NewsfetchItem(scrapy.Item):
    headline = scrapy.Field()
    link = scrapy.Field()

class RepublicSpider(scrapy.Spider):
    name = "republic"
    allowed_domains = ["www.republicworld.com"]
    start_urls = ['http://www.republicworld.com/']

    def parse(self, response):
        list = response.xpath('//a[@href ] /div[@class="card-headline txtTruncate"]/..')
        list2 = response.xpath('//a[@href]/span[@class="card-headline txtTruncate "]/..')
        # listheadline = []
        # listlink = []
        #


        for li in list:
            headline1 = (li.xpath('.//div[@class="card-headline txtTruncate"]/text()').extract_first())
            if type(headline1) is str:
                headline1 = headline1.strip()
                href = (li.xpath('.//@href').extract_first())
                republicitem = NewsfetchItem(headline= headline1,link=href)
                yield republicitem


            # listheadline.append(headline.strip())
            # listlink.append(href)

        for li in list2:
            headline1 = (li.xpath('.//span[@class="card-headline txtTruncate "]/text()').extract_first())
            href = (li.xpath('.//@href').extract_first())
            if type(headline1) is str:
                    headline1 = headline1.strip()
                    print(headline1)
                    href = (li.xpath('.//@href').extract_first())
                    print(href)
                    republicitem = NewsfetchItem(headline= headline1,link=href)
                    yield republicitem


                # listheadline.append(headline.strip())
                # listlink.append(href)
        # for hl in listheadline:
        #         print(hl)
        #         print('\n\n')
        # for hl in listlink:
        #         print(hl)
        #         print('\n\n')
