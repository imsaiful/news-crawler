# -*- coding: utf-8 -*-
import scrapy


class NewsfetchItem(scrapy.Item):
    headline = scrapy.Field()
    link = scrapy.Field()


class IndianexpressSpider(scrapy.Spider):
    name = "indianexpress"
    allowed_domains = ["https://indianexpress.com/"]
    start_urls = ['https://indianexpress.com//']

    def parse(self, response):
        list = []
        list1 = (response.xpath('//h1/a[@href]'))
        list2 = (response.xpath('//h2/a[@href]'))
        list3 = (response.xpath('//h3/a[@href]'))
        list4 = (response.xpath('//h4/a[@href]'))
        list5 = (response.xpath('//h5/a[@href]'))
        list6 = (response.xpath('//h6/a[@href]'))

        try:
            for li in list1:
                headline = li.xpath('.//text()').extract_first()
                href = li.xpath('.//@href').extract_first()

                if type(headline) is str and headline not in list:
                    if (len(headline) > 20):
                        list.append(headline)
                        indianexpressitem = NewsfetchItem(
                            headline=headline, link=href)
                        yield indianexpressitem
                        # print(headline.encode('utf-8'))
                        # print(href)
                        # print("\n\n")
            for li in list2:
                headline = li.xpath('.//text()').extract_first()
                href = li.xpath('.//@href').extract_first()

                if type(headline) is str and headline not in list:
                    if (len(headline) > 20):
                        list.append(headline)
                        indianexpressitem = NewsfetchItem(
                            headline=headline, link=href)
                        yield indianexpressitem
                        # print(headline.encode('utf-8'))
                        # print(href)
                        # print("\n\n")

            for li in list3:
                headline = li.xpath('.//text()').extract_first()
                href = li.xpath('.//@href').extract_first()

                if type(headline) is str and headline not in list:
                    if (len(headline) > 20):
                        list.append(headline)
                        indianexpressitem = NewsfetchItem(
                            headline=headline, link=href)
                        yield indianexpressitem
                        # print(headline.encode('utf-8'))
                        # print(href)
                        # print("\n\n")
            for li in list4:
                headline = li.xpath('.//text()').extract_first()
                href = li.xpath('.//@href').extract_first()

                if type(headline) is str and headline not in list:
                    if (len(headline) > 20):
                        list.append(headline)
                        indianexpressitem = NewsfetchItem(
                            headline=headline, link=href)
                        yield indianexpressitem
                        # print(headline.encode('utf-8'))
                        # print(href)
                        # print("\n\n")
            for li in list5:
                headline = li.xpath('.//text()').extract_first()
                href = li.xpath('.//@href').extract_first()

                if type(headline) is str and headline not in list:
                    if (len(headline) > 20):
                        list.append(headline)
                        indianexpressitem = NewsfetchItem(
                            headline=headline, link=href)
                        yield indianexpressitem
                        # print(headline.encode('utf-8'))
                        # print(href)
                        # print("\n\n")
            for li in list6:
                headline = li.xpath('.//text()').extract_first()
                href = li.xpath('.//@href').extract_first()

                if type(headline) is str and headline not in list:
                    if (len(headline) > 20):
                        list.append(headline)
                        indianexpressitem = NewsfetchItem(
                            headline=headline, link=href)
                        yield indianexpressitem
                        # print(headline.encode('utf-8'))
                        # print(href)
                        # print("\n\n")

        except Exception as ex:
            print(ex)
            print(list)
