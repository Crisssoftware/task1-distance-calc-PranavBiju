#!usr/bin/env python3
import rclpy
from rclpy.node import Node
from tutorial_interfaces.srv import Duration
from geometry_msgs.msg import Twist
import time
class Criss2(Node):

    def __init__(self):
        super().__init__("move")
        self.srv = self.create_service(Duration,"dur", self.duration_callback)
        self.publisher= self.create_publisher(Twist,"/cmd_vel", 10)
        
    def duration_callback(self, request, response):
        twist = Twist()
        twist.linear.x=1.0
        time1=time.time()
        while time.time()-time1<request.a:
          self.publisher.publish(twist)

        twist.linear.x=0.0
        self.publisher.publish(twist)
        response.success= True
        return response

def main(args=None):
    rclpy.init(args=args)
    node = Criss2()
    rclpy.spin(node)
    rclpy.shutdown()