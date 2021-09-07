# numbers
epsilonH=-0.500273
epsilonC=-37.846772
epsilonN=-54.583861
epsilonO=-75.064579
epsilonF=-99.718730
HfH=51.63
HfC=169.98
HfN=112.53
HfO=58.99
HfF=18.47
correctionC=0.25
correctionH=1.01
correctionN=1.04
correctionO=1.04
correctionF=1.05
# cauculate
fanswer=open('answer.txt','w')
for i in range(133885):
	j=i+1
	filename=''
	if (j//100000):
		filename=str(j)
	elif (j//10000):
		filename="0"+str(j)
	elif (j//1000):
		filename="00"+str(j)
	elif (j//100):
		filename="000"+str(j)
	elif (j//10):
		filename="0000"+str(j)
	else :
		filename="00000"+str(j)
	filename='/Users/agubo/Desktop/dsgdb9nsd.xyz/'+"dsgdb9nsd_"+filename+'.xyz'	# in my computer
	f=open(filename,'r')
	lines=f.readlines()
	a=[]
	for line in lines:
		x=line.split()
		a.append(x)
	N=a[0][0]
	Cnumber=0
	Hnumber=0
	Nnumber=0
	Onumber=0
	Fnumber=0
	for k in range(int(N)):
		if a[k+2][0]=='C':
			Cnumber+=1
		elif a[k+2][0]=='H':
			Hnumber+=1
		elif a[k+2][0]=='O':
			Onumber+=1
		elif a[k+2][0]=='N':
			Nnumber+=1
		elif a[k+2][0]=='F':
			Fnumber+=1
	Hf0=(Cnumber*HfC+Hnumber*HfH+Onumber*HfO+Nnumber*HfN+Fnumber*HfF)-627.5095*(Cnumber*epsilonC+Hnumber*epsilonH+Onumber*epsilonO+Nnumber*epsilonN+Fnumber*epsilonF-float(a[1][12]))
	Hf298=Hf0+627.5095*(float(a[1][13])-float(a[1][12]))-(Cnumber*correctionC+Hnumber*correctionH+Onumber*correctionO+Nnumber*correctionN+Fnumber*correctionF)
	fanswer.write('SMILES_{}={} Hf_{}={}\n'.format(j, a[int(N)+3][0], j, Hf298))