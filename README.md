# Go2 Lidar Odometry

## Package Structure

```
my_ros2_ws/src/go2_lidar_odom/
├── go2_lidar_odom/
│   ├── __init__.py
│   └── odom_node.py   # Main code
├── launch/
│   └── lidar_odom.launch.py # Launch file
├── resource/
│   └── go2_lidar_odom
├── package.xml
├── setup.py
└── setup.cfg
```

## Dependencies

- ROS2 Foxy
- Python 3

## Usage

1. Launch the navigation node:
   ```bash
   ros2 launch go2_lidar_odom lidar_odom.launch.py
   ```

### Published Topics
- `/odom/lidar topic` ([nav_msgs/Odometry](https://docs.ros.org/en/api/nav_msgs/html/msg/Odometry.html)) - Odometry topic for Navsat_Transform

### Generate Nodes
- `/odom_node`
