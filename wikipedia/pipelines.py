# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WikipediaPipeline(object):
    def process_item(self, item, spider):
        if item['R']:
            texto = item['R'].strip()
            texto = texto.replace('"','')
            texto = texto.upper()
            item['R'] = texto
        if item['R']:
            return item

class SaveDataPipeline(object):
    def open_spider(self,spider):
        self.arquivo = open("dados.txt","x")
    def process_item(self, item, spider):
        self.arquivo.write(item['R'] + '\n')
        return item
    def close_spider(self,spider):
        self.arquivo.close()
