from tkinter import *

class AuthoriseADB:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.slogan = Button(frame,
                             text="Authorise ADB", bg="orange", fg="black",
                             command=self.write_slogan)
        self.slogan.pack(side=LEFT)
    def write_slogan(self):
        import os
        os.system("adb.exe devices")

class CustomRecovery:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.slogan = Button(frame,
                             text="Flash Custom Recovery", bg="pink", fg="black",
                             command=self.write_slogan)
        self.slogan.pack(side=LEFT)
    def write_slogan(self):
        print("Please type the number that matches the version of twrp you want")
        print("1 - TWRP 2.8.7 Testing Edition")
        print("2 - TWRP 2.8.7 R2")
        print("3 - TWRP 2.8.7 R3")
        print("4 - TWRP 2.8.7 R4")
        print("5 - TWRP 2.8.7 R5")
        print("6 - TWRP 2.8.7 R7")
        print("7 - TWRP 3.4.5 R1")
        ask = input()
        if ask == ("1"):
            import os
            bootloaderwaittwrp = input("please press enter when your device is in bootloader mode")
            os.system("fastboot flash recovery TWRP2.8.7TESTING.img")
            print("Flash Done :-)")
            os.system("fastboot reboot")
        elif ask == ("2"):
            import os
            bootloaderwaittwrp = input("please press enter when your device is in bootloader mode")
            os.system("fastboot flash recovery TWRP2.8.7R2.img")
            print ("Flash Done :-)")
            os.system("fastboot reboot")

        elif ask == ("3"):
            import os
            bootloaderwaittwrp = input("please press enter when your device is in bootloader mode")
            os.system("fastboot flash recovery TWRP2.8.7R3.img")
            print ("Flash Done :-)")
            os.system("fastboot reboot")

        elif ask == ("4"):
            import os
            bootloaderwaittwrp = input("please press enter when your device is in bootloader mode")
            os.system("fastboot flash recovery TWRP2.8.7R4.img")
            print ("Flash Done :-)")
            os.system("fastboot reboot")
        
        elif ask == ("5"):
            import os
            bootloaderwaittwrp = input("please press enter when your device is in bootloader mode")
            os.system("fastboot flash recovery TWRP2.8.7R5.img")
            print ("Flash Done :-)")
            os.system("fastboot reboot")

        elif ask == ("6"):
            import os
            bootloaderwaittwrp = input("please press enter when your device is in bootloader mode")
            os.system("fastboot flash recovery TWRP2.8.7R7.img")
            print ("Flash Done :-)")
            os.system("fastboot reboot")

        elif ask == ("7"):
            import os
            bootloaderwaittwrp = input("please press enter when your device is in bootloader mode")
            os.system("fastboot flash recovery TWRP3.4.5R1.img")
            print ("Flash Done :-)")
            os.system("fastboot reboot")





class LollipopDowngrade:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.slogan = Button(frame,
                             text="Downgrade To Lollipop ", bg="light green", fg="black",
                             command=self.write_slogan)
        self.slogan.pack(side=LEFT)
    def write_slogan(self):
        import os
        print("please move all of the Lollipop firmware files into the moto toolkit directory (the same folder containing toolkit.py)")
        print("")
        ask2 = input("Please make sure usb debugging is turned on in developer settings, then type 'done' into this prompt")
        if ask2 == ("done"):
            import os
            os.system("adb.exe reboot-bootloader")
            bootloaderwait2 = input("Has your device successfully loaded bootloader mode ? please type 'yes' if it has successfully loaded")
            if bootloaderwait2 == ("yes"):
                confirmflash = input("Press enter to confirm you would like to downgrade your device to android marshmallow ;)")
                if confirmflash == (""):
                    import os
                    os.system("@echo off")
                    print("Partition table has been SKIPPED")
                    print("Bootloader has been SKIPPED")
                    os.system("fastboot.exe flash logo logo.bin")
                    print("boot logo has been flashed")
                    os.system("fastboot.exe flash boot boot.img")
                    print("boot.img has been flashed")
                    os.system("fastboot.exe flash recovery recovery.img")
                    print("Stock marshmallow recovery has now been flashed")
                    os.system("fastboot.exe flash system system.img_sparsechunk.0")
                    print("System part 1 has been flashed")
                    os.system("fastboot.exe flash system system.img_sparsechunk.1")
                    print("System part 2 has been flashed")
                    os.system("fastboot.exe flash system system.img_sparsechunk.2")
                    print("System part 3 has been flashed")
                    os.system("fastboot.exe flash system system.img_sparsechunk.3")
                    print("System part 4 has been flashed")
                    os.system("fastboot.exe flash system system.img_sparsechunk.4")
                    print("System part 5 has been flashed")
                    os.system("fastboot.exe flash system system.img_sparsechunk.5")
                    print("System part 6 has been flashed")
                    os.system("fastboot.exe flash system system.img_sparsechunk.6")
                    print("System part 7 has been flashed")
                    print("system partitions successfully flashed")
                    os.system("fastboot.exe flash modem NON-HLOS.bin")
                    print("Flashed Mobile Data Connection Chip Data")
                    os.system("fastboot.exe erase modemst1")
                    os.system("fastboot.exe erase modemst2")
                    print("Old data erased")
                    os.system("fastboot.exe flash fsg fsg.mbn")
                    print("Flashed FSG")
                    os.system("fastboot.exe erase cache")
                    print("cache erased")
                    os.system("fastboot.exe erase userdata")
                    print("userdata partition formatted")
                    os.system("fastboot.exe reboot")
                    print("flash finished")
                    print("Enjoy Lollipop again!")

class LollipopInstall:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.slogan = Button(frame,
                             text="Reinstall Lollipop To My Device", bg="red", fg="black",
                             command=self.write_slogan)
        self.slogan.pack(side=LEFT)
    def write_slogan(self):
        import os
        print("DO NOT USE THIS IF YOUR DEVICE HAS PREVIOUSLY BEEN RUNNING STOCK MARSHMALLOW")
        print("Please use the lollipop downgrade tool instead, so you dont brick your device ")
        print("")
        print("")
        print("please move all of the firmware files into the moto toolkit directory (the same folder containing toolkit.py)")
        print("")
        ask2 = input("Please make sure usb debugging is turned on in developer settings, then type 'done' into this prompt")
        if ask2 == ("done"):
            import os
            os.system("adb.exe reboot-bootloader")
            bootloaderwait2 = input("Has your device successfully loaded bootloader mode ? please type 'yes' if it has successfully loaded")
            if bootloaderwait2 == ("yes"):
                confirmflash = input("Press enter to confirm you would like to reinstall Android Lollipop ;)")
                if confirmflash == (""):
                    import os
                    os.system("@echo off")
                    os.system("fastboot.exe flash partition gpt.bin")
                    print("Partition table has been flashed")
                    os.system("fastboot.exe flash bootloader bootloader.img")
                    print("Bootloader has been flashed")
                    os.system("fastboot.exe flash logo logo.bin")
                    print("boot logo has been flashed")
                    os.system("fastboot.exe flash boot boot.img")
                    print("boot.img has been flashed")
                    os.system("fastboot.exe flash recovery recovery.img")
                    print("Stock marshmallow recovery has now been flashed")
                    os.system("fastboot.exe flash system system.img_sparsechunk.0")
                    print("System part 1 has been flashed")
                    os.system("fastboot.exe flash system system.img_sparsechunk.1")
                    print("System part 2 has been flashed")
                    os.system("fastboot.exe flash system system.img_sparsechunk.2")
                    print("System part 3 has been flashed")
                    os.system("fastboot.exe flash system system.img_sparsechunk.3")
                    print("System part 4 has been flashed")
                    os.system("fastboot.exe flash system system.img_sparsechunk.4")
                    print("System part 5 has been flashed")
                    os.system("fastboot.exe flash system system.img_sparsechunk.5")
                    print("System part 6 has been flashed")
                    os.system("fastboot.exe flash system system.img_sparsechunk.6")
                    print("System part 7 has been flashed")
                    print("system partitions successfully flashed")
                    os.system("fastboot.exe flash modem NON-HLOS.bin")
                    print("Flashed Mobile Data Connection Chip Data")
                    os.system("fastboot.exe erase modemst1")
                    os.system("fastboot.exe erase modemst2")
                    print("Old data erased")
                    os.system("fastboot.exe flash fsg fsg.mbn")
                    print("Flashed FSG")
                    os.system("fastboot.exe erase cache")
                    print("cache erased")
                    os.system("fastboot.exe erase userdata")
                    print("userdata partition formatted")
                    os.system("fastboot.exe reboot")
                    print("flash finished")
                    print("enjoy Lollipop!")

class MarshmallowInstall:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.slogan = Button(frame,
                             text="Flash Android Marshmallow To My Device", bg="light blue", fg="black",
                             command=self.write_slogan)
        self.slogan.pack(side=LEFT)
    def write_slogan(self):
        import os
        print("please move all of the firmware files into the moto toolkit directory (the same folder containing toolkit.py)")
        print("")
        ask2 = input("Please make sure usb debugging is turned on in developer settings, then type 'done' into this prompt")
        if ask2 == ("done"):
            import os
            os.system("adb.exe reboot-bootloader")
            bootloaderwait2 = input("Has your device successfully loaded bootloader mode ? please type 'yes' if it has successfully loaded")
            if bootloaderwait2 == ("yes"):
                confirmflash = input("Press enter to confirm you would like to upgrade/reinstall android marshmallow ;)")
                if confirmflash == (""):
                    import os
                    os.system("@echo off")
                    os.system("fastboot.exe flash partition gpt.bin")
                    print("Partition table has been flashed")
                    os.system("fastboot.exe flash bootloader bootloader.img")
                    print("Bootloader has been flashed")
                    os.system("fastboot.exe flash logo logo.bin")
                    print("boot logo has been flashed")
                    os.system("fastboot.exe flash boot boot.img")
                    print("boot.img has been flashed")
                    os.system("fastboot.exe flash recovery recovery.img")
                    print("Stock marshmallow recovery has now been flashed")
                    os.system("fastboot.exe flash system system.img_sparsechunk.0")
                    print("System part 1 has been flashed")
                    os.system("fastboot.exe flash system system.img_sparsechunk.1")
                    print("System part 2 has been flashed")
                    os.system("fastboot.exe flash system system.img_sparsechunk.2")
                    print("System part 3 has been flashed")
                    os.system("fastboot.exe flash system system.img_sparsechunk.3")
                    print("System part 4 has been flashed")
                    os.system("fastboot.exe flash system system.img_sparsechunk.4")
                    print("System part 5 has been flashed")
                    os.system("fastboot.exe flash system system.img_sparsechunk.5")
                    print("System part 6 has been flashed")
                    os.system("fastboot.exe flash system system.img_sparsechunk.6")
                    print("System part 7 has been flashed")
                    print("system partitions successfully flashed")
                    os.system("fastboot.exe flash modem NON-HLOS.bin")
                    print("Flashed Mobile Data Connection Chip Data")
                    os.system("fastboot.exe erase modemst1")
                    os.system("fastboot.exe erase modemst2")
                    print("Old data erased")
                    os.system("fastboot.exe flash fsg fsg.mbn")
                    print("Flashed FSG")
                    os.system("fastboot.exe erase cache")
                    print("cache erased")
                    os.system("fastboot.exe erase userdata")
                    print("userdata partition formatted")
                    os.system("fastboot.exe reboot")
                    print("flash finished")
                    print("enjoy Marshmallow!")


class Userdata_erase:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.slogan = Button(frame,
                             text="Erase Android userdata", bg="light green", fg="black",
                             command=self.write_slogan)
        self.slogan.pack(side=LEFT)
    def write_slogan(self):
        import os
        confirm3 = input("Please turn on usb debugging in developer settings, then type 'done' here")
        if confirm3 == ("done"):
            os.system("adb.exe reboot-bootloader")
            bootloaderwait5 = input("is your device in bootloader mode? ")
            if bootloaderwait5 == ("yes"):
                os.system("fastboot.exe erase userdata")
                os.system("fastbot.exe reboot")
                print("device userdata wipe done")


class Driver:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.slogan = Button(frame,
                             text="Install Motorola USB Driver", bg="pink", fg="black",
                             command=self.write_slogan)
        self.slogan.pack(side=LEFT)
    def write_slogan(self):
        import os
        os.system("Driver.exe")


class wireless_app_sideload:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.slogan = Button(frame,
                             text="Wireless APK Sideload No Root (BETA)", bg="pink", fg="black",
                             command=self.write_slogan)
        self.slogan.pack(side=LEFT)
    def write_slogan(self):
        print("Welcome to the wireless apk sideloading tool")
        print("This tool will require a bit of setting up, due to the fact it does not require root")
        import os
        adbwait = input("Please turn on usb debugging in your device settings. Please type 'done'.")
        if adbwait == ("done"):
            print("please connect your device to your pc via usb and unlock your device for the set up process")
            print("then accept the adb connect request , and select always allow from this computer")
            print("then press enter when done")
            wait_enter = input("")
            import os
            os.system("adb.exe devices")
            ask123 = input(" press enter to continue \n \n")
            os.system("adb.exe tcpip 5555")
            ip = input("what is the ip adddress of your phone? please type :5555 at the end of the ip address!  ")
            print("")
            print("")
            print("")
            print ("adb.exe connect",ip)
            print("")
            print("")
            print("")
            com1 = input("Please remove the usb of your device and type the above command in this window now   ")
            os.system(com1)
            os.system("pause")
            print("If the above line reads connected to",ip," then you are configured correctly !")
            print("Please put the apk you would like to sideload in the directory that you dowloaded Moto Toolkit in")
            print("make sure the directory you place the app in contains toolkit.py(this program!)")
            print("now rename the apk to app")
            print("so the full filename reads app.apk (including the file extension")
            renamewait = input ("press enter when done !")
            os.system("adb.exe install app.apk")
            print("app sideloading now !")


class RootDevice:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    #packs frame so viewable within app.
    self.slogan = Button(frame,
                         text="Root Your Device(MM)", bg="orange", fg="black",
                         command=self.write_slogan)
                        #defines the design aspects of the button.
    self.slogan.pack(side=LEFT)
  def write_slogan(self):
      import os
      adbask = input("Has adb been authorised ?")
      if adbask == ("yes"):
          adbask = input ("")
          os.system("")
          os.system("adb.exe push mm-root.zip /sdcard/")
          print("Please launch TWRP, and flash mm-root.zip , which should now be found on your phones memory")


class RootDeviceLP:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    #packs frame so viewable within app.
    self.slogan = Button(frame,
                         text="Root Your Device(MM)", bg="orange", fg="black",
                         command=self.write_slogan)
                        #defines the design aspects of the button.
    self.slogan.pack(side=LEFT)
  def write_slogan(self):
      import os
      adbask = input("Has adb been authorised ?")
      if adbask == ("yes"):
          adbask = input ("")
          os.system("")
          os.system("adb.exe push lp-root.zip /sdcard/")
          os.system("adb.exe reboot-bootlaoder")
          print("Please launch TWRP, and flash lp-root.zip , which should now be found on your phones memory")






root = Tk()
root.title("Moto Toolkit Universal Edition")
root.geometry("500x500+200+200")
app = AuthoriseADB(root)
app = CustomRecovery(root)
app = LollipopDowngrade(root)
app = LollipopInstall(root)
app = MarshmallowInstall(root)
app = Userdata_erase(root)
app = Driver(root)
app = wireless_app_sideload(root)
app = RootDevice(root)
app = RootDeviceLP(root)
root.mainloop()


