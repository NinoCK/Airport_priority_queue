from node import Node
from priority_queue import PriorityQueue    
import time
import random

def generate_random_traffic(landing_priority_queue, priority_queue_take_off):
    for _ in range(random.randint(0, 2)):
        if (land_priority := random.randint(100, 200)) and (take_off_priority := random.randint(100, 200)):
            landing_priority_queue.insert("requests landing", land_priority)
            takeoff_priority_queue.insert("requests take off", take_off_priority)

def initialize_queue(landing_queue, takeoff_queue, max_flights):
    """
    Initializes the queue and processes the flights until the maximum number of flights is reached.

    Parameters:
    landing_queue (Queue): The queue for landing flights.
    takeoff_queue (Queue): The queue for takeoff flights.
    max_flights (int): The maximum number of flights to process.

    Returns:
    None
    """
    generate_random_traffic(landing_queue, takeoff_queue)
    processed_flights = 0
    
    while (landing_queue.is_not_empty() or takeoff_queue.is_not_empty()) and processed_flights <= max_flights:
        if landing_queue.is_not_empty() is False:
            time.sleep(0.5)
            takeoff_queue.traverse()
            node = takeoff_queue.remove()
            time.sleep(0.5)
            if node is not None:
                print("CONTROL: " + str(node.priority) + " permission to takeoff.")
                processed_flights += 1
        else:
            time.sleep(0.5)
            landing_queue.traverse()
            node = landing_queue.remove()
            time.sleep(0.5)
            if node is not None:
                print("CONTROL: " + str(node.priority) + " permission to land.")
                processed_flights += 1

if __name__ == "__main__": 
    landing_priority_queue = PriorityQueue()
    takeoff_priority_queue = PriorityQueue() 
    initialize_queue(landing_priority_queue, takeoff_priority_queue,random.randint(6, 10))