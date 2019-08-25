# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from bs4 import BeautifulSoup

class Top100ScraperPipeline(object):
    def process_item(self, item, spider):

        book_info['f_rank'] = int(''.join(filter(str.isdigit, book_info['f_rank'])))

        book_info['title'] = ' '.join(book_info['title'].split())

        try:
            book_info['price'] = book_info['price'].strip()
        except:
            print('No price for ' + book_info['title'])
            print(book_info['price'])

        try:
            book_info['series_num'] = int(''.join(filter(str.isdigit,
                book_info['series_num'])))
        except:
            pass

        try:
            book_info['series_len'] = int("".join(filter(str.isdigit,
                book_info['series_len'])))
        except:
            pass

        try:
            book_info['rating'] = float(book_info['rating'].split()[0])
        except:
            print('No rating for ' + book_info['title'])
            print(book_info['rating'])

        try:
            book_info['review_count'] = int((book_info['review_count'].
                replace(',','')).split()[0])
        except:
            print('No reviews for ' + book_info['title'])
            print(book_info['review_count'])

        try:
            book_info['page_count'] = int((book_info['page_count'].
                replace(',','')).split()[0])
        except:
            print('No page count for ' + book_info['title'])
            print(book_info['page_count'])

        try:
            book_info['publisher'] = book_info['publisher'].strip()
        except:
            print('No publisher for ' + book_info['title'])
            print(book_info['publisher'])

        try:
            book_info['all_rank'] = int(((' '.join(book_info['all_rank'].
                split())).replace('#','').split())[0])
        except:
            print('No kindle rank for ' + book_info['title'])
            print(book_info['all_rank'])

        try:
            book_info['blurb'] = BeautifulSoup(book_info['blurb']).text.strip('\n')
        except:
            print('No blurb for ' + book_info['title'])
            print(book_info['blurb'])

        return item
