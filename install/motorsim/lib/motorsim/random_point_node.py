#!/usr/bin/python3

import random
import rclpy
import yaml
from rclpy.node import Node
from std_msgs.msg import Bool


class SchedulerNode(Node):
    def __init__(self):
        super().__init__('scheduler_node')

        self.freq = 100.0
        self.yaml_create()

        self.randomReady_publisher = self.create_publisher(Bool, "randomReady", 10)
        
        self.create_subscription(Bool, "random", self.random_callback, 10)

        self.create_timer(1.0 / self.freq, self.timer_callback)
        
        self.random = False
        self.data
        self.state = 0
    
    def random_callback(self, msg:Bool):
        self.random = msg.data
        
    def yaml_create(self):
        empty_data = {}  # Or [] if you want an empty list

        # Write to the YAML file
        with open('/home/teety/GitHub/FUN3-5/src/motorsim/via_point/' + str(self.get_namespace()) + '_via_point.yaml', 'w') as file:
            yaml.dump(empty_data, file)
            self.data = {'targets': []}
     
    def yaml_write(self):
        with open('/home/teety/GitHub/FUN3-5/src/motorsim/via_point/' + str(self.get_namespace()) + '_via_point.yaml', 'w') as file:
            yaml.dump(self.data, file)     
            
    def timer_callback(self):

        if self.random:
            if self.state == 0:
                # self.get_logger().info(f"Current Rand: {self.random}")
                random_target = random.uniform(0.0, 10.0)
                self.data['targets'].append(random_target)
                self.state = 1
                
            self.yaml_write()
            msg = Bool()
            msg.data = True
            self.randomReady_publisher.publish(msg)
            # print(self.data)
            
        else:
            msg = Bool()
            msg.data = False
            self.randomReady_publisher.publish(msg)
            self.state = 0

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
