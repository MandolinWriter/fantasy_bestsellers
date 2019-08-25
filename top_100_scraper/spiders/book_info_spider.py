import scrapy
from top_100_scraper.items import BookItem


class BookInfoSpider(scrapy.Spider):
    name = "book_info"

    start_urls = {
        ('https://www.amazon.com/Best-Sellers-Kindle-Store-Fantasy/zgbs/'
            'digital-text/158576011'),
    }

    def parse(self, response):

        for book in response.xpath('//div[has-class("a-section a-spacing-none aok-relative")]'):

            book_info = BookItem()

            book_info['f_rank'] = book.xpath('./div/span/span/text()').get()

            next_book_url = book.xpath('./span/a/@href').get()

            if next_book_url is not None:
                yield scrapy.Request(response.urljoin(next_book_url),
                    callback = self.parse_book, meta = {'item': book_info})


        next_page_url = response.xpath('//ul[@class = "a-pagination"]'
            '//li[@class="a-last"]/a/@href').get()

        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))



    def parse_book(self, response):
        book_info = response.meta['item']

        book_info['title'] = response.xpath(
            '//span[@id = "ebooksProductTitle"]/text()').get()

        book_info['author'] = response.xpath('//div[@id = "bylineInfo"]/span/span[1]'
            '/a/text()').get()

        book_info['price'] = response.xpath('//tr[@class = "kindle-price"]'
            '//span[@class = "a-size-medium a-color-price"]/text()').get()

        group_str = '//div[@id = "reviewFeatureGroup"]'
        book_info['series'] = response.xpath(group_str + '/span/a/text()').get()
        book_info['series_num'] = response.xpath(group_str + '/span/b').get()
        book_info['series_len'] = response.xpath(group_str + '/span/text()').getall()[1]
        book_info['rating'] = response.xpath(group_str + '//div[@id = "averageCustomerReviews"]'
            '/span/span/@title').get()
        book_info['review_count'] = response.xpath(
            group_str + '//span[@id = "acrCustomerReviewText"]/text()').get()


        detail_str = '//div[@id = "detail-bullets"]//div[@class = "content"]'
        book_info['page_count'] = response.xpath(detail_str +
            '//li/b[contains(text(), "Print Length:")]/../text()').get()
        book_info['publisher'] = response.xpath(detail_str +
            '//li/b[contains(text(), "Publisher:")]/../text()').get()
        book_info['all_rank'] = response.xpath(detail_str +
            '//li[@id = "SalesRank"]/text()').getall()[1]

        if response.xpath('//span[@id = "upsell-button"]').get() is not None:
            book_info['ku'] = 'yes'
        else:
            book_info['ku'] = 'no'

        book_info['blurb'] = response.xpath('//div[@id = "bookDescription_feature_div"]'
            '/noscript').get()

        yield book_info
