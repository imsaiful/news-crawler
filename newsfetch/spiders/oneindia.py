# -*- coding: utf-8 -*-
import scrapy

# //div[@class="main-block"]/a[@href]
# //li/a[@href]/div[@class='oi-slider-text']
# //div[@class="news-desc"]/a[@href]]


class NewsfetchItem(scrapy.Item):
    headline = scrapy.Field()
    link = scrapy.Field()


class OneindiaSpider(scrapy.Spider):
    name = "oneindia"
    allowed_domains = ["www.oneindia.com"]
    start_urls = ['http://www.oneindia.com/']

    def parse(self, response):
        list = response.xpath('//div[@class="news-desc"]/a[@href]')
        list1 = []
        try:
            for li in list:
                headline = li.xpath('.//text()').extract_first()
                href = li.xpath('.//@href').extract_first()

                if type(headline) is str and headline not in list1:

                    if(len(headline) > 22):

                        list1.append(headline)
                        oneindiaitem = NewsfetchItem(
                            headline=headline, link=href)
                        yield oneindiaitem
                        # print(headline.encode('utf-8'))
                        # print(href)
                        # print('\n\n')

            list2 = response.xpath(
                '//li/a[@href]/div[@class="oi-slider-text"]')

            for li in list2:
                headline = li.xpath('.//text()').extract_first()
                href = li.xpath('.//@href').extract_first()

                if type(headline) is str and headline not in list1:

                    if(len(headline) > 22):

                        list1.append(headline)
                        oneindiaitem = NewsfetchItem(
                            headline=headline, link=href)
                        yield oneindiaitem
                        # print(headline.encode('utf-8'))
                        # print(href)
                        # print('\n\n')
            list3 = response.xpath('//div[@class="main-block"]/a[@href]')

            for li in list3:
                headline = li.xpath('.//text()').extract_first()
                href = li.xpath('.//@href').extract_first()

                if type(headline) is str and headline not in list1:

                    if(len(headline) > 22):

                        list1.append(headline)
                        oneindiaitem = NewsfetchItem(
                            headline=headline, link=href)
                        yield oneindiaitem
                        # print(headline.encode('utf-8'))
                        # print(href)
                        # print('\n\n')

        except Exception as ex:
            print(ex)
