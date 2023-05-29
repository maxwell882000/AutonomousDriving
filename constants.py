import rospy

class SIGNS:
    IDLE = 0
    LANE_FOLLOWING = 1
    PARKING = 2
    CYCLE = 3
    LEFT = 4
    RIGHT = 5
    
class TASK_PARTS:
    START = 1
    BIG_PART = 2
    TURNS = 3
    PARKING  = 4