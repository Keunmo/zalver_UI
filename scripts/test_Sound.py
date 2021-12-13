#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# import glob
import rospy
import os
#import cv2
import pygame
import time
#from multiprocessing import Process
#import threading
from cv2 import *
from zalver_main.msg import state
import playsound



#pygame.init()
behavior = 1
sound_state = False


playsound.playsound('/home/ubuntu/catkin_ws/src/rospy_zv/scripts/sounds/1ment.ogg')
playsound.playsound('/home/ubuntu/catkin_ws/src/rospy_zv/scripts/sounds/8bit_Music.ogg')




'''
pygame.mixer.init()
s = pygame.mixer.Sound('/home/ubuntu/catkin_ws/src/rospy_zv/scripts/sounds/1ment.ogg')

while True:
    s.play()
    time.sleep(10.0)


def soundplayer():
    
    sound_list = os.listdir('/home/ubuntu/catkin_ws/src/rospy_zv/scripts/sounds/')
    sound_files = [os.path.join(os.getcwd(), '/home/ubuntu/catkin_ws/src/rospy_zv/scripts/sounds/', file) for file in sound_list if file.endswith('.ogg')]
    sound_files.sort()
    for f in sound_files:
        print(f)
   
    pygame.mixer.init()
    test_sound = pygame.mixer.Sound('/home/ubuntu/catkin_ws/src/rospy_zv/scripts/sounds/8bit_Music.ogg')
    test_sound.play()
   
    
    global behavior 
    global sound_state
    while True:
        if behavior == 1:
            print("behavior:1")
            break

        elif behavior == 2:
            if sound_state == False:
                sound_state = 1
                print("behavior:2")
                pygame.mixer.init()
                pygame.mixer.music.load(sound_files[0])
                pygame.mixer.play(-1)
                time.sleep(2)
                pygame.mixer.init()
                pygame.mixer.music.load(sound_files[1])
                pygame.mixer.play(-1)
                break
            else :
                                
                break

        elif behavior == 3:
            print("behavior:3")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_files[2])
            pygame.mixer.play(-1)
            break

        elif behavior == 4:
            print("behavior:4")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_files[3])
            pygame.mixer.play(-1)
            break
            
        elif behavior == 5:
            print("behavior:1")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_files[4])
            pygame.mixer.play(-1)
            time.sleep(8)
            pygame.mixer.init()
            pygame.mixer.music.load(sound_files[5])
            pygame.mixer.play(-1)
            break
            

    # cv2.destroyAllWindows()

def callback(data):
    # rate = rospy.Rate(40)
    global behavior
    behavior = data.Zalver_State
    # print("state-callback", behavior)




def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/robot_state', state, callback)
    # soundplayer()
    
    sound_list = os.listdir('/home/ubuntu/catkin_ws/src/rospy_zv/scripts/sounds/')
    sound_files = [os.path.join(os.getcwd(), '/home/ubuntu/catkin_ws/src/rospy_zv/scripts/sounds/', file) for file in sound_list if file.endswith('.ogg')]
    sound_files.sort()
    for f in sound_files:
        print(f)
   
    pygame.mixer.init()
    test_sound = pygame.mixer.Sound('/home/ubuntu/catkin_ws/src/rospy_zv/scripts/sounds/8bit_Music.ogg')
    test_sound.play()
    
    while not rospy.is_shutdown():
        a = 1


if __name__ == '__main__':
    listener()
    
    '''
    
    
    
