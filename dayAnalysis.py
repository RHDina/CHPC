import numpy as np
import glob #to import the name of all the files in a given directory
import matplotlib.pyplot as pl

DayList=glob.glob("*day.csv")

resultmax=np.array([0,0,0,0]) 
resultmin=np.array([0,0,0,0]) 
resultmean=np.array([0,0,0,0]) 

for day in DayList:
	andro = np.loadtxt(day,delimiter=",",skiprows=1,usecols=(1,2,3,4))
	dimfile = andro.shape # (nb rows,nb cols)
	cols=int(dimfile[1])
	
	allmax = [np.max(andro[:,i]) for i in range(cols)]
	allmin = [np.min(andro[:,i]) for i in range(cols)]
	allmean = [np.mean(andro[:,i]) for i in range(cols)]
	resultmax = np.vstack((resultmax, np.array(allmax)))
	resultmin = np.vstack((resultmin, np.array(allmin)))
	resultmean = np.vstack((resultmean, np.array(allmean)))

np.savetxt("resultmax",resultmax[1:8,:],delimiter=",") 
np.savetxt("resultmin",resultmin[1:8,:],delimiter=",") 
np.savetxt("resultmean",resultmean[1:8,:],delimiter=",") 

smx=resultmean.shape
rx=int(smx[0]) #nb of rows
cx=int(smx[1]) #nb of cols
#print("(rx,cx)",rx,cx)

fig, ax = pl.subplots(nrows=2, ncols=2)

for i in range(cx):
	ii=i+1
	pl.subplot(2, 2, ii)
	tempmin=resultmin[1:rx,i]
	tempmax=resultmax[1:rx,i]
	tempmean=resultmean[1:rx,i]

	xminm=range(len(tempmin)) 
	xmaxm=range(len(tempmax))
	xmean=range(len(tempmean))

	pl.plot(xminm,tempmin,"g-",label="min")
	pl.plot(xmaxm,tempmax,"r-",label="max")
	pl.plot(xmean,tempmean,"b-",label="mean")
	
	pl.legend()
	if i==0:
		pl.title("Temperature")
		pl.ylim(ymax=30,ymin=-10)
	elif i==1:
		pl.title("Pression")
		pl.ylim(ymax=2,ymin=-1)
	elif i==2:
		pl.title("Wind")
		pl.ylim(ymax=30,ymin=-10)
	elif i==3:
		pl.title("Heading")
		pl.ylim(ymax=450,ymin=0)

pl.show()

#============================================================================================
# Another options to read the files
#files=["monday","tuesday","wednesday","thursday","friday"]
#data=[]
#for fname in files:
#	data.append(np.loadtext(fname+".csv",delimiter=",",skiprow=1,usecols=(tuple(range(1,5)))))



