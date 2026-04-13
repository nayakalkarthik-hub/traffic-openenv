import random

class TrafficMedEnv:
    def __init__(self):
        self.num_lanes = 4

    def reset(self):
        self.traffic = [random.randint(5, 20) for _ in range(self.num_lanes)]
        self.ambulance_lane = random.randint(0, self.num_lanes - 1)
        return self.traffic, self.ambulance_lane


def predict(input_data=None):
    print("[START]")

    env = TrafficMedEnv()
    traffic, ambulance_lane = env.reset()

    # Simple logic (replace later with RL)
    action = ambulance_lane

    # Single STEP line
    print(f"[STEP] Traffic: {traffic} | Ambulance: {ambulance_lane} | Signal: {action}")

    result = {
        "traffic": traffic,
        "ambulance_lane": ambulance_lane,
        "chosen_signal": action
    }

    print("[END]")
    print(result)

    return result
