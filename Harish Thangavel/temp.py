                import random
                import time
                while True:
	   temp=random.randint(0,70)
	   humd=random.randint(10,60)
	   if temp > 50 and humd < 20:
                print("Temperature=",temp,end=" ")
	   print("Humidity=",humd,"#########ALARM ON#######")
	   time.sleep(3)
	   else:
                 print("Temperature=",temp,end=" ")
       	    print("Humidity=",humd)
	    time.sleep(1)
