import scrapy
from maoyan_movie.items import MaoyanMovieItem
from scrapy.selector import Selector


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/board']

    
    def start_requests(self):
        url = 'http://maoyan.com/board'
        yield scrapy.Request(url, callback = self.parse)
            
    def parse(self, response):
        print(response.url)
        # 打印网页的内容
        print(response.text)
        
        movies = Selector(response = response).xpath('//p[@class="name"]')
        for m in movies:
            link = m.xpath('./a/@href').extract_first()
            print(link)
            yield scrapy.Request(url = f'http://maoyan.com{link}',  callback = self.parse2)

    def parse2(self, response):
        item  = MaoyanMovieItem()
        mb = Selector(response = response).xpath('//div[@class="movie-brief-container"]') 
        item['c_name'] = mb.xpath('./h1/text()').extract_first()
        item['e_name'] = mb.xpath('./div/text()').extract_first()
        item['on_date'] = mb.xpath('./ul/li[3]/text()').extract_first()
        item['movie_types'] = ','.join(mb.xpath('./ul/li/a/text()').extract())
        print(item['c_name'])
        print('...........')
        yield item