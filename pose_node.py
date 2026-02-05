import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
from ultralytics import YOLO

class PoseEstimationNode(Node):

    def __init__(self):
        super().__init__('pose_estimation_node')

        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10
        )

        self.publisher = self.create_publisher(
    String,
    '/pose_estimation',
    10
)

        self.bridge = CvBridge()
        self.model = YOLO("yolov8n-pose.pt")

        self.get_logger().info("YOLOv8 Pose Estimation Node Started")

    def image_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, 'bgr8')
        results = self.model(cv_image)
        keypoints = results[0].keypoints.xy.tolist()
        self.publisher.publish(String(data=str(keypoints)))

def main():
    rclpy.init()
    node = PoseEstimationNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()