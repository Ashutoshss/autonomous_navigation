from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    talk = Node(
        package="demo",                     #package name
        executable="talkerNode",            # executable name given in the setup.py
        name="taker"
    )
    listen = Node(
        package="demo",                     #package name
        executable="listenerNode",          # executable name given in the setup.py
        name="listener"                     
    )

    return LaunchDescription([
        talk,
        listen
    ])