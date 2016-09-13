import os 
import string


#CREATING A SEPARATE DIRECTORY FOR A GIVEN PDB FILE.
#CREATING TWO FILES WITH NAMES ATOM.TXT AND ANISOU.TXT.

pdbfile = raw_input('Enter a file name:-')

source = pdbfile

target_dir = '/home/naren/chemistry-'+pdbfile
if not os.path.exists(target_dir):

	os.mkdir(target_dir)

f1 = open(target_dir+'/atom.txt','w')
f2 = open(target_dir+'/anisou.txt','w')

pdb = open(source,'r')

while True:
	line1 = pdb.readline()
	if len(line1)==0:
		break
	if line1.startswith('ATOM'):
		f1.write(line1)
	elif line1.startswith('ANISOU'):
		f2.write(line1)
f1.close()
f2.close()
pdb.close()


#DEFINING A FUNCTION WHICH RETURNS A FILE(XYZ.TXT) CONTAINING X Y Z COORDINATES OF MOLECULES.


def extractxyz(chemfile):
	f3=open(chemfile,'r')
	f4=open(target_dir+'/xyz.txt','w')
	while True:
		line2 = f3.readline()
		if len(line2)==0:
			break
		list1=line2.split()
		
		if len(list1)==12:
			temp='x@{}       y@{}       z@{}\n'.format(list1[6],list1[7],list1[8])
			f4.write(temp)
			
	f3.close()
	f4.close()


extractxyz(source)



#CREATING A FILE(INFO.TXT) WHICH GIVES INFORMATION ABOUT NUMBER OF DIFFERENT ATOMS IN THE GIVEN PDB FILE.


x1=0;x2=0;x3=0;x4=0;y1=0;y2=0;y3=0;y4=0

info1 = open(target_dir+'/atom.txt','r')
while True:
	line3 = info1.readline()
	if len(line3)==0:
		break
	list2=line3.split()
	if list2[-1]=='C':
		x1=x1+1
	elif list2[-1]=='N':
		x2=x2+1
	elif list2[-1]=='O':
		x3=x3+1
	elif list2[-1]=='H':
		x4=x4+1
x=x1+x2+x3+x4
info1.close()


info2=open(target_dir+'/anisou.txt','r')
while True:
	line4 = info2.readline()
	if len(line4)==0:
		break
	list3=line4.split()
	if list3[-1]=='C':
		y1=y1+1
	elif list3[-1]=='N':
		y2=y2+1
	elif list3[-1]=='O':
		y3=y3+1
	elif list3[-1]=='H':
		y4=y4+1
y=y1+y2+y3+y4
info2.close()

total =x+y

information='''Total molecules count:{}

ATOM molecules
----------------------
ATOM molecules count:{}
C count:{}
N count:{}
O count:{}
H count:{}


ANISOU molecules
----------------------
ANISOU molecules count:{}
C count:{}
N count:{}
O count:{}
H count:{}'''.format(total,x,x1,x2,x3,x4,y,y1,y2,y3,y4)



info3=open(target_dir+'/info.txt','w')
info3.write(information)
info3.close()


