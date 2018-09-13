# Web-Programming-Project-1
Names: Shelby Stocker and Jen Lee

References: We used the example code to get us started.
We also used the following links:
http://htmlcolorcodes.com/color-names/
https://stackoverflow.com/questions/5922774/writing-output-of-a-python-script-to-html-with-cgi
https://developer.mozilla.org/en-US/docs/Web/HTML/Element/center 

URL: http://cs.uky.edu/~jmle265/CS316/Project1/alien.html

Description: This project uses a text file that contains various translations
	     of words between different languages. The user enters a word they
	     want to translate, the original language, and the language they want
	     to translate it to, and the program displays the translated word. 

If one of the fields is completely missing, our program prints the whole line in red 
and says invalid.

If the value of a field is blank, our CGI will print invalid in red. 

We did not test our CGI with a client such as curl. 

If one of the field values submitted is a string of 100, 1000, or 10000 characters
our program our program prints them all out. 

We tested this by typing a lot of words in a word document and then copying and 
pasting it multiple times and then copying and pasting it to the inputs in our website.
