import cv2
import numpy as np
#import ip_module

cap = cv2.VideoCapture(1)

ret,frame = cap.read()
X = frame.shape[1]
Y = frame.shape[0]
start_x = 0
start_y = 0
end_x = X/9
end_y = Y/9

p=0
if __name__=="__main__":
	#obj = ip_module.Ball()
	
	while (True):
		ret,frame = cap.read()
		fra = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
		mask_ball = cv2.inRange(fra, np.array([23,52,230]), np.array([40,120,260]))
	        _,contours_ball,hierarchy = cv2.findContours(mask_ball, cv2.RETR_TREE, 2)
		#for p in range(contours_ball[p]):		
		M = cv2.moments(contours_ball[p])
                centroid_ball = int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"])
		
		cv2.circle(frame,(centroid_ball[0],centroid_ball[1]),10,(0,0,255),2)
		
		for i in range(9):
			for j in range(9):
				frame = cv2.rectangle(frame,(start_x+(X/9)*i,start_y+(Y/9)*j),(end_x+(X/9)*i,end_y+(Y/9)*j),(0,0,255))		
		'''
		frame_gray = obj.rgb2gray(frame)
		ret, thresh = obj.threshold_image(frame_gray,50,255)
		contour, heirarchy = obj.find_contours(thresh)
		'''
		cv2.imshow("img",frame)
		cv2.imshow("img2",fra)
		
		if (cv2.waitKey(1) & 0xFF == ord('q')) :
			break
	cap.release()
	cv2.DestroyAllWindows()

