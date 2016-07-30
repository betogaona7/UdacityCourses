############################################################################################################################################
"""Web crawler, for any seed page, it will find all the pages that can 
be reached from that page, and return them in a list"""

def get_page(url):
	try:
		import urllib.request
		return str(urllib.request.urlopen(url).read())
	except:
		return "Error"

def get_next_target(page):
	start_link = page.find("<a href=")
	if(start_link == -1):
		return None, 0
	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote+1)
	url = page[start_quote+1:end_quote]
	return url, end_quote

def union(list_one,list_two):
	for element in list_two:
		if(element not in list_one):
			list_one.append(element)

def get_all_links(page):
	links = []
	while(True):
		url, endpos = get_next_target(page)
		if url:
			links.append(url)
			page = page[endpos:]
		else:
			break
	return links

#def crawl_web(seed):
#	tocrawl = [seed]
#	crawled = []
#	while tocrawl:
#		page = tocrawl.pop()
#		if(page not in crawled):
#			union(tocrawl,get_all_links(get_page(page)))
#			crawled.append(page)
#	return crawled

############################################################################################################################################
""" AMake a index """
def add_to_index(index,keyword,url):
    for element in index:
        if keyword in element[0]:
            element[1].append(url)
            return index
    index.append([keyword,[url]])
    return index

def add_page_to_index(index,url,content):
    words = content.split()
    for word in words:
        add_to_index(index,word,url)
    return None
        
def lookup(index, word):
	for element in index:
		if keyword in element[0]:
			return element[1]
	return []

def crawl_web(seed):
	tocrawl = [seed]
	crawled = []
	index = []
	while tocrawl:
		page = tocrawl.pop()
		if(page not in crawled):
			content = get_page(page)
			add_page_to_index(index, page, content)
			union(tocrawl,get_all_links(content))
			crawled.append(page)
	return index


print(crawl_web("https://www.udacity.com/cs101x/index.html?_ga=1.161011645.1417601336.1463164125"))