# -*- coding: utf-8 -*-

import scrapy
import TianMao.Common
from TianMao.items import TianMaoItem


class DmozSpider(scrapy.Spider):
    def __init__(self):
        TianMao.Common.CURRENT_URL = TianMao.Common.URL28
        TianMao.Common.CURRENT_TYPE = TianMao.Common.TYPE28
        self.name = "tianmao_tixu"
        self.allowed_domains = ["tmall.com"]
        self.start_urls = [
            TianMao.Common.CURRENT_URL
        ]

    name = "tianmao_tixu"
    allowed_domains = ["tmall.com"]
    start_urls = [
        TianMao.Common.CURRENT_URL
    ]

    def parse(self, response):
        items = []
        for sel in response.xpath("//*[@id='J_ItemList']/div"):
            item = TianMaoItem()
            # 商品ID
            id = sel.xpath("@data-id").extract()
            # 商品链接
            url = sel.xpath("./div/div[@class='productImg-wrap']/a/@href").extract()
            # 商品图片one,可能抓取不到
            img = []
            imgOne = sel.xpath("./div/div[@class='productImg-wrap']/a/img/@src").extract()
            imgTwo = sel.xpath("./div/div[@class='productImg-wrap']/a/img/@data-ks-lazyload").extract()
            if imgOne:
                img = imgOne
            else:
                img = imgTwo
            print img
            # 商品名称
            title = sel.xpath("./div/p[@class='productTitle']/a/text()").extract()
            # 商品价格
            price = sel.xpath("./div/p[@class='productPrice']/em/@title").extract()
            #成交量
            valume = sel.xpath("./div/p[@class='productStatus']/span/em/text()").extract()

            item['id'] = [i.encode('utf-8') for i in id]
            item['url'] = [u.encode('utf-8') for u in url]
            item['img'] = [im.encode('utf-8') for im in img]
            item['title'] = [t.encode('utf-8') for t in title]
            item['price'] = [p.encode('utf-8') for p in price]
            item['valume'] = [v.encode('utf-8') for v in valume]

            if len(item['img']) <= 0:
                item['img'] = [
                    '//b.hiphotos.baidu.com/image/h%3D200/sign=7e9d1a99a9345982da8ae2923cf5310b/d009b3de9c82d15825ffd75c840a19d8bd3e42da.jpg']
            items.append(item)
        return items