#David Tsang
#30 Jul 2019
#This Python 3.7 program find and replace binary value in mrf file.
#Compiled by using pyinstaller

import sys

authorName = "David Tsang"
markDate = "30 Jul 2019"
contact = "https://github.com/DavidTsangHW"

programDesc = authorName + '\n' + markDate 
programDesc = programDesc + '\n' + contact + '\n\n'
programDesc = programDesc + 'This Python 3.7 program find and replace binary value in mrf file.\n'


def formatValue(val):
    l = len(val)
    r = ''

    for i in range(0, l):
        r = r + val[i] + '\x00'

    return r

argv = sys.argv

if len(argv)>1:
    sfname = argv[1]
    ofname = argv[2]
    v1 = argv[3]
    v2 = argv[4]
else:
    print(programDesc)
    print("Usage: editmrf.exe [source.mrf] [output.mrf] [original value] [replace value]")
    exit(0)

f=open(sfname,"rb")
s= f.read()
f.close()

v1 = formatValue(v1)
v2 = formatValue(v2)

bv1 = v1.encode()
bv2 = v2.encode()

s=s.replace(bv1,bv2)

ofile =open(ofname,mode="wb")
ofile.write(s)
ofile.close()

print(ofname + " created")



    







