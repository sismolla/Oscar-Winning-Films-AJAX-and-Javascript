# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class AjaxScraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        list = ['year', 'awards', 'nominations']
        try:
            for items in list:
                value = adapter.get(items)
                if value is not None:
                    adapter[items] = float(value.strip())
            print('task is compleat.... ')
        except Exception as e:
            print('error found..........', e)

        return item
