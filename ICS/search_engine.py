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

""" Three main issues with scaling up a web crawler
- One is the normal politeness that you need on the web
- How you get a bunch of machines involved in crawling not just one
- How to consume a lot of bandwith so that you keep the expensive resources busy, while still being polite """

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

def compute_ranks(graph):
    d = 0.8 # damping factor, probabilty
    numloops = 10
    
    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages
    
    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                	newrank = newrank+d*(ranks[node]/len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks

def lucky_search(index, ranks, keyword):
	pages = lookup(index, keyword)
	if not pages:
		return None 
	best_page = pages[0]
	for candidate in pages:
		if ranks[candidate] > ranks[best_page]:
			best_page = candidate
	return best_page


#print all index
#print(crawl_web("https://www.udacity.com/cs101x/index.html?_ga=1.161011645.1417601336.1463164125"))
#print all pages with keyword "learning"
#print("\n" + str(lookup(crawl_web("https://www.udacity.com/cs101x/index.html?_ga=1.161011645.1417601336.1463164125"),"learning")))

#Output: Highest Rating page with keyword 
index, graph = crawl_web("https://www.udacity.com/cs101x/index.html?_ga=1.161011645.1417601336.1463164125")
ranks = compute_ranks(graph)

print (lucky_search(index, ranks, "learning"))
