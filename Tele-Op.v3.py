lM = "56692008314550567751418"
rM = "47247829588732201610280"
RFID = "51977114113569040836828"
lineID = "4748884830604085344402"
deg180 = 3.6

def most_common_digit(num):
  #YOUR CODE HERE
  countstring=str(num)
  array=[]
  if num == 0:
    return 0
  for i in countstring:
    if (not i=="0") or i.isDigit():
      j = 0
      while True:
        if j==len(array):
          array.append([i,1])
          break
        if array[j][0]==i:
          array[j][1]+=1
          break
        j+=1
  if(len(array)==0):return num
  h = [array[0]]
  for d in range(1,len(array)):
    if array[d][1]>h[0][1]:
      h[0]=array[d]
    elif array[d][1]==h[0][1]:
      h.append(array[d])
  hi = h[0][0]
  if len(h) > 1:
    for i in h:
      if i[0]>hi:
        hi = i[0]
  else:
    return int(h[0][0])
  return int(hi)

# Sets value of a specified motor controller (YogiBear)
# @param devID: <String> identifies which controller will be set, value: <float> [-1, 1] specifies % power of motor
def setM(devID, value):
    Robot.set_value(devID, "duty_cycle", value)
# def getM(devID, value):
#     Robot.get_value(devID, "duty_cycle", value)
def autonomous_setup():
    print("Autonomous mode has started!")
    Robot.run(autonomous_actions)
    
def reset():
    Robot.set_value(lM,"enc_pos",0)
    Robot.set_value(rM,"enc_pos",0)

def getPos(side):
    return Robot.get_value(side, "enc_pos")

#functions for autonomous
async def turnAround():
    reset()
    setM(rM, 1.0)
    setM(lM, 1.0)
    while (abs(getPos(rM)) < 10000) and (abs(getPos(lM)) < 10000):
        await Actions.sleep(0.05)
    setM(rM, 0)
    setM(lM, 0)
    await Actions.sleep(2000000000000000000000000000)
    
def autonomous_main():
    # if Robot.get_value("21025408676888160927", "switch0"):
    #     setM(rM, 1.0)
    #     setM(lM, -1.0)
    # else:
    #     setM(rM, 0.0)
    #     setM(lM, 0.0)
    Robot.run(turnAround)
    pass

async def autonomous_actions():
    print("Autonomous action sequence started")
    await Actions.sleep(1.0)
    print("1 second has passed in autonomous mode")

def teleop_setup():
    print("Tele-operated mode has started!")

def teleop_main():
    # right stick y value
    rY = Gamepad.get_value("joystick_right_y")
    # left stick y value
    lY = Gamepad.get_value("joystick_left_y")
    # right stick button
    rsb = Gamepad.get_value("r_stick")
    # left stick button
    lsb = Gamepad.get_value("l_stick")
    #Right Servo
    rS = "servo0"
    #Left Servo
    lS = "servo1"
    # slow speed value (for easy debug)
    s = 0.4
    # joystick treshhold
    thresh = 0.1
    #Angle of servo movement
    angle = 0.08
    if rY > thresh:
        #setM(rM, -s if rsb else -1)
        #Move Right
        Robot.set_value(servo_arm_id, lS, angle) 
        Robot.set_value(servo_arm_id, rS, -angle)
    elif rY < -thresh:
        #setM(rM, s if rsb else 1)
        Robot.set_value(servo_arm_id, rS, 0)
        Robot.set_value(servo_arm_id, lS, 0)
    else:
        #setM(rM, 0)
        #Resets to zero
         Robot.set_value(servo_arm_id, rS, 0)
        Robot.set_value(servo_arm_id, lS, 0)
    if lY > thresh:
        #setM(lM, s if lsb else 1)
        #Move left
        Robot.set_value(servo_arm_id, lS, -angle) 
        Robot.set_value(servo_arm_id, rS, angle)
    elif lY < -thresh:
        #setM(lM, -s if lsb else -1)
        Robot.set_value(servo_arm_id, rS, 0)
        Robot.set_value(servo_arm_id, lS, 0)
    else:
        #setM(lM, 0)
        Robot.set_value(servo_arm_id, rS, 0)
        Robot.set_value(servo_arm_id, lS, 0)
        
    # if Robot.get_value(RFID, "tag_detect"):
    #     print(Robot.get_value(RFID, "id"))
