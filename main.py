from gopigo import *
import time


class Piggy(object):

    def __init__(selfslef):
            print("I am alive")
    def cha_cha(self):
        for x in range(5):
            right_rot()
            time.sleep(.5)
            left_rot()
            time.sleep(.5)
            motor_fwd(3)
            stop()




p = Piggy ()
p.cha_cha()