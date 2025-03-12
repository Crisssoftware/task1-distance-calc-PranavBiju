#!usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from std_msgs.msg import  Float64
class Calc(Node):
    
    def __init__(self):
        super().__init__("calc")
        self.calc_subscriber= self.create_subscription(Pose,"/turtle1/pose", self.pose_callback, 10)
        self.calc_publisher = self.create_publisher(Float64, "/turtle1/distance_from_origin", 10)
    def pose_callback(self, pose: Pose):
        cmd = Float64()
        cmd.data = pose.x*pose.x + pose.y*pose.y
        self.calc_publisher.publish(cmd)

  

   
def main(args=None):
    rclpy.init(args=args)  
    node =Calc()
    rclpy.spin(node)
    rclpy.shutdown()