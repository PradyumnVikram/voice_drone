import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import numpy as np
from voice_rec import return_coordinates

class DroneCoordinatePublisher(Node):
    def _init_(self):
        super()._init_('drone_coordinate_publisher')
        self.publisher_ = self.create_publisher(Float32MultiArray, 'drone_coordinates', 10)
        self.timer = self.create_timer(1.0, self.publish_coordinates)

        self.drone_position = np.array([0.0, 0.0, 3.0])

        self.get_logger().info("Drone Coordinate Publisher Started")

    def publish_coordinates(self):
        self.drone_position += return_coordinates()

        msg = Float32MultiArray()
        msg.data = self.drone_position.tolist()

        self.publisher_.publish(msg)
        self.get_logger().info(f"Published coordinates: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = DroneCoordinatePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()