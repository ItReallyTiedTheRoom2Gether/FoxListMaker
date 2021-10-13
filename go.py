#!/usr/bin/env python3
import csv
import os
import time

#Reset the terminal
os.system("reset")

#Remove all *.source and *.html files
try:
	os.system("rm *.html >/dev/null 2>&1 && rm -r buildfolder >/dev/null 2>&1 ")
except:
	pass

#This function adds the HTML header from 'top.source' to an open file
def add_top_html(output_file):
	file_to_copy = open("top.source","r")
	for line in file_to_copy:
		output_file.write(line)
	file_to_copy.close()
	return;
	
#This function adds the HTML footer from 'bottom.source' to an open file
def add_bottom_html(output_file):
	file_to_copy = open("bottom.source","r")
	for line in file_to_copy:
		output_file.write(line)
	file_to_copy.close()

tag_list = []
alphabet_tags = 1 # Set this to '1' if you want the list of tags to be alphabetized. Otherwise, leave it at '0'. The sort happens on line 42!
	
source_file = open("source.txt","r")
delimit_source_file = csv.reader(source_file,delimiter=",")

# This block of code builds the list of tags to use as an index
for line in delimit_source_file:
	line_tags = line[3]
	line_tags = line[3].split("+")	# Break up the list of tags using the '+' sign. It's now a list of items, rather than a single string.
	for x in line_tags: # This nested loop checks to see if the current tag already exists in the tag_list
		tag_found = 0 # Boolean variable which is changed to '1' ('true') if the tag already exists in the tag list
		for y in tag_list:
			if(x==y):
				tag_found = 1
			else:
				pass
		if(tag_found==0): # If the tag was not found in the tag_list
			tag_list.append(x) # Add it to the tag_list
		else:
			pass
		
source_file.close() # The source file can now be closed as it's not needed right now.

if(alphabet_tags==0):
	pass
else:
	tag_list.sort()	# Sort the tag list alphabetically

print("Tags found in source file:\n"+str(tag_list))

# Start building the individual HTML files for each tag!
for x in tag_list:
	output_file = x+".html"
	output_file = open(output_file,"w")
	add_top_html(output_file)
	output_file.write("<a href=\"index.html\">&lt;&lt; Go Back</a><br />")
	source_file = open("source.txt","r") # Now we will start to find each relevant entry that should be included in this tag's HTML file
	delimit_source_file = csv.reader(source_file,delimiter=",")
	for line in delimit_source_file:
		line_tags = line[3]
		line_tags = line_tags.split("+")
		tags_for_html = line_tags
		for y in line_tags:
			if(y==x):
				output_file.write("<h1>"+line[0]+"</h1>"+line[4]+" ")
				print(line[1][0:8])
				if (line[1][0:8]=="pagelink"):
					output_file.write("<a href=\""+line[1][9:]+".html\">Read item</a>.")
				output_file.write("<br />Tags: ")
				for i in line_tags:
					output_file.write(i+" ")
				output_file.write("<hr /><br />")
			else:
				pass
	source_file.close()
	output_file.write("\n") # This line just adds a newline character before we start to write the footer
	output_file.write("<a href=\"index.html\">&lt;&lt; Go Back</a><br />")
	add_bottom_html(output_file)
	output_file.close()

# Start building the index file
output_file = open("index.html","w")
add_top_html(output_file)
for x in tag_list:
	output_file.write("<a href=\""+x+".html\">"+x+"</a><br />")
add_bottom_html(output_file)
