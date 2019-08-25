# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from bs4 import BeautifulSoup

class Top100ScraperPipeline(object):
    def process_item(self, item, spider):

        item['f_rank'] = int(''.join(filter(str.isdigit, item['f_rank'])))

        item['title'] = ' '.join(item['title'].split())

        try:
            item['price'] = item['price'].strip()
        except:
            print('No price for ' + item['title'])
            print(item['price'])

        try:
            item['series_num'] = int(''.join(filter(str.isdigit,
                item['series_num'])))
        except:
            pass

        try:
            item['series_len'] = int("".join(filter(str.isdigit,
                item['series_len'])))
        except:
            pass

        try:
            item['rating'] = float(item['rating'].split()[0])
        except:
            print('No rating for ' + item['title'])
            print(item['rating'])

        try:
            item['review_count'] = int((item['review_count'].
                replace(',','')).split()[0])
        except:
            print('No reviews for ' + item['title'])
            print(item['review_count'])

        try:
            item['page_count'] = int((item['page_count'].
                replace(',','')).split()[0])
        except:
            print('No page count for ' + item['title'])
            print(item['page_count'])

        try:
            item['publisher'] = item['publisher'].strip()
        except:
            print('No publisher for ' + item['title'])
            print(item['publisher'])

        try:
            item['all_rank'] = int(((' '.join(item['all_rank'].
                split())).replace('#','').split())[0])
        except:
            print('No kindle rank for ' + item['title'])
            print(item['all_rank'])

        try:
            item['blurb'] = BeautifulSoup(item['blurb']).text.strip('\n')
        except:
            print('No blurb for ' + item['title'])
            print(item['blurb'])

        return item
