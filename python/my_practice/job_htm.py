
import re
import sys

line_list = []
HEADER = '<html><body><table>'
FOOTER = '</table></body></html>'

print(sys.argv[1])
f=open(sys.argv[1], 'rt')

for line in f:
	"""print(line)"""
	line = line.replace("/var/www/html/job/","")
	fields = re.split("\t",line)
	line_list.append(fields)
f.close()

fo=open(sys.argv[2], 'wt')
fo.write(HEADER)
for fields in line_list:
	length = len(fields)
	line = '<tr><td>'
	if length == 7:
		line += fields[0] + '</td><td>' + fields[1] + '</td><td>' + fields[2] + '</td><td>' + fields[3] + '</td><td>' + '<a href="' + fields[5] + '">' + fields[4] + '<a></td></tr>'
	else:
		line += fields[0] + '</td><td>' + fields[1] + '</td><td>' + fields[2] + '</td><td>' + '<a href="' + fields[4] + '">' + fields[3] + '<a></td></tr>'
	fo.write(line)
fo.write(FOOTER)
fo.close