
from pymem import Pymem
import keyboard
import pygetwindow as gw
import time

# bf1.exe+1AE0151 bullet address
# 2x value 85899000000002B8
# 1x value 858900000104818B

def main():
    pm = Pymem('bf1.exe')
    game_module = pm.process_base.lpBaseOfDll

    bulletOffset = 0x1AE0151
    defaultValue = 0x858900000104818B
    doubledValue = 0x85899000000002B8
    bulletAddress = game_module+bulletOffset
    setedValue = defaultValue
    while True:
        title = gw.getActiveWindowTitle()
        if title == "Battlefield™ 1":
            if keyboard.is_pressed("F1"):
                if setedValue == defaultValue:
                    continue
                print('Set 1x')
                setedValue = defaultValue
                pm.write_ulonglong(bulletAddress,int(defaultValue))
            elif keyboard.is_pressed("F2"):
                if setedValue == doubledValue:
                    continue
                print('Set 2x')
                setedValue = doubledValue
                pm.write_ulonglong(bulletAddress,int(doubledValue))
        time.sleep(0.1)

if __name__ == "__main__":
    main()
