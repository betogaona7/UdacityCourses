############################################################################################################################################
""" Web crawler, for any seed page, it will find all the pages that can 
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

#Produces a list
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
""" Make a index """
def add_to_index(index,keyword,url):
    if keyword in index:
    	index[keyword].append(url)
    else:
    	index[keyword] = [url]
    return index

def add_page_to_index(index,url,content):
    words = content.split()
    for word in words:
        add_to_index(index,word,url)
    return None
        
def lookup(index, keyword):
	if keyword in index:
		return index[keyword]
	else:
		return None

# Produces a dictionary
#def crawl_web(seed):
#	tocrawl = [seed]
#	crawled = []
#	index = {}
#	while tocrawl:
#		page = tocrawl.pop()
#		if(page not in crawled):
#			content = get_page(page)
#			add_page_to_index(index, page, content)
#			union(tocrawl,get_all_links(content))
#			crawled.append(page)
#	return index

#print all index
print(crawl_web("https://www.udacity.com/cs101x/index.html?_ga=1.161011645.1417601336.1463164125"))
#print all pages with keyword "learning"
print("\n" + str(lookup(crawl_web("https://www.udacity.com/cs101x/index.html?_ga=1.161011645.1417601336.1463164125"),"learning")))

############################################################################################################################################
"""Recusive definition, how to use a recursive definition of popularity to make the search engine 
repond with the best page for a given query. Implementing algorithm of Google."""


#produces a index and a graph
#Graph, is the structure that gives a maping from
#each node to the pages that it links to.
def crawl_web(seed):
	tocrawl = [seed]
	crawled = []
	index = {}
	graph = {}
	while tocrawl:
		page = tocrawl.pop()
		if(page not in crawled):
			content = get_page(page)
			add_page_to_index(index, page, content)
			outlinks = get_all_links(content)
			graph[page] = outlinks
			union(tocrawl,outlinks)
			crawled.append(page)
	return index, graph