#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
import cv2
import sys
from cv_bridge import CvBridge
from darknet_ros_msgs.msg import BoundingBoxes
from darknet_ros_msgs.msg import BoundingBox 
from std_msgs.msg import Int32
#from sensor_msgs.msg import Image

pub_1 = rospy.Publisher('max_bbox', BoundingBox, queue_size=10)
pub_2 = rospy.Publisher('num_person', Int32, queue_size=10)


# rate = rospy.Rate(30)
# pub_msg = Int32()

def callback(data):
    # initalize
    rate = rospy.Rate(40) # pub rate
    # find max bbox
    bboxes = data.bounding_boxes
    # bbox_0_xmin = boundingboxes[0].xmin
    # bbox_num = len(BoundingBoxes)
    area = []
    bbox = []
    # print("num person",len(bboxes))
    for i in range(len(bboxes)):
        if bboxes[i].id == 0:
            area.append((bboxes[i].xmax-bboxes[i].xmin)*(bboxes[i].ymax-bboxes[i].ymin))
            bbox.append(bboxes[i])
        if len(bbox) > 0:
            max_idx = area.index(max(area))
            max_bbox = bbox[max_idx]
            print("num person", len(bbox))
            print("max person",max_bbox)
            pub_1.publish(max_bbox)
            pub_2.publish(len(bbox))

    # img processing
    # bridge = CvBridge()
    # cv_image = bridge.imgmsg_to_cv2(sensor_msgs/Image, desired_encoding='passthrough')
    # cv2.imshow('test', frame)
    # bbox_img = cv_image[max_bbox.ymin: max_bbox.ymax, max_bbox.xmin: max_bbox.xmax]
    # print(bbox_img[0])
    # cv2.imshow('test', bbox_img)
    
    # key = cv2.waitKey(1)
    # if key == ord('q'):
    #     cv2.destroyAllWindows()
    #     sys.exit(0)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/darknet_ros/bounding_boxes', BoundingBoxes, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

