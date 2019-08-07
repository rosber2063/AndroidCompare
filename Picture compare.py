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
   
   print "Start picture comparing..."
   MonkeyRunner.sleep(3)
   # print "Screenshot:", str(count+1)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data1.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,1.0)):
       print "Pass... 1st Level _ Picture"
   else:
       print "NG... 1st Level _ Picture"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_CENTER') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data2.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,1.0)):
       print "Pass... 2nd Level _ Picture style"
   else:
       print "NG... 2nd Level _ Picture style"
   MonkeyRunner.sleep(5)
    

   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data3.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,1.0)):
       print "Pass... 2nd Level _ Colour"
   else:
       print "NG... 2nd Level _ Colour"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data4.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,1.0)):
       print "Pass... 2nd Level _ Contrast"
   else:
       print "NG... 2nd Level _ Contrast"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data5.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,1.0)):
       print "Pass... 2nd Level _ Sharpness"
   else:
       print "NG... 2nd Level _ Sharpness"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data6.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 2nd Level _ Brightness"
   else:
       print "NG... 2nd Level _ Brightness"
   MonkeyRunner.sleep(3)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data7.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 2nd Level _ Advanced"
   else:
       print "NG... 2nd Level _ Advanced"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_CENTER') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data8.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 3rd Level _ Colour"
   else:
       print "NG... 3rd Level _ Colour"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_CENTER') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data9.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 4th Level _ Colour enhancement"
   else:
       print "NG... 4th Level _ Colour enhancement"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data10.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 4th Level _ Colour temperature"
   else:
       print "NG... 4th Level _ Colour temperature"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data11.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 4th Level _ Custom colour temperature"
   else:
       print "NG... 4th Level _ Custom colour temperature"
   MonkeyRunner.sleep(5)

 
   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data12.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 4th Level _ Colour control"
   else:
       print "NG... 4th Level _ Colour control"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data13.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 4th Level _ RGB only mode"
   else:
       print "NG... 4th Level _ RGB only mode"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_LEFT')
   MonkeyRunner.sleep(3) 
   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data14.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 3rd Level _ Contrast"
   else:
       print "NG... 3rd Level _ Contrast"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_CENTER') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data15.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 4th Level _ Contrast mode"
   else:
       print "NG... 4th Level _ Contrast mode"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data16.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 4th Level _ HDR Upscaling"
   else:
       print "NG... 4th Level _ HDR Upscaling"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data17.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 4th Level _ HDR Plus"
   else:
       print "NG... 4th Level _ HDR Plus"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data18.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 4th Level _ Dynamic contrast"
   else:
       print "NG... 4th Level _ Dynamic contrast"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data19.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 4th Level _ Video contrast"
   else:
       print "NG... 4th Level _ Video contrast"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data20.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 4th Level _ Light sensor"
   else:
       print "NG... 4th Level _ Light sensor"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data21.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 4th Level _ Gamma"
   else:
       print "NG... 4th Level _ Gamma"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_LEFT')
   MonkeyRunner.sleep(3) 
   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data22.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 3rd Level _ Sharpness"
   else:
       print "NG... 3rd Level _ Sharpness"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_CENTER') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data23.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 4th Level _ Ultra resolution"
   else:
       print "NG... 4th Level _ Ultra resolution"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_LEFT')
   MonkeyRunner.sleep(3) 
   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data24.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 3rd Level _ Picture clean"
   else:
       print "NG... 3rd Level _ Picture clean"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_CENTER') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data25.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 4th Level _ Noise reduction"
   else:
       print "NG... 4th Level _ Noise reduction"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data26.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 4th Level _ MPEG artefact reduction"
   else:
       print "NG... 4th Level _ MPEG artefact reduction"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_LEFT')
   MonkeyRunner.sleep(3) 
   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data27.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 3rd Level _ Motion"
   else:
       print "NG... 3rd Level _ Motion"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_CENTER') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data28.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 4th Level _ Motion style"
   else:
       print "NG... 4th Level _ Motion style"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data29.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 4th Level _ Natural motion"
   else:
       print "NG... 4th Level _ Natural motion"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_LEFT')
   MonkeyRunner.sleep(3) 
   device.press('KEYCODE_DPAD_LEFT')
   MonkeyRunner.sleep(3) 
   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data30.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 2nd Level _ Picture format"
   else:
       print "NG... 2nd Level _ Picture format"
   MonkeyRunner.sleep(5)


   device.press('KEYCODE_DPAD_DOWN') 
   MonkeyRunner.sleep(3)

   pic=MonkeyRunner.loadImageFromFile('D:\\Data31.png')
   newpic=device.takeSnapshot()
   if(newpic.sameAs(pic,0.9)):
       print "Pass... 2nd Level _ Quick picture setting"
   else:
       print "NG... 2nd Level _ Quick picture setting"
   MonkeyRunner.sleep(5)

   count += 1
   if count == 1:
      break

MonkeyRunner.sleep(5)
print "Testing Finish !" 
