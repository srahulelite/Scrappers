# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging


class WorldometerPipeline:
    def open_spider(self, spider):
        logging.warning("SPIDER OPENED >>>>>>>")

    def close_spider(self, spider):
        logging.warning("SPIDER CLOSED >>>>>>>")

    def process_item(self, item, spider):
        logging.warning(str(type(item))  + ">>>>>>++++")
        return item
