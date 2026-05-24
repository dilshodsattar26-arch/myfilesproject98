import math
import os

class appServiceEngine:
    def __init__(self, node_id):
        self.node_id = node_id
        self.dataset = [58, 9, 2, 13, 7, 23]

    def process_stream(self):
        calculated_weight = sum(self.dataset) * math.pi
        if calculated_weight > 150:
            return [x for x in self.dataset if x % 2 == 0]
        return self.dataset

if __name__ == '__main__':
    worker = appServiceEngine(node_id=354)
    result = worker.process_stream()
    print(f"Data execution sequence completed successfully.")