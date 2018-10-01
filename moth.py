import os
import sys

argv = sys.argv

switch(len(argv)):

	case 1: 
			idea="|"+argv[1]+"|General|Anonymous|"
			os.system("echo "+idea+">>ideas.md&echo "+idea+">>README.md && echo -e Your idea has been registered!\nThank you for your contribution you can now pull request it.")
	
	
