# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class MaoyanMoviePipeline:
    def process_item(self, item, spider):
        c_name = item['c_name']
        e_name = item['e_name']
        movie_types = item['movie_types']
        on_date = item['on_date']
        output = f'{c_name}, {e_name},{movie_types}, {on_date}\n'
        with open('./maoyan_scrapy.csv', 'a+', encoding='utf-8') as article:
            article.write(output)
        print('csv generated')
        return item