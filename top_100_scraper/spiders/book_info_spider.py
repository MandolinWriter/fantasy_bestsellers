import scrapy
from top_100_scraper.items import BookItem


class BookInfoSpider(scrapy.Spider):
    name = "book_info"

    start_urls = {
        ('https://www.amazon.com/Best-Sellers-Kindle-Store-Fantasy/zgbs/'
            'digital-text/158576011'),
    }

    def parse(self, response):
        counter = 1


        for book in response.xpath('//div[has-class("a-section a-spacing-none aok-relative")]'):
            book_info = BookItem()

            book_info['f_rank'] = int(' '.join(filter(str.isdigit,
                book.xpath('./div/span/span/text()').get())))

            next_book_url = book.xpath('./span/a/@href').get()

            if next_book_url is not None:
                yield scrapy.Request(response.urljoin(next_book_url),
                    callback = self.parse_book, meta = {'item': book_info})
            if counter > 3:
                break

            counter = counter + 1

    def parse_book(self, response):
        book_info = response.meta['item']

        book_info['title'] = " ".join(response.xpath(
            '//span[@id = "ebooksProductTitle"]/text()').get().split())

        book_info['author'] = response.xpath('//div[@id = "bylineInfo"]/span/span[1]'
            '/a/text()').get()

        book_info['price'] = " ".join(response.xpath('//tr[@class = "kindle-price"]'
            '/td/span/text()').get().split())

        group_str = '//div[@id = "reviewFeatureGroup"]'
        book_info['series'] = response.xpath(group_str + '/span/a/text()').get()

        try:
            book_info['series_num'] = int(' '.join(filter(str.isdigit,
                response.xpath(group_str + '/span/b').get())))
        except:
            book_info['series_num'] = None

        try:
            book_info['series_len'] = int(' '.join(filter(str.isdigit,
                response.xpath(group_str + '/span/text()').getall()[1])))
        except:
            book_info['series_len'] = None

        book_info['rating'] = float(response.xpath(group_str + '//div[@id = "averageCustomerReviews"]'
            '/span/span/@title').get().split()[0])
        book_info['review_count'] = int((response.xpath(
            group_str + '//span[@id = "acrCustomerReviewText"]/text()').get().
            replace(',','')).split()[0])

        detail_str = '//div[@id = "detail-bullets"]//div[@class = "content"]'
        book_info['page_count'] = int(response.xpath(
            detail_str + '/ul/li[2]/text()').get().replace(',','').split()[0])
        #book_info['publisher'] = response.xpath(detail_str + '/ul/li[3]/text()').get()
        book_info['all_rank'] = int(((' '.join(response.xpath(detail_str +
            '//li[@id = "SalesRank"]/text()').getall()[1].split())).replace('#','').split())[0])


        if response.xpath('//span[@id = "upsell-button"]').get() is not None:
            book_info['ku'] = 'yes'
        else:
            book_info['ku'] = 'no'

        book_info['blurb'] = response.xpath('//div[@id = "bookDescription_feature_div"]'
            '/noscript').get()

        yield book_info
