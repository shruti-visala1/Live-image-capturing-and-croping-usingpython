import argparse 
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # do what you want with frame
    #  and then save to file
    cv2.imwrite('image.png', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'): # you can increase delay to 2 seconds here

        break
    cv2.imshow("imshow2",frame)
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()



# now let's initialize the list of reference point 
ref_point = [] 
crop = False

def shape_selection(event, x, y, flags, param): 
	# grab references to the global variables 
	global ref_point, crop 

	# if the left mouse button was clicked, record the starting 
	# (x, y) coordinates and indicate that cropping is being performed 
	if event == cv2.EVENT_LBUTTONDOWN: 
		ref_point = [(x, y)] 

	# check to see if the left mouse button was released 
	elif event == cv2.EVENT_LBUTTONUP: 
		# record the ending (x, y) coordinates and indicate that 
		# the cropping operation is finished 
		ref_point.append((x, y)) 

		# draw a rectangle around the region of interest 
		cv2.rectangle(image, ref_point[0], ref_point[1], (0, 255, 0), 5) 
		cv2.imshow("image", image) 


# construct the argument parser and parse the arguments 
'''ap = argparse.ArgumentParser() 
ap.add_argument("-i", "--image", required = True, help ="Path to the image") 
args = vars(ap.parse_args())''' 

# load the image, clone it, and setup the mouse callback function 
image = cv2.imread("image.png") 
clone = image.copy() 
cv2.namedWindow("image") 
cv2.setMouseCallback("image", shape_selection) 


# keep looping until the 'q' key is pressed 
while True: 
	# display the image and wait for a keypress 
	cv2.imshow("image", image) 
	key = cv2.waitKey(1) & 0xFF

	# press 'r' to reset the window 
	if key == ord("r"): 
		image = clone.copy() 

	# if the 'c' key is pressed, break from the loop 
	elif key == ord("c"): 
		break

if len(ref_point) == 2: 
	crop_img = clone[ref_point[0][1]:ref_point[1][0], ref_point[0][0]: 
														ref_point[1][0]] 
	im=cv2.imshow("crop_img", crop_img)
	cv2.imwrite('crop.png', crop_img)
	cv2.write()
	cv2.waitKey(0) 

# close all open windows 
cv2.destroyAllWindows()

