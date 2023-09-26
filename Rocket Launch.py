import time
import logging

# Constants
MAX_ALTITUDE = 100
SPEED_INCREMENT = 10
STAGE_1_SEPARATION_ALTITUDE = 10

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the Rocket class
class Rocket:
    def __init__(self):
        self.stage = "Pre-Launch"
        self.fuel = 100
        self.altitude = 0
        self.speed = 0
        self.stage_number = 1  # Initial stage number
        self.orbit_achieved = False  # Track orbit achievement

    def pre_launch_checks(self):
        logger.info("Initiating pre-launch checks...")
        time.sleep(1)
        logger.info("All systems are 'Go' for launch.")

    def launch(self):
        if self.orbit_achieved:
            logger.info("Orbit already achieved! Mission Successful.")
            return

        logger.info("Beginning rocket launch...")
        self.stage = "Launch"
        while self.fuel > 0 and self.altitude < MAX_ALTITUDE:
            self.fuel -= 1
            self.altitude += 1
            self.speed += SPEED_INCREMENT

            # Check for stage separation
            if self.altitude == STAGE_1_SEPARATION_ALTITUDE and self.stage_number == 1:
                self.stage_number = 2
                logger.info("Stage 1 complete. Separating stage. Entering Stage 2.")

            logger.info(
                f"Stage: {self.stage_number}, Fuel: {self.fuel}%, Altitude: {self.altitude} km, Speed: {self.speed} km/h"
            )

            time.sleep(1)

        if self.altitude >= MAX_ALTITUDE:
            self.orbit_achieved = True
            logger.info("Orbit achieved! Mission Successful.")
        else:
            logger.error("Mission Failed due to insufficient fuel.")
            raise Exception("Mission Failed due to insufficient fuel.")

    def fast_forward(self, seconds):
        logger.info(f"Fast forwarding simulation by {seconds} seconds...")
        
        for _ in range(seconds):
            if self.fuel <= 0 or self.altitude >= MAX_ALTITUDE:
                break
            self.fuel -= 1
            self.altitude += 1
            self.speed += SPEED_INCREMENT

            # Check for stage separation
            if self.altitude == STAGE_1_SEPARATION_ALTITUDE and self.stage_number == 1:
                self.stage_number = 2
                logger.info("Stage 1 complete. Separating stage. Entering Stage 2.")

        logger.info(
            f"Stage: {self.stage_number}, Fuel: {self.fuel}%, Altitude: {self.altitude} km, Speed: {self.speed} km/h")
        
       

# Define the main function
def main():
    # Create a new Rocket object
    rocket = Rocket()
    
    print(" ")
    print("***Welcome to Rocket Launch***")
    print(" ")
    # Print the initial state
    print("Initial State")
    print("Stage:", rocket.stage)
    print("Fuel:", rocket.fuel, "%")
    print("Altitude:", rocket.altitude, "km")
    print("Speed:", rocket.speed, "km/h")

    # Initialize fast forward command
    fast_forward_seconds = 0

    # Start a loop to accept user input and update the rocket state
    while True:
        # Get the user input
        user_input = input("User Input: ")

        # Process user input
        if user_input == "start_checks":
            rocket.pre_launch_checks()
        elif user_input == "launch":
            rocket.launch()
        elif user_input.startswith("fast_forward"):
            try:
                seconds = int(user_input.split()[-1])
                fast_forward_seconds += seconds
                # Print current state while fast forwarding
                rocket.fast_forward(seconds)
            except ValueError:
                print("Invalid input for fast_forward.")
        elif user_input == "exit":
            break
        else:
            print("Invalid command. Valid commands are: start_checks, launch, fast_forward X, exit")

if __name__ == "__main__":
    main()