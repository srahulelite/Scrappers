# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
import sqlite3

class SQLitePipeline:
    def open_spider(self, spider):
        self.connection = sqlite3.connect('transcripts.db')
        self.c = self.connection.cursor()

        #query
        try:
            self.c.execute('''
                        CREATE TABLE transcripts(
                        title TEXT,
                        plot TEXT,
                        transcript TEXT,
                        url TEXT
                           )
                        ''')
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO transcripts (title, plot, transcript, url) VALUES(?,?,?,?)
        ''',(
                item.get('title'),
                item.get('plot'),
                item.get('transcript'),
                item.get('url')
            ))
        self.connection.commit()
        return item
    
class WorldometerPipeline:
    def open_spider(self, spider):
        logging.warning("SPIDER OPENED >>>>>>>")

    def close_spider(self, spider):
        logging.warning("SPIDER CLOSED >>>>>>>")

    def process_item(self, item, spider):
        logging.warning(str(type(item))  + ">>>>>>++++")
        return item
