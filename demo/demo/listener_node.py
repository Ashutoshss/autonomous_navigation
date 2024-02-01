#!/usr/bin/env python3

'''
Created 27 Jan. 2024
 Modified 27 Jan. 2024
 by Ashutosh Singh
'''
import rclpy
from rclpy.node import Node
import sys

from std_msgs.msg import String


class listener(Node):
    def __init__(self):
        super().__init__("listener_node")

        self.sub_ = self.create_subscription(
            String,  # Message type
            'topic',  # Topic name
            self.callback_function,  # Callback function
            10  # QoS profile
        )
        
    def callback_function(self,msg):
        self.get_logger().info(msg.data)
        
def main():
    rclpy.init(args=sys.argv)   #rclpy: This is the Python client library for ROS 2.
                                #init: This function is used to initialize the ROS 2 Python client library.    
                                #args=sys.argv: This argument is optional. It allows you to pass command-line arguments to the initialization process. 
    listen = listener()

    rclpy.spin(listen)

    listen.destroy_node()

    rclpy.shutdown()
    
if __name__ == "__main__":
    main()