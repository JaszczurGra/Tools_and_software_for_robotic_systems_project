#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Point
from cv_bridge import CvBridge
import cv2
import numpy as np

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.declare_parameter('length', 200)
        self.length = self.get_parameter('length').value
        self.window_name = "camera"
        self.subscription = self.create_subscription(Image,'image_raw',self.listener_callback,10)
        self.subscription
        self.point = None
        self.publisher_ = self.create_publisher(Point, '/point', 10)

    def listener_callback(self, image_data):
        cv_image = np.zeros((512,700,3), np.uint8)
        if(self.point is not None):
            cv2.rectangle(cv_image,self.point,(self.point[0]+self.length,self.point[1]+self.length),(0,255,0),3)
        cv2.imshow(self.window_name,cv_image)
        cv2.waitKey(25)
        cv2.setMouseCallback(self.window_name, self.draw_rectangle)

    def draw_rectangle(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.point = (x,y)
            point_msg = Point()
            point_msg.x = float(x)
            point_msg.y = float(y)
            point_msg.z = 0.0
            self.publisher_.publish(point_msg)

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
