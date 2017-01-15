def main():

	# load in all apps
	apps=importApps()
	
	#create an applicant and adds to notebook
	for i in apps:
		temp = createApplicant(apps[i])
		Ipython.append(temp)

	#export notebook
	


