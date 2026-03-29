# GOAL: Reach the target step and STOP.

def reach_top(current, target):
    if current == target:
        print("Goal Reached")
        return
    print(f"Climbing step number {current}")
    reach_top(current + 1, target)

reach_top(1, 5)