import pyautogui
import pynput
import time

def test_mode():
    print('  - 開始測試模式，')
    print('    按下滑鼠左鍵右鍵會記錄下對應的 script。')
    print('    要終止時請按下滑鼠中鍵。')

    with pynput.mouse.Listener(on_click=on_test_click) as listener:
        listener.join()

    print('  - 結束測試模式。')


def on_test_click(x, y, button, pressed):
    # Stop event when press middle button
    if button == pynput.mouse.Button.middle:
        return False

    # Record script
    if pressed:
        print('move {} {}'.format(x, y))
        print('wait 0.3')
        if button == pynput.mouse.Button.left:
            print('lc')
        else:
            print('rc')
        print('wait 0.3')

def wait_time(input_num):
    print('  - Sleep: ' + input_num)
    time.sleep(float(input_num))

def move_mouse(input_position):
    print('  - Move: {}'.format(input_position))
    pyautogui.moveTo(int(input_position[0]), int(input_position[1]), duration=0.3)

def left_click():
    print('  - Left Click')
    pyautogui.click(clicks=1, button='left')

def right_click():
    print('  - Right Click')
    pyautogui.click(clicks=1, button='right')

FunctionDict = {
    'test': test_mode,
    'wait': wait_time,
    'move': move_mouse,
    'lc': left_click,
    'rc': right_click
}