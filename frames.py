import cv2

def Take_Video():
	video = cv2.VideoCapture(0)
	frame_width = int(video.get(3))
	frame_height = int(video.get(4))
	size = (frame_width, frame_height)
	result = cv2.VideoWriter('vid1.avi',cv2.VideoWriter_fourcc(*'MJPG'),10, size)
	while(True):
		ret, frame = video.read()
		if ret == True:
			result.write(frame)
			cv2.imshow('Frame', frame)
			if cv2.waitKey(1) & 0xFF == 32:
				break
		else:
			break
	video.release()
	result.release()
	cv2.destroyAllWindows()
	print("The video was successfully saved")



def FrameCapture(path,ms,choice):
	vidObj = cv2.VideoCapture(path)
	if not vidObj.isOpened():
		print("Error in opening video file.")
		return

	success = 1
	l=[]
	while success:
		success, image = vidObj.read()
		try:
			image=cv2.resize(image,(700,500))
		except:
			break

		l.append(image)
	if choice==1:
		for i in reversed(l):
			cv2.imshow("Rev_Vid",i)
			cv2.waitKey(ms)
	else:
		for i in l:
			cv2.imshow("Fast_Fwd",i)
			cv2.waitKey(ms)
	cv2.destroyAllWindows()


while True:
	choice= int(input("\n1. To Reverse Play the Video.\n2. To Fast Forward-Play the Video.\n3. To Take a Video.\n4.Exit.\nChoice: "))
	if choice==1:
		FrameCapture("sample.mp4",20,1)
	elif choice==2:
		FrameCapture("sample.mp4",10,2)
	elif choice==3:
		Take_Video()
	elif choice==4:
		break
	else:
		print("\nInvalid Choice\n")
