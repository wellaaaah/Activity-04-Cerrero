import cv2
File='me.jpg'
Flag=int(1)
img=cv2.imread(File,Flag)
cv2.imshow("Activity04", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
