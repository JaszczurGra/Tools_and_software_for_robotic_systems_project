#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class MyNode(Node):
    def __init__(self):
        super().__init__("camera_sub_node")
        self.get_logger().info('Camera node started')
        
        
        self.bridge = CvBridge()
        
    
        self.subscriber_ = self.create_subscription(
            Image, 
            'image_raw', 
            self.listener_callback,
            10
        )
    
    def listener_callback(self, image_data):
        cv_image = self.bridge.imgmsg_to_cv2(image_data, "bgr8")
        cv2.imshow("camera", cv_image)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
