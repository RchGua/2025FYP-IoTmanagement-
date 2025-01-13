inside makeJSON

{class makeJSON} contain 8 method. They are for creating a JSON to Create and Update data in database:
speaker()	
user()		
th()	        	#for temperature and humidity sensor 
wl()		        #for waterleak sensor
hm()	         	#for human motion sensor
charger()
panel()
linkage()

{class CreateAndUpdate} contains 3 method:
buildAcharger()	#it create a charger in database witch links with sensors
updatePower()  	#for control the on and off of device through web or app. #it updates panel and device data
updateCharger() #for update the current status of devices and sensors(not finished)

{class Read} has one method for now:
powerstatus()	  #only checks the power of charger for now
