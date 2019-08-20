import scrapy

class Top100Spider(scrapy.Spider):
    name = "top100"

    start_urls = [
        ('https://www.amazon.com/Best-Sellers-Kindle-Store-Fantasy/zgbs/'
            'digital-text/158576011'),
    ]

    def parse(self, response):
        for book in response.xpath('//span[has-class("aok-inline-block zg-item")]'):
            yield {
                'title': book.xpath('./a/div/text()').get(),
                'author': book.xpath('./div[1]/a/text()').get(),
                'price': book.xpath('./div[3]/a/span/span/text()').get()

        # yield {
        #     'title': response.css('title::text').get()
        }
