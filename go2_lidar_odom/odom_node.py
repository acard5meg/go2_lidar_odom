import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
import pdb

class Go2LidarOdom(Node):
  """
  Create an Odom from LiDaR class, which is a subclass of the Node class.
  """
  def __init__(self):
    """
    Class constructor to set up the node
    """
    # Initiate the Node class's constructor and give it a name
    super().__init__('go2_lidar_odom')

    self.odom_publisher = self.create_publisher(
            Odometry,
            '/odom/lidar',
            10)


    self.go2_lidar_subsribe = self.create_subscription(
            Odometry,
            '/utlidar/robot_odom',
            self.lidar_odom_pub,
            10)
            
  def lidar_odom_pub(self, msg):
    self.odom_publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    
    node = Go2LidarOdom()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
