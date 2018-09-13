#!/usr/bin/python
import cgi
import cgitb
# Authors: Shelby Stocker and Jen Lee
# Note - not "proper" HTML - shortens the example code! - pjl

def translate(theword, fromnative, newlanguage):
    text = open("xarn_language.txt", "r")
    found = False
    for line in text:
	language1, word1, language2, word2 = line.split(',')
    	if (theword in line and fromnative in line and newlanguage in line):
		if fromnative == newlanguage:
			return theword
		elif theword == word1:
			return word2
		else:
   			return word1
		found = True
    if found == False:
    	return "unknown"
    text.close()

def main():
    print "Content-type:text/html\n\n"
    cgitb.enable()
    form = cgi.FieldStorage()
    if (form.getvalue('fromnative') == None) :
	First = "invalid"
	print '<font color = "red">Origin Language:', First, "</font><br>"    
    else:
	First = (form.getvalue('fromnative')).lower()
	print '<font color = "blue">Origin Language: </font>', First, "<br>"
    if (form.getvalue('newlanguage') == None) :
	Middle = "invalid"
	print '<font color = "red">Requested Language:', Middle, "</font><br>"
    else: 
	Middle = (form.getvalue('newlanguage')).lower()
	print '<font color = "blue">Requested Language: </font>', Middle, "<br>"
    if (form.getvalue('theword') == None) :
	Last = "invalid"
	print '<font color = "red">Original Word:', Last, "</font><br>"
    else:
	Last = (form.getvalue('theword')).lower()
	print '<font color = "blue">Original Word: </font>', Last, "<br>"
    output = translate(Last, Middle, First)
    if (output == "unknown"):
	print '<font color = "red"> Translation: unknown' "</font>"
    else :
	print '<font color = "blue"> Translation:', '<font color = "green">', output, "</font>"  
if __name__ == "__main__":
    main()
