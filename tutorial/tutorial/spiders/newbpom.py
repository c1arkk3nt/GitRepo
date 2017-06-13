import scrapy

from scrapy.selector import HtmlXPathSelector
		
class NewBPom(scrapy.Item):
	noreg = scrapy.Field()
	product = scrapy.Field()
	registered = scrapy.Field()
	
class NewBPomSpider(scrapy.Spider):
	name = "newbpom"
	start_urls = 	['http://cekbpom.pom.go.id/']