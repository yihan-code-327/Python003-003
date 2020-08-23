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
            # callback 引擎将下载好的页面（response对象）发送给该方法， 执行数据解析
            # callback 可以指定新的函数， 不用parse作为默认的回调参数 
    
    def parse(self, response):
        
        #print(response.url)
        #print(response.text)
        movies = Selector(response = response).xpath('//p[@class="name"]')
        
        for m in movies:
            link = m.xpath('./a/@href').extract()
            #print(link)
            yield scrapy.Request(url = f'http://maoyan.com{link}', meta = {'item':item}, callback = self.parse2)

    def parse2(self, response):
        item  = MaoyanMovieItem()
        #item = response.meta['item']
        movie_types = Selector(response = response).xpath('//div[@movie-brief-container]/ul/li/a/text()').extract_all()
        c_name = Selector(response = response).xpath('//div[@movie-brief-container]/h1[@name]/text()').extract()
        e_name = Selector(response = response).xpath('//div[@movie-brief-container]/div[@ename ellipsis]/text()').extract()
        on_date = Selector(response = response).xpath('//div[@movie-brief-container]/ul/li[2]/text()').extract()
        print(movie_types, c_name, e_name, on_date)
        #item['movie_types'] = Selector(response = response).xpath('//div[@movie-brief-container]/ul/li/a/text()').extract_all()
        #item['c_name'] = Selector(response = response).xpath('//div[@movie-brief-container]/h1[@name]/text()').extract()
        #item['e_name'] = Selector(response = response).xpath('//div[@movie-brief-container]/div[@ename ellipsis]/text()').extract()
        #item['on_date'] = Selector(response = response).xpath('//div[@movie-brief-container]/ul/li[3]/text()').extract()
        
        yield item