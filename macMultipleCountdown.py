# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 11:00:24 2020

@author: GiuliaFedrizzi

A timer to alternate work and breaks automatically, without having to start timers when a work session/break is over.
Set how long the work session must be (sessionTime), how long breaks should last (breakTime) and a total number of 
sessions (sum of work sessions and breaks). You'll have an alarm every sessionTime and an alarm after the break is over.
"""
# --- import some useful modules: ---
import time
#import winsound  # to play sounds on Windows machines
import ctypes
import os   
#from pymsgbox import *

# ---  for Windows version: it used to play sounds (not working on Mac)
# duration = 1  # seconds
# freq = 440  # Hz
# os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))


# --- mac version: 
os.system('say "Start"')  # it says 'start' when you start the app
os.system(''' osascript -e 'display dialog "Starting..." buttons {"Ok"} default button "Ok"' ''') # a dialog box appears, press ok to continue


# --- frequencies of sounds: (Windows version)
la = 440  # Hz
si = 494
do = 523

# input - how many minutes? :::: CHANGE THESE VALUES TO CHANGE THE DURATION OF WORK SESSIONS AND BREAKS :::::
sessionTime = 25
breakTime = 5
totnumberOfSessions =  12 # how many sessions, including breaks
workcount = 1     # initial session number (if = 1, the first session will be WORK)
                                         # (if =0, it will start with BREAK)
if totnumberOfSessions % 2==0:           # if it's an even number (even number of work sessions and breaks)
    remainingTime = (sessionTime+breakTime)*totnumberOfSessions/2  # the total number of minutes is given by the number of sessions 
                                                               # times the length of the sessions (including breaks)
else:                        # if odd totnumberOf Sessions (work session != breaks):                   
    if workcount%2==0:     # if it starts with a break
        remainingTime = (sessionTime+breakTime)*(totnumberOfSessions+1)/2  # add 1 to totnumberOfSessions to make it even  
    else:                           
        remainingTime = (sessionTime+breakTime)*(totnumberOfSessions-1)/2+breakTime  # remove one (now it's even) and add breakTime             
seconds=remainingTime*60

def countdown(n): # session countdown
    """ the main function: countdown that takes time in seconds as input
    """
    if workcount % 2 == 1:   # this session is WORK
        print(int(remainingTime/60),'hours and',int(remainingTime % 60),'minutes to go. WORK WORK WORK!!')
        print('Starting session: ',int(sessionTime),'minutes')
#        alert(text='Work!', title='Countdown Over', button='OK')    #ctypes.windll.user32.MessageBoxW(0, "Work! NOW! JUST DO IT!", "Countdown over", 0) # Windows
        os.system(''' osascript -e 'display dialog "Workkkk just do it!" buttons {"Ok"} default button "Ok"' ''')  # dialog box
        #os.system(''' osascript -e 'WORKKKK JUST DO IT" buttons {"Ok"} default button "Ok"' ''')
    else:                   # this session is BREAK
        print('Relax, you deserve this break')
        print('Starting break: '+str(breakTime)+' minutes')
        os.system(''' osascript -e 'display dialog "Sweet break :P" buttons {"Ok"} default button "Ok"' ''')
#        alert(text='Break!', title='Countdown Over', button='OK')      # ctypes.windll.user32.MessageBoxW(0, "Break, YAAASS!", "Countdown over", 0)
        
    # local countdown, inside a session
    while n>0:   # n = local time in seconds, time from start of the session
        time.sleep(1)
        if n % 60 == 0:
            mins=n/60
            print(int(mins),'minutes to go in this session.')  # displays the remaining minutes, every minute on the minute
        n-= 1     # one less second
    if n==0:    # no more seconds
        print('Countdown over!')

# ---- execute function ----------
while workcount <= totnumberOfSessions:    # if there are still sessions scheduled 
    if workcount % 2 == 1:   # if workcount is odd =>  time to work
                             # if workcount is even => time to take a break     
        seconds = sessionTime*60
        # --------------------------------------------------------- 
        countdown(seconds)   # here is where we RUN COUNTDOWN for WORK time
        # -------------------------------------------------------------
        remainingTime=remainingTime - sessionTime # after working, subtract working session time
        
    else:
        seconds = breakTime*60
        print('Break time!')
        # --------------------------------------------------------- 
        countdown(seconds)   # here is where we RUN COUNTDOWN for BREAK time
        # -------------------------------------------------------------
        remainingTime=remainingTime - breakTime # after pausing, subtract break time
    
    print('Remaining time: ',remainingTime)
   
    # play a sound *beepTimes* times WINDOWS
    # say that it's time to work/take a break
    if workcount % 2 == 1:   # if workcount is odd => finished working
        os.system('say "Break time."')    
        #winsound.Beep(do, duration) # plays C
        #winsound.Beep(la, duration) # plays A       
    else:                   # workcount is even => break is over
        os.system('say "Work time."')
        #winsound.Beep(la, duration) # plays A (Windows)
        #winsound.Beep(do, duration) # plays C
#        beepTimes = 1
#        while beepTimes > 0:
#            winsound.Beep(la, duration)
#            beepTimes -= 1

    print('Finished session number (including breaks) ',workcount)
    workcount = workcount+1 # increases counts the sessions: odd = work, even = break
# ctypes.windll.user32.MessageBoxW(0, "Time's up! You're a free elf *.*", "No more time left", 0)
