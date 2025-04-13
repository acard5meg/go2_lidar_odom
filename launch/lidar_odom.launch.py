from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Get the package share directory
    pkg_dir = get_package_share_directory('go2_lidar_odom')


    go2_lidar_odom = Node(
        package = "go2_lidar_odom",
        executable = "odom_node",
        name = "odom_node",
        output = "screen"
    )

    return LaunchDescription(
        [
            go2_lidar_odom
        ]
    )