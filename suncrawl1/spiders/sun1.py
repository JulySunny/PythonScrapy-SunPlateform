# -*- coding: utf-8 -*-
import scrapy
from suncrawl1.items import Suncrawl1Item

class Sun1Spider(scrapy.Spider):
    name = 'sun1'
    # 要爬取的范围
    allowed_domains = ['sun0769.com']
    # 起始页
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    def parse(self, response):
        # 1.获取响应,处理数据
        tr_list=response.xpath("//div[@class='greyframe']/table[2]/tr/td/table/tr")
        # 2.遍历拿到所有的数据
        for tr in tr_list:
            item=Suncrawl1Item()
            item["title"]=tr.xpath("./td[2]/a[@class='news14']/@title").extract_first()
            item["type"]=tr.xpath("./td[2]/a[@class='red14']/text()").extract_first().strip()[1:-1]
            item["href"]=tr.xpath("./td[2]/a[@class='news14']/@href").extract_first()
            item["publish_date"]=tr.xpath("./td[@class='t12wh']/text()").extract_first() #
            item["person"]=tr.xpath("./td[4]/text()").extract_first()  # 投诉人
            item["state"]=tr.xpath("./td[3]/span/text()").extract_first()  # 处理状态
            # print(item)
            # 爬取详情页
            yield scrapy.Request(
                # 1.请求的url
                item["href"],
                # 2.回调函数
                callback=self.parse_detail,
                # 3.数据传递 通过meta传递
                meta={"item":item}
            )
            # 翻页--查找翻页的 ">"  图 标
        next_url=response.xpath("//a[text()='>']/@href").extract_first()
        if next_url is not None:
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )
    def parse_detail(self,response):
        # 获取响应
        item=response.meta["item"]
        # item["content"]=response.xpath("//div[@class='contentext']/text()").extract()
        item["content"]=response.xpath("/html/body/div[@class='wzy1'][1]/table[2]//tr[1]/td[@class='txt16_3']/text()").extract()
        item["content_img"]=response.xpath("//td[@class='txt16_3']//img/@src").extract()
        item["content_img"]=["http://wz.sun0769.com"+ i  for i in item["content_img"]]
        # 传递item
        yield item

