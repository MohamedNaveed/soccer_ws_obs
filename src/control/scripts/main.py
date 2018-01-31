import XBee
from time import sleep

if __name__ == "__main__":
    xbee = XBee.XBee("/dev/ttyUSB0",115200)  # Your serial port name here
    a,b,c,d,e=200,2,3,4,4
    a=str(a)
    b=str(b)
    c=str(c)
    d=str(d)
    e=str(e)
    # A simple string message
    while (1):
    	xbee.SendStr(a+":"+b+":"+c+":"+d+":"+e+":")
    
    	sleep(0.25)	
    #Msg = xbee.Receive()
    #if Msg:
     #?   content = Msg[7:-1].decode('ascii')
       # print("Msg: " + content)

    # A message that requires escaping
    
