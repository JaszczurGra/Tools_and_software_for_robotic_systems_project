#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class VelPublisher(Node):
    def __init__(self):
        super().__init__('velocity_publisher')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.publish_velocity)
        self.vel_msg = Twist()
        self.vel_msg.linear.x = 1.0
        self.vel_msg.linear.y = 0.0
        self.vel_msg.linear.z = 0.0
        self.vel_msg.angular.x = 0.0
        self.vel_msg.angular.y = 0.0
        self.vel_msg.angular.z = 1.0

    def publish_velocity(self):
        self.publisher.publish(self.vel_msg)
        self.get_logger().info('Publishing velocity')

def main(args=None):
    rclpy.init(args=args)
    vel_publisher = VelPublisher()
    rclpy.spin(vel_publisher)
    vel_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
