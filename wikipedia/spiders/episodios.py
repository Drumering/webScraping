# -*- coding: utf-8 -*-
import scrapy


class EpisodiosSpider(scrapy.Spider):
    name = 'episodios'
    allowed_domains = ['https://pt.wikipedia.org/wiki/Lista_de_epis%C3%B3dios_de_Breaking_Bad']
    start_urls = ['https://pt.wikipedia.org/wiki/Lista_de_epis%C3%B3dios_de_Breaking_Bad']

    def parse(self, response):
        nomes = response.xpath('//table[@class="wikitable plainrowheaders wikiepisodetable"]//td[@class="summary"]//text()').extract()
        for nome in nomes:
            yield {'R':nome}
