import datetime
import time 
from win10toast import ToastNotifier
def getTimeInput(): 
	hour = int(input("Interval hours: ")) 
	minutes = int(input("Interval minutes: ")) 
	seconds = int(input("Interval seconds: ")) 
	time_interval = seconds+(minutes*60)+(hour*3600) 
	return time_interval 

def log(): 
	now = datetime.datetime.now() 
	start_time = now.strftime("%H:%M:%S") 
	with open("WaterDiary.txt", 'a') as f: 
		f.write(f"Drank water: {now}\n") 
	return 0

def notify(): 
	notification = ToastNotifier() 
	notification.show_toast("Time to drink water!") 
	log() 
	return 0

def starttime(time_interval): 
	while True: 
		time.sleep(time_interval) 
		notify() 
if __name__ == '__main__': 
	time_interval = getTimeInput() 
	starttime(time_interval) 
