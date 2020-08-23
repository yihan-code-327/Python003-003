from scrapy import Selector

sample_file = "././movie1.html"

with open(sample_file, 'r', encoding='utf-8-sig', newline='') as f:
    page = f.read()
    mb = Selector(text=str(page)).xpath('//div[@class="movie-brief-container"]') 
    c_name = mb.xpath('./h1/text()').extract_first()
    e_name = mb.xpath('./div/text()').extract_first()
    on_date = mb.xpath('./ul/li[3]/text()').extract_first()
    movie_type = ','.join(mb.xpath('./ul/li/a/text()').extract())
    


    
    #movie_types = Selector(text=str(page)).xpath('//div[@movie-brief-container]/ul/li/a/').extract()
    #c_name = Selector(text=str(page).xpath('//h1[class="name"]').extract()
    #print(c_name)
    #e_name = Selector(text=str(page)).xpath('//div[class = "ename ellipsis"]/text()').extract()
    #print(e_name)
    #on_date = Selector(text=str(page)).xpath('//div[@movie-brief-container]/ul/li[2]/text()').extract()
    #print(movie_types, c_name, e_name, on_date)

