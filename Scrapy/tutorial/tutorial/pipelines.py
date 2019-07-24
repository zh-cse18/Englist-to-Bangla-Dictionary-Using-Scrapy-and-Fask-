# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class TutorialPipeline(object):
    def __init__(self):
        self.create_sqlite_connection()
        self.create_table_dictionary_tb()

    def create_sqlite_connection(self):
        self.sqlite_conn = sqlite3.connect("mydb.db")
        self.curr = self.sqlite_conn.cursor()

    def create_table_dictionary_tb(self):
        self.curr.execute("""DROP TABLE IF EXISTS dictionary_tb""")
        self.curr.execute("""create table dictionary_tb(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     eng  text,
                     ban  text
                     )""")

    def store_item(self, item, spider):
        self.store_into_db(item)
        return item

    def store_into_db(self, item):
        self.curr.execute("""insert into dictionary_tb values(?,?)""", (
            item['eng_word'],
            item['bengli_mean']
        ))
        self.conn.commit()
