# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re
import logging
from  pymongo import MongoClient

client = MongoClient()
collection = client["sun1"]["news"]


class Suncrawl1Pipeline(object):
    def process_item(self, item, spider):
        item["content"] = self.process_content(item["content"])
        # logging.warning(item)
        # 注意 这里的item 是json 格式的数据 需要转换成dict 格式的数据 否则无法存到mongodb 中
        collection.insert(dict(item))
        return item

    def process_content(self, content):
        # 使用正则 re.sub(pattern,repl,string) 参数1:正则,参数2:要替换成啥样,参数3.要进行处理的字符串
        # 这里使用列表传导式处理每一个content数据
        content = [re.sub(r"\xa0|\s|\n", "", i) for i in content]
        # 这里还要处理一次  ""这种空字符串,去掉该空字符串
        content = [i for i in content if len(i) > 0]  # 去除列表中的空字符串
        return content

        pass
