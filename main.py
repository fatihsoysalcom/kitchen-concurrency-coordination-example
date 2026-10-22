import threading
import time
import random

# Represents a critical shared zone in the kitchen, like a narrow passageway
class KitchenPassageway:
    def __init__(self):
        # The 'Behind!' command is implemented as a threading.Lock
        # It ensures only one chef can be in the critical section at a time.
        self.lock = threading.Lock()
        self.current_occupant = None

    def enter(self, chef_name):
        print(f"[{time.strftime('%H:%M:%S')}] {chef_name}: About to enter the passageway... (waiting for 'Behind!' signal)")
        
        # Chef acquires the lock, simulating shouting "Behind!" and waiting for clearance.
        # This prevents multiple chefs from entering simultaneously.
        self.lock.acquire()
        try:
            self.current_occupant = chef_name
            print(f"[{time.strftime('%H:%M:%S')}] {chef_name}: *** 'BEHIND!' *** (Entered passageway safely)")
            time.sleep(random.uniform(0.1, 0.5)) # Simulate the time spent passing through
            print(f"[{time.strftime('%H:%M:%S')}] {chef_name}: Exiting passageway.")
        finally:
            self.current_occupant = None
            # Chef releases the lock, signaling the passageway is clear.
            self.lock.release()

def chef_task(chef_name, passageway):
    for i in range(3): # Each chef tries to pass through multiple times
        time.sleep(random.uniform(0.5, 1.5)) # Simulate doing other work in the kitchen
        print(f"[{time.strftime('%H:%M:%S')}] {chef_name}: Needs to use the passageway (attempt {i+1}).")
        passageway.enter(chef_name)

if __name__ == "__main__":
    print("--- Kitchen Simulation: Parallel Coding Agents ---\n")
    passageway = KitchenPassageway()

    chef_names = ["Chef Alice", "Chef Bob", "Chef Charlie"]
    threads = []

    for name in chef_names:
        thread = threading.Thread(target=chef_task, args=(name, passageway))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("\n--- All chefs have completed their tasks. Kitchen closed. ---")
