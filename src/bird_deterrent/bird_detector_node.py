#!/usr/bin/env python3
import argparse
from pathlib import Path

import cv2
import rclpy
from cv_bridge import CvBridge
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String

import sys

sys.path.append(str(Path('/home/bird_deterrent_system/bird_deterrent_project').resolve()))
from bird_deterrent import BirdDeterrentSystem


class BirdDetectorNode(Node):
    def __init__(self):
        super().__init__('bird_detector_node')
        self.declare_parameter('model_path', '/home/bird_deterrent_system/bird_deterrent_project/yolov8n.pt')
        self.declare_parameter('confidence', 0.5)
        self.declare_parameter('image_topic', '/camera/image_raw')
        self.declare_parameter('output_topic', '/bird_detections')

        model_path = self.get_parameter('model_path').value
        confidence = self.get_parameter('confidence').value
        self.image_topic = self.get_parameter('image_topic').value
        self.output_topic = self.get_parameter('output_topic').value

        if not Path(model_path).exists():
            self.get_logger().error(f'Model file not found: {model_path}')
            raise FileNotFoundError(model_path)

        self.get_logger().info(f'Loading YOLO model from {model_path}')
        self.detector = BirdDeterrentSystem(model_path=model_path, confidence=confidence)
        self.bridge = CvBridge()

        self.subscription = self.create_subscription(Image, self.image_topic, self.image_callback, 10)
        self.publisher = self.create_publisher(String, self.output_topic, 10)
        self.debug_publisher = self.create_publisher(Image, '/bird_detector/debug_image', 10)

    def image_callback(self, msg: Image):
        try:
            frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        except Exception as exc:  # noqa: BLE001
            self.get_logger().warn(f'Could not convert image message: {exc}')
            return

        annotated_frame, detections = self.detector.detect_frame(frame)

        if annotated_frame is not None:
            debug_msg = self.bridge.cv2_to_imgmsg(annotated_frame, encoding='bgr8')
            debug_msg.header = msg.header
            self.debug_publisher.publish(debug_msg)

        if detections:
            payload = {
                'detections': detections,
                'frame_width': frame.shape[1],
                'frame_height': frame.shape[0],
            }
            self.publisher.publish(String(data=str(payload)))
            self.get_logger().info(f'Published {len(detections)} detections')


def main(args=None):
    parser = argparse.ArgumentParser(description='ROS 2 bird detector bridge')
    parser.add_argument('--model', default='/home/bird_deterrent_system/bird_deterrent_project/yolov8n.pt')
    parser.add_argument('--confidence', type=float, default=0.5)
    parser.add_argument('--image-topic', default='/camera/image_raw')
    parser.add_argument('--output-topic', default='/bird_detections')
    parsed, _ = parser.parse_known_args(args)

    rclpy.init(args=args)
    node = BirdDetectorNode()
    node.set_parameters([
        rclpy.parameter.Parameter('model_path', rclpy.Parameter.Type.STRING, parsed.model),
        rclpy.parameter.Parameter('confidence', rclpy.Parameter.Type.DOUBLE, parsed.confidence),
        rclpy.parameter.Parameter('image_topic', rclpy.Parameter.Type.STRING, parsed.image_topic),
        rclpy.parameter.Parameter('output_topic', rclpy.Parameter.Type.STRING, parsed.output_topic),
    ])
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
