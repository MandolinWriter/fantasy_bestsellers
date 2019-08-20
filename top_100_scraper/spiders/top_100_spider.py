import scrapy

class Top100Spider(scrapy.Spider):
    name = "top100"

    start_urls = [
        ('https://www.amazon.com/Best-Sellers-Kindle-Store-Fantasy/zgbs/'
            'digital-text/158576011'),
    ]

    def parse(self, response):
        for book in response.xpath('//div[has-class("a-section a-spacing-none aok-relative")]'):
            yield {
                'f-rank': book.xpath('./div/span/span/text()').get(),
                'title': book.xpath('./span/a/div/text()').get(),
                'author': book.xpath('./span/div[1]/a/text()').get(),
                'price': book.xpath('./span/div[3]/a/span/span/text()').get()
            }
        next_page_url = response.xpath('//li[@class="a-last"]/a/@href').get()

        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
