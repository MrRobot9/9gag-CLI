from __future__ import print_function
from api import *
from parser import *
from utils import *
import getpass
import title9gag





if __name__ == "__main__":
    title9gag.print_9gag()
    number_of_pages = int(raw_input("Enter number the of pages you want to browse:"))
    posts = get_posts_from_page(number_of_pages =number_of_pages)
    for post in posts:
    	for i in range(0, get_terminal_width()):
    		print("*", end="")
    	print(post['title'])
    	if post['type']=='Image':
    		img_parse(post['media_url'], True)


	
	
    	