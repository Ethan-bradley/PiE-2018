left_motor = "56692008314550567751418"
right_motor = "56695389584535285373953"
#central_motor = ""
servo_arm_id = "33080838212650385105500"

def autonomous_setup():
    print("Autonomous mode has started!")
    Robot.run(autonomous_actions)

def autonomous_main():
    #Robot.set_value(left_motor, "duty_cycle", -1.0)
    #Robot.set_value(right_motor, "duty_cycle", 1.0)
    Robot.set_value(servo_arm_id, "servo1", 0.0) 
    Robot.set_value(servo_arm_id, "servo0", 0.0) 


async def autonomous_actions():
    print("Autonomous action sequence started")
    await Actions.sleep(1.0)
    print("1 second has passed in autonomous mode")

def teleop_setup():
    print("Tele-operated mode has started!")

def teleop_main():
    print("anything")
    right_y = Gamepad.get_value("joystick_right_y")
    if right_y > 0.5:
        Robot.set_value(right_motor, "duty_cycle", -1.0)
    elif right_y < -0.5:
        Robot.set_value(right_motor, "duty_cycle", 1.0)
    else:
        Robot.set_value(right_motor, "duty_cycle", 0)
    left_y = Gamepad.get_value("joystick_left_y")
    if left_y > 0.5:
        Robot.set_value(left_motor, "duty_cycle", 1.0)
    elif left_y < -0.5:
        Robot.set_value(left_motor, "duty_cycle", -1.0)
    else:
        Robot.set_value(left_motor, "duty_cycle", 0)
        
    print("something else")
    
    if Robot.get_value("rfid", "tag_detect"):
        Robot.set_value(left_motor, "duty_cycle", 1.0)
        print(Robot.get_value("rfid", "id"))