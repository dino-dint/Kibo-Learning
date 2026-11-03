import random

def watchdog():
    battery = 100.0
    for step in range(1,11):
        reduce_battery = random.uniform(1.5, 3.5)
        battery -= reduce_battery
        print(f"step {step}: Battery at {battery:.2f}%")

        if battery < 75.0 :
            print("[EMEGENCY RETURN TRIGGERED]")
            break
        elif battery < 80.0 : 
            print("[CAUTION] Caution: Battery level is below 80%")

if __name__ == "__main__":
    watchdog()