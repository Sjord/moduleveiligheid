import sys
import re

num = 0

def make_filename(title):
    global num
    num += 1
    return ("%02d_" % num) + re.sub('[^A-Za-z]', '_', title.strip()) + ".md"

out_file = None
with open(sys.argv[1]) as in_file:
    for line in in_file:
        if line.startswith('# '):
            title = line[2:]
            if out_file:
                out_file.close()

            out_file = open(make_filename(title), 'w')
        if out_file:
            out_file.write(line)
        
out_file.close()
