# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import codecs


class GetchuxiaoPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d',time.localtime())
        filename = today + '.txt'
        with codecs.open(filename,'a', 'utf-8') as fp:
            fp.write("{'Gname':'%s','discount':'%s','price':'%s','grade':'%s'}\n"
                                                %(item['Gname'],
                                              item['cost'],
                                              item['price'],
                                              item['grade']
                                              ))
        print("txt读写完成")
        fp.close()
        return item
