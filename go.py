#!/usr/bin/env python3
import csv
import os
import time

os.system("rm *.html")

#Initializing script variables

line_title, line_page_number, line_image, line_tags, current_tag = "", "", "", "", ""

source_file_list	=	[]

#HTML Meta Data
title_tag	=	"Insert the title content which will appear for your website here"
description_tag	=	"Insert the description content which will appear for your website here"

in_file	=	open("source.txt","r")
delimit_in_file	= csv.reader(in_file,delimiter=",")

working_directory	=	os.getcwd()
print("Working directory is "+working_directory)

## This for loop takes the data provided in the index and separates it out into separate text files with the extension "*.source"

for line in delimit_in_file:
	line_title	=	line[0]
	line_page_number = line[1]
	line_image	=	line[2]
	line_tags	=	line[3]
	
	line_tags	=	line_tags.split("+")	#	Break the tags up using the 'plus' sign
	no_of_tags	=	0
	no_of_tags	=	len(line_tags)			#	Count the number of tags used
	current_tag_count	=	0						#	Counter variable for iterating through tags
	
	while(current_tag_count<no_of_tags):
		current_tag	=	line_tags[current_tag_count]
		out_file	=	open((current_tag+".source"),"a")	#	Start building the source files for each of the tags
		
		out_file.write(line_title+","+line_page_number+","+line_image)	# Add to the tag's source file each of the necessary items	
		out_file.write("\n")
		out_file.close()
		
		current_tag_count	+=	1
		
in_file.close()

for file in os.listdir(working_directory):
	if file.endswith(".source"):
		source_file_list.append(file)

for x in source_file_list:
	current_tag	=	x
	output_file	=	x
	output_file	=	((output_file[:-7])+".html")
	output_file	=	open(output_file,"w")
	
	# Quick note: Credit for this HTML template goes to https://www.sitepoint.com/a-basic-html5-template/
	
	output_file.write("<!doctype html>\n\n")
	output_file.write("<html lang=\"en\">\n")
	output_file.write("<head>\n")
	output_file.write("\t<meta charset=\"utf-8\">\n")
	output_file.write("\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n\n")
	output_file.write("\t<title>Tag: "+x[:-7]+"</title>\n\n")
	
	output_file.write("\t<meta property=\"og:title\" content=\""+title_tag+"\">\n")
	output_file.write("\t<meta property=\"og:type\" content=\"website\">\n")
	output_file.write("\t<meta property=\"og:description\" content=\""+description_tag+"\">\n\n")
	
	output_file.write("\t<link rel=\"icon\" href=\"/favicon.ico\">\n")
	output_file.write("\t<link rel=\"icon\" href=\"/favicon.svg\" type=\"image/svg+xml\">\n\n")

	output_file.write("\t<link rel=\"stylesheet\" href=\"style.css\">\n\n")
	
	output_file.write("</head>\n\n")
	output_file.write("<body>\n\n")
	
	in_file	=	open("source.txt","r")
	delimit_in_file	=	csv.reader(in_file,delimiter=",")
	for line in delimit_in_file:
		current_line_tags	=	line[3].split("+")
		for i in current_line_tags:
			if(x[:-7]==i):
				output_file.write("\t<div class=\"newentry\">\n<span class=\"header\">")
				output_file.write(line[0])
				output_file.write("</span><br />")
				output_file.write(line[4])
				output_file.write("</div>\n")
				output_file.write("<br />")
	in_file.close()
	
	output_file.write("</body>\n")
	output_file.write("</html>\n")
	
	
	output_file.close()

os.system("rm *.source")	#	Remove all source files
