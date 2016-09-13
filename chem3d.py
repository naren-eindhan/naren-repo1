
#DISPLAYING A 3D SCATTERED VIEW OF MOLECULES


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


pdbfile = raw_input('enter a flie name:')

pdb = open(pdbfile,r)

xc=[];yc=[];zc=[]
xn=[];yn=[];zn=[]
xo=[];yo=[];zo=[]
xh=[];yh=[];zh=[]


while True:
	line = pdb.readline()
	if len(line)==0:
		break

	list1 = line.split()
	
	if list1[-1]=='C':
		xc.append(list1[6]);yc.append(list1[7]);zc.append(list1[8])

	if list1[-1]=='N':
		xn.append(list1[6]);yn.append(list1[7]);zn.append(list1[8])
	
	if list1[-1]=='O':
		xo.append(list1[6]);yo.append(list1[7]);zo.append(list1[8])

	if list1[-1]=='H':
		xh.append(list1[6]);yh.append(list1[7]);zh.append(list1[8])



ax.scatter(xc, yc, zc, c='r', marker='o')
ax.scatter(xn, yn, zn, c='b', marker='o')
ax.scatter(xo, yo, zo, c='g', marker='o')
ax.scatter(xh, yh, zh, c='b', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
