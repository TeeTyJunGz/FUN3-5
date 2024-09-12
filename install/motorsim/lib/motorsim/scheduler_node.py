#!/usr/bin/python3

import rclpy
import yaml
from rclpy.node import Node
from std_msgs.msg import Float64, Bool

from std_srvs.srv import SetBool

class SchedulerNode(Node):
    def __init__(self):
        super().__init__('scheduler_node')

        self.freq = 100.0

        self.notify_service = self.create_service(SetBool, "notify", self.notifyService)

        self.random_publisher = self.create_publisher(Bool, "random", 10)
        self.target_publisher = self.create_publisher(Float64, "target", 10)
        
        self.create_subscription(Bool, "randomReady", self.random_callback, 10)
        self.create_timer(1.0 / self.freq, self.timer_callback)
        
        self.random = False
        self.notify = False
        self.index = 0
        self.state = 0

    def loadYAML(self):
        with open('/home/teety/GitHub/FUN3-5/src/motorsim/via_point/' + str(self.get_namespace()) + '_via_point.yaml', 'r') as file:
            data = yaml.safe_load(file)
            return data['targets']

    def notifyService(self, request:SetBool.Request, response:SetBool.Response):
        msg = request
        self.notify = msg.data
        response.success = True
        response.message = 'Change Boolean Successfully'
        return response
    
    def random_callback(self, msg:Bool):
        self.random = msg.data
    
    def timer_callback(self):

        if self.notify:
            random = Bool()
            random.data = True
            self.random_publisher.publish(random)
            if self.random:
                self.target = self.loadYAML()
                msg = Float64()
                msg.data = self.target[self.index]
                self.get_logger().info(f"Current target: {self.target[self.index]}")
                self.target_publisher.publish(msg)
                self.state = 1
            
        else:
            if self.state == 1:
                self.index += 1
                self.state = 0
            else:
                random = Bool()
                random.data = False
                self.random_publisher.publish(random)

        # self.get_logger().info(f"Current target: {self.notify}")
        # self.get_logger().info(f"Current target: {self.index}")
        # pass
    
def main(args=None):
    rclpy.init(args=args)
    node = SchedulerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
