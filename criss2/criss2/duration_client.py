#!usr/bin/env python3
import sys
import rclpy
from rclpy.node import Node
from tutorial_interfaces.srv import Duration

class Client(Node):
    def __init__(self):
        super().__init__("client_node")
        self.client = self.create_client(Duration, "dur")
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn("Waiting for service to be available...")

    def request(self, duration):
        req = Duration.Request()
        req.a =duration
        self.future = self.client.call_async(req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()
     




def main(args=None):
    rclpy.init(args=args)
    node = Client()
    try:
        duration = int(sys.argv[1]) 
        response = node.request(duration)
        print(f"Response from server: Success = {response.success}") 
    except Exception as e:
        print(f"Service call failed: {e}")
    rclpy.shutdown()