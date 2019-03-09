right_motor = "56692008314550567751418"
left_motor = "56695389584535285373953"
#central_motor = ""
servo_arm_id = "33085227150045326350192"
line_followers = "4754803307256596519891"

def autonomous_setup():
    print("Autonomous mode has started!")
    Robot.run(autonomous_actions)

def autonomous_main():
    print("main")
    #Robot.set_value(left_motor, "duty_cycle", -1.0)
    #Robot.set_value(right_motor, "duty_cycle",1.0)
    #Robot.set_value(servo_arm_id, "servo1", 1.0) 
    #Robot.set_value(servo_arm_id, "servo0", -1.0) 
    #await Actions.sleep(3.0)
    #autonomous_move()
    
    
async def autonomous_actions():
    #Robot.set_value(servo_arm_id, "servo1", 1.0) 
    #Robot.set_value(servo_arm_id, "servo0", 1.0) 
    #Tells robot to move forward:
    Robot.run(autonomous_move)
    
    
async def autonomous_move():
    #Tells robot to move forward:
    #Opposite to go forward, same to turn.
    print("Starting forward")
    Robot.set_value(left_motor, "duty_cycle", 0.5)
    Robot.set_value(right_motor, "duty_cycle", -0.5)
    await Actions.sleep(1.0)
    print("Starting turn")
    Robot.set_value(left_motor, "duty_cycle", 0.5)
    Robot.set_value(right_motor, "duty_cycle", 0.5)
    await Actions.sleep(0.5)
    print("Starting foward")
    Robot.set_value(left_motor, "duty_cycle", 0.5)
    Robot.set_value(right_motor, "duty_cycle", -0.5)
    await Actions.sleep(1.0)
    print("Ending")
    
def autonomous_follow_line():
    #Tells robot to move along line (More than 0.9 is black, less is white):
    if(Robot.get_value(line_follower_id, "center") <= 0.9):
        #Tells robot to move forward if on white line
        Robot.set_value(left_motor, "duty_cycle", 0.4)
        Robot.set_value(right_motor, "duty_cycle", 0.4)
    elif (Robot.get_value(line_follower_id, "center") > 0.9):
        #Tells robot to turn if not on white line
        Robot.set_value(left_motor, "duty_cycle", -0.4)
        Robot.set_value(right_motor, "duty_cycle", 0.4)

async def autonomous_pick_up_center_box():
    #Tells robot to move forward:
    Robot.set_value(left_motor, "duty_cycle", 0.4)
    Robot.set_value(right_motor, "duty_cycle", 0.4)
    await Actions.sleep(0.5)
    #Lift up box
    #Tells Roboto to move backwards
    Robot.set_value(left_motor, "duty_cycle", -0.4)
    Robot.set_value(right_motor, "duty_cycle", -0.4)
    #Unload box
    Robot.set_value(left_motor, "duty_cycle", 0.1)
    Robot.set_value(right_motor, "duty_cycle", 0.5)
    await Actions.sleep(1.0) 
    


def teleop_setup():
    print("Tele-operated mode has started!")

def teleop_main():
    #print("anything")
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
        Robot.set_value(left_motor, "duty_cycle", 0.0)
            
        #if Robot.get_value("rfid", "tag_detect"):
        #    Robot.set_value(left_motor, "duty_cycle", 1.0)
        #print(Robot.get_value("rfid", "id"))