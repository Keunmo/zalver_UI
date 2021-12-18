import sys
if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    from Tkinter import *
else:
    from tkinter import *
import time
# import Adafruit_ADS1x15
import queue
import threading
 
 
# psd threshold
psd_th = 15000
                
class MyApp:
    def __init__(self):
        self.tk = Tk()
        # fullscreen
        # F11: fullscreen toggle, Esc : exit fullscreen mode 
        self.tk.attributes("-fullscreen", True)
        self.tk.bind("<F11>", lambda event: self.tk.attributes("-fullscreen",
                                    not self.tk.attributes("-fullscreen")))
        self.tk.bind("<Escape>", lambda event: self.tk.attributes("-fullscreen", False))
        #image center position
        self.positionRight = self.tk.winfo_screenwidth()/2 
        self.positionDown = self.tk.winfo_screenheight()/2
        #set image
        self.tk_image1 = PhotoImage(file='/Users/keunmo/Workspace/projects/zalver_UI/imgs/EYES_EMOJI_400px.gif')
        self.tk_image2 = PhotoImage(file='/Users/keunmo/Workspace/projects/zalver_UI/imgs/EYES_EMOJI_400px.gif')
        self.imageNum = 1
        self.label = Label(image=self.tk_image1, bg='black')
        self.label.place(x=self.positionRight,y=self.positionDown,anchor=CENTER)
        #background color
        self.tk.configure(bg='black')
        
    def start_read_psd(self):
        self.q1 = queue.Queue()
        readPsd(self.q1).start()
        self.tk.after(0,self.check_psd)
    
    def changeImage(self):
        if self.imageNum==1 :
            self.imageNum = 2
            self.label.configure(image=self.tk_image2)
            self.label.image = self.tk_image2
        else :
            self.imageNum = 1
            self.label.configure(image=self.tk_image1)
            self.label.image = self.tk_image1
    
    def check_psd(self):
        try:
            value1 = self.q1.get(0)
            print(value1)
            if value1 > psd_th:
                print("over!!")
                self.changeImage()
                time.sleep(0.5)
        except queue.Empty:
            pass
        finally:
            self.tk.after(100,self.check_psd)
            
 
class readPsd(threading.Thread):
    
    def __init__(self,q1):
        threading.Thread.__init__(self)
        self.q1 = q1
        # ads1115(adc) init
        # self.adc = Adafruit_ADS1x15.ADS1115()
        self.abc = 0
        # psd gain
        self.GAIN = 1
        
    def run(self):
        # read psd
        while True:
            time.sleep(0.1)
            # Read all the ADC channel values in a list.
            values = [0]*4
            for i in range(4):
                # Read the specified ADC channel using the previously set gain value.
                values[i] = self.adc.read_adc(i, gain=self.GAIN)
            # put data0 in queue
            self.q1.put(values[0]) 
            
 
root = MyApp()
root.start_read_psd()
root.tk.mainloop()