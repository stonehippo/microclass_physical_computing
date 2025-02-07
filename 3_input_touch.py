# Input: sennsing with capacitive touch!
import time
import board

import touchio

touch_one = touchio.TouchIn(board.TOUCH1)
touch_two = touchio.TouchIn(board.TOUCH2)

while True:
	if touch_one.value:
		print("Someone is touching the first pad")
	if touch_two.value:
		print("Someone is touching the second pad")
	time.sleep(0.01)
