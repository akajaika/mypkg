import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

rclpy.init()
node = Node("listener")

def cb(msg):
    global node
    self.get_logger().info(f"Listen: {msg.data}")

def main():
    pub = node.create_subscription(Float32MultiArray, "similar", cb, 10)
    rclpy.spin(node)

