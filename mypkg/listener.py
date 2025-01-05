import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray, String

class SimilarityListener(Node):
    def __init__(self):
        super().__init__('similarity_listener')
        self.create_subscription(Float32MultiArray, 'similar', self.similarity_callback, 10)
        self.create_subscription(String, 'file_names', self.filenames_callback, 10)

    def similarity_callback(self, msg):
        self.get_logger().info(f"Received similarity data: {msg.data}")

    def filenames_callback(self, msg):
        self.get_logger().info(f"Received filenames: {msg.data}")

def main():
    rclpy.init()
    node = SimilarityListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
