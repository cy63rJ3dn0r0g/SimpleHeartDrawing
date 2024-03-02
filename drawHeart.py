import pyautogui
import time

def bringPaintToTop():
    paintWindows = pyautogui.getWindowsWithTitle('Paint')
    if paintWindows:
        paintWindow = paintWindows[0]
        paintWindow.activate()
        paintWindow.maximize()

def increaseSize():
    pyautogui.hotkey('ctrl', 'add')

def decreaseSize():
    pyautogui.hotkey('ctrl', 'subtract')

def selectAll():
    pyautogui.hotkey('ctrl', 'a')

pyautogui.press('winleft')
pyautogui.typewrite("paint")
time.sleep(1)
pyautogui.press('enter')
bringPaintToTop()
time.sleep(1)

increaseSize()
increaseSize()
increaseSize()

startX = 1300
startY = 900

#left side
pyautogui.moveTo(startX, startY)
pyautogui.dragTo(startX - 220, startY - 360, duration=0.1)
#rught side
pyautogui.moveTo(startX, startY)
pyautogui.dragTo(startX + 220, startY - 360, duration=0.1)
#bottom
#mid
pyautogui.moveTo(startX, startY - 360)
#mid to left
pyautogui.dragTo
for line in range(5):
    pyautogui.dragTo(startX, startY - 360, duration=0.1)
    startY -= 5
    startX -= 2
for line in range(5):
    pyautogui.dragTo(startX, startY - 360, duration=0.1)
    startY -= 5
    startX -= 4
for line in range(5):
    pyautogui.dragTo(startX, startY - 360, duration=0.1)
    startY -= 5
    startX -= 6
for line in range(5):
    pyautogui.dragTo(startX, startY - 360, duration=0.1)
    startY -= 5
    for line in range(5):
        startX -= 1+1
        print('X' + str(startX))
for line in range(5):
    pyautogui.dragTo(startX, startY - 360, duration=0.1)
    startY -= 0
    startX -= 10
for line in range(5):
    pyautogui.dragTo(startX, startY - 360, duration=0.1)
    startY += 2
    startX -= 4
    print("Y:" + str(startY))
    print('X' + str(startX))
for line in range(5):
    pyautogui.dragTo(startX, startY - 360, duration=0.1)
    startY += 3
    startX -= 3
    print("Y:" + str(startY))
    print('X' + str(startX))
for line in range(6):
    pyautogui.dragTo(startX, startY - 360, duration=0.1)
    startY += 3
    startX -= 3
    print("Y:" + str(startY))
    print('X' + str(startX))
for line in range(5):
    pyautogui.dragTo(startX, startY - 360, duration=0.1)
    startY += 4
    startX -= 2
    print("Y:" + str(startY))
    print('X' + str(startX))
for line in range(7):
    pyautogui.dragTo(startX, startY - 360, duration=0.1)
    startY += 2
    startX += 0
for line in range(8):
    pyautogui.dragTo(startX, startY - 360, duration=0.1)
    startY += 2
    startX += 0
for line in range(5):
    pyautogui.dragTo(startX, startY - 360, duration=0.1)
    startY += 2
    startX += 1
pyautogui.dragTo(1080, 540, duration=0.1)
startXR=1310
startYR = 510
#mid to Right
pyautogui.moveTo(1300, 540)
pyautogui.dragTo(startXR, startYR,duration=0.1)
for line in range(5):
    pyautogui.dragTo(startXR, startYR,duration=0.1)
    startXR +=2
    startYR -=3
for line in range(5):
    pyautogui.dragTo(startXR, startYR,duration=0.1)
    startXR +=2
    startYR -=2
for line in range(5):
    pyautogui.dragTo(startXR, startYR,duration=0.1)
    startXR +=3
    startYR -=2
for line in range(5):
    pyautogui.dragTo(startXR, startYR,duration=0.1)
    startXR +=3
    startYR -=2
for line in range(5):
    pyautogui.dragTo(startXR, startYR,duration=0.1)
    startXR +=3
    startYR -=1
for line in range(5):
    pyautogui.dragTo(startXR, startYR,duration=0.1)
    startXR +=2
    startYR -=1
for line in range(5):
    pyautogui.dragTo(startXR, startYR,duration=0.1)
    startXR +=3
    startYR -=1
for line in range(5):
    pyautogui.dragTo(startXR, startYR,duration=0.1)
    for line in range (5):
        startXR +=2
    startYR -=1
for line in range(8):
    pyautogui.dragTo(startXR, startYR,duration=0.1)
    startXR +=3
    startYR +=1
for line in range(5):
    pyautogui.dragTo(startXR, startYR, duration=0.1)
    startXR +=3
    startYR +=1
for line in range(5):
    pyautogui.dragTo(startXR, startYR, duration=0.1)
    startXR +=3
    startYR +=2
for line in range(8):
    pyautogui.dragTo(startXR, startYR, duration=0.1)
    startXR +=2
    startYR +=2
for line in range(8):
    pyautogui.dragTo(startXR, startYR, duration=0.1)
    startXR +=1
    startYR +=2
pyautogui.dragTo(1525, 525, duration=0.1)
pyautogui.dragTo(1520, 540, duration=0.1)

selectAll()
decreaseSize()
increaseSize()
decreaseSize()
increaseSize()
decreaseSize()
increaseSize()
decreaseSize()
