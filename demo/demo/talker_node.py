#!/usr/bin/env python3

'''
Created 26 Jan. 2024
 Modified 26 Jan. 2024
 by Ashutosh Singh
'''

import rclpy
from rclpy.node import Node
import sys
from std_msgs.msg import String         # string is a part of std_msgs
from demo.move import Movement          # how to import custom modules

class talker(Node):
    def __init__(self):
        super().__init__("talker_node")         #node name

        self.pub_ = self.create_publisher(msg_type = String,topic = "topic" ,qos_profile = 10)      # creating  publisher

        processing_rate = 0.1
        self.timer = self.create_timer(timer_period_sec = processing_rate, callback = self.callback_function)      # creating a timer for calling the function in every 0.1 sec
        self.motion = Movement()        #making the object of the module
        self.count = 0

    def callback_function(self):
        _msg_ = String()
        _msg_.data = f"Ashutosh is Great... {self.count}"
        self.get_logger().info(f"Ashutosh is Great... {self.count}")
        self.get_logger().info(f"Ashutosh is Great... {self.motion.movedown()}")            #using the function inside the module
        self.count+=1
        self.pub_.publish(_msg_)



def main():

    rclpy.init(args=sys.argv)       #initalizing

    talk = talker()                 #making the instance of the node class

    rclpy.spin(talk)                # Spin the node 

    talk.destroy_node()             #destroy node

    rclpy.shutdown()                #shutdown the node
if __name__ == "__main__":
    main()