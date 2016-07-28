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

def print_all_links(page):
	while(True):
		url, endpos = get_next_target(page)
		if url:
			print(url)
			page = page[endpos:]
		else:
			break


#print(get_page("http://xkcd.com/353/")) # Test get_page
#print(get_next_target('<li><a href="http://blag.xkcd.com">Blag</a></li>')) #Test get_next_target
#print_all_links('<li><a href="http://blag.xkcd.com">Blag</a></li><li><a href="http://store.xkcd.com/">Store</a></li>') # Test print_all_links
 

print_all_links(get_page('http://xkcd.com/353/'))   
