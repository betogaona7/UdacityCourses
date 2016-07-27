
'''Break time. The program starts to keep track of time and after every two hours of work 
on the computer it opens a browser to play your friend's favorite song, After another two 
hours of work, it prompts you to take another break and so on.'''

import webbrowser 
import time

total_breaks = 3
break_count = 0

print("This program started on " + time.ctime())
while(break_count <  total_breaks):
	time.sleep(2*60*60) 
	webbrowser.open("https://www.youtube.com/watch?v=RjCGgAiRzdg")
	break_count = break_count + 1