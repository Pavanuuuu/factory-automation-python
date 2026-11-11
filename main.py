
from equipment.robot import Robot
from equipment.conveyor import Conveyor

# Create factory equipment
robot1 = Robot("Welding Robot", 65, 15, "Arc")
conveyor1 = Conveyor("Assembly Conveyor", 55, 8, 2.5)
robot2 = Robot("Painting Robot", 50,10, "Spray")

# Start equipment
robot1.start()
conveyor1.start()

# Perform operations
robot1.weld()
conveyor1.move_products()

# Check status
robot1.check_status()
conveyor1.check_status()

# Stop robot
robot1.stop()

# Try welding after stopping
robot1.weld()
robot2.start()
robot2.paint()

robot1.show_temperature()
