#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# import glob
import rospy
import os
import cv2
from multiprocessing import Process
import threading
from cv2 import *
from zalver_main.msg import state

behavior = 1

def slideshow():
    
    file_list = os.listdir('/home/ubuntu/catkin_ws/src/rospy_zv/scripts/imgs/')
    img_files = [os.path.join(os.getcwd(), '/home/ubuntu/catkin_ws/src/rospy_zv/scripts/imgs/', file) for file in file_list if file.endswith('.jpg')]
    img_files.sort()
    for f in img_files:
        print(f)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    global behavior 
    while True:
        if behavior == 1:
            print("behavior:1")
            img = cv2.imread(img_files[0])
            img = cv2.resize(img, dsize=(1980, 1060), interpolation=cv2.INTER_LINEAR)
            cv2.imshow('image', img)
            cv2.waitKey(2000)
            img = cv2.imread(img_files[1])
            img = cv2.resize(img, dsize=(1980, 1060), interpolation=cv2.INTER_LINEAR)
            cv2.imshow('image', img)
            cv2.waitKey(30)
            img = cv2.imread(img_files[2])
            img = cv2.resize(img, dsize=(1980, 1060), interpolation=cv2.INTER_LINEAR)
            cv2.imshow('image', img)
            cv2.waitKey(150)
            img = cv2.imread(img_files[1])
            img = cv2.resize(img, dsize=(1980, 1060), interpolation=cv2.INTER_LINEAR)
            cv2.imshow('image', img)
            cv2.waitKey(30)
            img = cv2.imread(img_files[0])
            img = cv2.resize(img, dsize=(1980, 1060), interpolation=cv2.INTER_LINEAR)
            cv2.imshow('image', img)
            
            if cv2.waitKey(300) >= 0:
                break

        elif behavior == 2:
            print("behavior:2")
            img = cv2.imread(img_files[3])
            img = cv2.resize(img, dsize=(1920, 1080), interpolation=cv2.INTER_LINEAR)
            cv2.imshow('image', img)
            cv2.waitKey(500)
            img = cv2.imread(img_files[4])
            img = cv2.resize(img, dsize=(1920, 1080), interpolation=cv2.INTER_LINEAR)
            cv2.imshow('image', img)
            if cv2.waitKey(300) >= 0:
                break

        elif behavior == 3:
            print("behavior:3")
            img = cv2.imread(img_files[5])
            img = cv2.resize(img, dsize=(1920, 1080), interpolation=cv2.INTER_LINEAR)
            cv2.imshow('image', img)
            if cv2.waitKey(15000) >= 0:
                break

        elif behavior == 4:
            print("behavior:4")
            img = cv2.imread(img_files[6])
            img = cv2.resize(img, dsize=(1920, 1080), interpolation=cv2.INTER_LINEAR)
            cv2.imshow('image', img)
            if cv2.waitKey(12000) >= 0:
                break

        elif behavior == 5:
            print("behavior:1")
            img = cv2.imread(img_files[7])
            img = cv2.resize(img, dsize=(1920, 1080), interpolation=cv2.INTER_LINEAR)
            cv2.imshow('image', img)
            if cv2.waitKey(15000) >= 0:
                break
            

    # cv2.destroyAllWindows()

def callback(data):
    # rate = rospy.Rate(40)
    global behavior
    behavior = data.Zalver_State
    print("state-callback", behavior)
    # slideshow(behavior = behavior)



def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/robot_state', state, callback)
    slideshow()
    while not rospy.is_shutdown():
        a = 1
    # rospy.spin()

if __name__ == '__main__':
    '''
    file_list = os.listdir('./imgs')
    img_files = [os.path.join(os.getcwd(), 'imgs', file) for file in file_list if file.endswith('.jpg')]
    img_files.sort()
    for f in img_files:
        print(f)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    '''
    # p1 = Process(target=listener)
    # p2 = Process(target=slideshow)

    listener()
    # p1.start()
    # p2.start()
    
