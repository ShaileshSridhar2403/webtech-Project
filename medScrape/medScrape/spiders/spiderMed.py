#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:31:57 2019

@author: shailesh
"""

import scrapy


class QuotesSpider(scrapy.Spider):
	name = "medList"
	start_urls = [
	"https://medlineplus.gov/all_healthtopics.html",
	]
	def parse(self, response):
#		page = response.url.split("/")[-2]
#		filename = 'quotes-%s.html' % page
#		with open(filename, 'wb') as f:
#			f.write(response.body)
#		for container in response.css("div.m-srp-card__container"): 
#			print('\n'*10 + 'hello')
#			priceContainer = container.css("div.m-srp-card__info"); 
#			price = priceContainer.css("div.m-srp-card__price::text").get() 
#		#	print(text)
#			
#			descContainer = container.css("div.m-srp-card__desc")
#			title = descContainer.css("span.m-srp-card__title::text").getall()
#			BHK = descContainer.css("span.m-srp-card__title__bhk::text").get()
#			socName = descContainer.css("a.m-srp-card__link::text").get()
#	
#			fieldList = []
#			for summaryContainer in descContainer.css("div.m-srp-card__summary__item"):
#				fieldName = summaryContainer.css("div.m-srp-card__summary__title::text").get()
#				fieldValue = summaryContainer.css("div.m-srp-card__summary__info::text").get()
#				fieldList.append([fieldName,fieldValue])
		
		names = response.css('a::text').getall()
		startInd =names.index('A1C')
#		endInd = names.index('Animal Diseases and Your Health')
		endInd = len(names) - 1 - names[::-1].index('Animal Diseases and Your Health') 
		names = names[startInd:endInd+1]
		
		links = response.css('a::attr(href)').extract()[startInd:]
		startInd =links.index('https://medlineplus.gov/a1c.html')
#		endInd = links.index('https://medlineplus.gov/animaldiseasesandyourhealth.html')
		links = links[startInd:len(names)]
		for i in range(len(names)):
			yield{
						'communityName':names[i],
						'links':links[i],
						
					}
		
		
		