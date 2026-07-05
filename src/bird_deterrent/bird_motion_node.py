#!/usr/bin/env python3
import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node


class BirdMotionNode(Node):
    def __init__(self):
        super().__init__('bird_motion_node')
        self.publisher_ = self.create_publisher(Twist, '/bird_model/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.start_time = self.get_clock().now().nanoseconds / 1e9
        self.get_logger().info('Bird motion node started')

    def timer_callback(self):
        elapsed = self.get_clock().now().nanoseconds / 1e9 - self.start_time
        twist = Twist()

        if elapsed < 8.0:
            twist.linear.x = 0.8
            twist.angular.z = 0.18
        elif elapsed < 16.0:
            twist.linear.x = 0.8
            twist.angular.z = -0.18
        else:
            twist.linear.x = 0.6
            twist.angular.z = 0.0
            self.start_time = self.get_clock().now().nanoseconds / 1e9

        self.publisher_.publish(twist)


def main(args=None):
    rclpy.init(args=args)
    node = BirdMotionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
