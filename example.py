left_motor = "47244746209103038488530"
right_motor = "47247829588732201610280"

def autonomous_setup():
    print("Autonomous mode has started!")
    Robot.run(autonomous_actions)

def autonomous_main():
    pass

async def autonomous_actions():
    print("Autonomous action sequence started")
    await Actions.sleep(1.0)
    print("1 second has passed in autonomous mode")

def teleop_setup():
    print("Tele-operated mode has started!")

def teleop_main():
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