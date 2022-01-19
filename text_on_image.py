import cv2
font_size=1
def click_event(event, x, y, flags, params):
    global img,font_size
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ' ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text, (x,y), font,font_size, (200, 200, 200),2)
        cv2.imshow('image', img)
    if event==cv2.EVENT_RBUTTONDOWN:
        #call new page
        img=cv2.imread('demo.jpg',1)
        cv2.imshow('image',img)
        if cv2.waitKey(1):
            cv2.imwrite("Text_img.jpg",img)
    if event == cv2.EVENT_MOUSEWHEEL:
        font_size+=1
    if event == cv2.EVENT_MBUTTONDOWN:
        font_size=1

print("\n**INSTRUCTIONS**")
print("-----------------")
print("Left-click of mouse on the image at any position puts the text on that position.")
print("Right-click of mouse undos everything.")
print("Mouse wheel increases the font size.")
print("Mouse button to reset font size to small.")
print("Press any button to save the image.")
text=input("\nEnter the text to enter on image: ")

img = cv2.imread('demo.jpg', 1)
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
if cv2.waitKey(0):
    cv2.imwrite("Text_img.jpg",img)
cv2.destroyAllWindows()
