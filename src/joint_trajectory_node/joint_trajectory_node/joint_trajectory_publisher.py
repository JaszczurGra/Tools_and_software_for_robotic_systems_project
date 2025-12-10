#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

class TrajectoryPublisher(Node):
    def __init__(self):
        super().__init__('trajectory_publisher')
        self.publisher = self.create_publisher(JointTrajectory, 
                                               '/scaled_joint_trajectory_controller/joint_trajectory', 10)
        self.timer = self.create_timer(0.5, self.publish_trajectory)
        self.subscription = self.create_subscription(Point, '/point', 
                                                     self.listener_callback, 10) 
        self.traj_msg = JointTrajectory()
        self.traj_msg.joint_names = ['joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']
        point = JointTrajectoryPoint()
        point.positions = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        point.velocities = [0.0]*6
        point.time_from_start.sec = 1
        point.time_from_start.nanosec = 0
        self.traj_msg.points.append(point)

    def listener_callback(self, point_data):
        point = JointTrajectoryPoint()
        if point_data.y <= 256:
            point.positions = [0.5, 0.0, 0.0, 0.0, 0.0, 0.0]
        else:
            point.positions = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        point.velocities = [0.0]*6
        point.time_from_start.sec = 1
        point.time_from_start.nanosec = 0
        self.traj_msg.points = [point]

    def publish_trajectory(self):
        self.publisher.publish(self.traj_msg)

def main(args=None):
    rclpy.init(args=args)
    traj_publisher = TrajectoryPublisher()
    rclpy.spin(traj_publisher)
    traj_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
