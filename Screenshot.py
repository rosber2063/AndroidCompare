# Imports the monkeyrunner modules used by this program
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
import commands
import sys

print "Start Test!"  

# Connects to the current device, returning a MonkeyDevice object
#MonkeyRunner.waitForConnection()
device = MonkeyRunner.waitForConnection() 

try:
        device.wake()
except java.lang.NullPointerException, e:
        print >> sys.stderr, "%s: ERROR: Couldn't connect to %s: %s" % (progname, serialno, e)
        sys.exit(3)

# if not device:
   # print "Please connect a device to start!"
# else:
   # print "Device connected!"

# Runs the component
device.startActivity(component="org.droidtv.settings/.setupmenu.SetupMenuActivity")
MonkeyRunner.sleep(3)

# Presses the key event
count = 0
while count <= 1:
   
   print "Start Screenshot"
   MonkeyRunner.sleep(3)
   # print "Screenshot:", str(count+1)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data1.png','png')
   print "Take ScreenShot 1... 1st Level _ Picture"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_CENTER') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data2.png','png')
   print "Take ScreenShot 2... 2nd Level _ Picture style"
   MonkeyRunner.sleep(10)
    

   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data3.png','png')
   print "Take ScreenShot 3... 2nd Level _ Colour"
   MonkeyRunner.sleep(6)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data4.png','png')
   print "Take ScreenShot 4... 2nd Level _ Contrast"
   MonkeyRunner.sleep(6)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data5.png','png')
   print "Take ScreenShot 5... 2nd Level _ Sharpness"
   MonkeyRunner.sleep(10)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data6.png','png')
   print "Take ScreenShot 6... 2nd Level _ Brightness"
   MonkeyRunner.sleep(6)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data7.png','png')
   print "Take ScreenShot 7... 2nd Level _ Advanced"
   MonkeyRunner.sleep(4)


   device.press('KEYCODE_DPAD_CENTER') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data8.png','png')
   print "Take ScreenShot 8... 3rd Level _ Colour"
   MonkeyRunner.sleep(4)


   device.press('KEYCODE_DPAD_CENTER') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data9.png','png')
   print "Take ScreenShot 9... 4th Level _ Colour enhancement"
   MonkeyRunner.sleep(6)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data10.png','png')
   print "Take ScreenShot 10... 4th Level _ Colour temperature"
   MonkeyRunner.sleep(6)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data11.png','png')
   print "Take ScreenShot 11... 4th Level _ Custom colour temperature"
   MonkeyRunner.sleep(4)

 
   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data12.png','png')
   print "Take ScreenShot 12... 4th Level _ Colour control"
   MonkeyRunner.sleep(4)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data13.png','png')
   print "Take ScreenShot 13... 4th Level _ RGB only mode"
   MonkeyRunner.sleep(4)


   device.press('KEYCODE_DPAD_LEFT')
   MonkeyRunner.sleep(3) 
   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data14.png','png')
   print "Take ScreenShot 14... 3rd Level _ Contrast"
   MonkeyRunner.sleep(4)


   device.press('KEYCODE_DPAD_CENTER') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data15.png','png')
   print "Take ScreenShot 15... 4th Level _ Contrast mode"
   MonkeyRunner.sleep(4)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data16.png','png')
   print "Take ScreenShot 16... 4th Level _ HDR Upscaling"
   MonkeyRunner.sleep(4)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data17.png','png')
   print "Take ScreenShot 17... 4th Level _ HDR Plus"
   MonkeyRunner.sleep(4)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data18.png','png')
   print "Take ScreenShot 18... 4th Level _ Dynamic contrast"
   MonkeyRunner.sleep(6)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data19.png','png')
   print "Take ScreenShot 19... 4th Level _ Video contrast"
   MonkeyRunner.sleep(6)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data20.png','png')
   print "Take ScreenShot 20... 4th Level _ Light sensor"
   MonkeyRunner.sleep(6)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data21.png','png')
   print "Take ScreenShot 21... 4th Level _ Gamma"
   MonkeyRunner.sleep(4)


   device.press('KEYCODE_DPAD_LEFT')
   MonkeyRunner.sleep(3) 
   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data22.png','png')
   print "Take ScreenShot 22... 3rd Level _ Sharpness"
   MonkeyRunner.sleep(4)


   device.press('KEYCODE_DPAD_CENTER') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data23.png','png')
   print "Take ScreenShot 23... 4th Level _ Ultra resolution"
   MonkeyRunner.sleep(6)


   device.press('KEYCODE_DPAD_LEFT')
   MonkeyRunner.sleep(3) 
   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data24.png','png')
   print "Take ScreenShot 24... 3rd Level _ Picture clean"
   MonkeyRunner.sleep(4)


   device.press('KEYCODE_DPAD_CENTER') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data25.png','png')
   print "Take ScreenShot 25... 4th Level _ Noise reduction"
   MonkeyRunner.sleep(6)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data26.png','png')
   print "Take ScreenShot 26... 4th Level _ MPEG artefact reduction"
   MonkeyRunner.sleep(6)


   device.press('KEYCODE_DPAD_LEFT')
   MonkeyRunner.sleep(3) 
   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data27.png','png')
   print "Take ScreenShot 27... 3rd Level _ Motion"
   MonkeyRunner.sleep(4)


   device.press('KEYCODE_DPAD_CENTER') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data28.png','png')
   print "Take ScreenShot 28... 4th Level _ Motion style"
   MonkeyRunner.sleep(4)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data29.png','png')
   print "Take ScreenShot 29... 4th Level _ Natural motion"
   MonkeyRunner.sleep(6)


   device.press('KEYCODE_DPAD_LEFT')
   MonkeyRunner.sleep(3) 
   device.press('KEYCODE_DPAD_LEFT')
   MonkeyRunner.sleep(3) 
   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data30.png','png')
   print "Take ScreenShot 30... 2nd Level _ Picture format"
   MonkeyRunner.sleep(4)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   # Takes a screenshot
   result = device.takeSnapshot()
   # Writes the screenshot to a file
   result.writeToFile('D:\\Data31.png','png')
   print "Take ScreenShot 31... 2nd Level _ Quick picture setting"
   MonkeyRunner.sleep(4)

   count += 1
   if count == 1:
      break

MonkeyRunner.sleep(5)
print "Testing Finish !" 
