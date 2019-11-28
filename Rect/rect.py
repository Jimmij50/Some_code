#finding a rect hole in white board
# need to adjust the hsv threshol mannully
import cv2
img=cv2.imread("2.jpg")
import numpy as np
img=cv2.resize(img,(img.shape[1]//5,img.shape[0]//5))
dst=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
def nothing(x):
    pass
cv2.namedWindow('inr')
inr=cv2.inRange(dst,(0,0,0),(200,200,200))
cv2.createTrackbar('Hmin', 'inr', 0, 255, nothing)
cv2.createTrackbar('Smin', 'inr', 0, 255, nothing)
cv2.createTrackbar('Vmin', 'inr', 0, 255, nothing)
cv2.createTrackbar('Hmax', 'inr', 187, 255, nothing)
cv2.createTrackbar('Smax', 'inr', 187, 255, nothing)
cv2.createTrackbar('Vmax', 'inr', 187, 255, nothing)
cap=cv2.VideoCapture(0)
def child_contours(hierchy,contours):
    ans=[]
    b=hierchy[0][0][2]
    ans.append(b)
    while(b>0):
        b=hierchy[0][b][0]
        ans.append(b)
    ans=ans[:-1]
    cont=[]
    for i in ans:
        cont.append(contours[i])
    return cont
def judge(hierarchy,contours):
    ans=[]
    for i in range(hierarchy.shape[1]):
        if(hierarchy[0][i][3]!=-1):
            ans.append(contours[i])
    return ans

while True:
    _,frame=cap.read()
    #frame=img
   
    frame=cv2.resize(frame,(frame.shape[1]//2,frame.shape[0]//2))
    ori=frame
    frame=cv2.medianBlur(frame,3)
    hsv=cv2.cvtColor(frame,cv2.COLOR_RGB2HSV)
    #cv2.imshow("frame",frame)
    
    Hmin=cv2.getTrackbarPos('Hmin', 'inr')
    Smin=cv2.getTrackbarPos('Smin', 'inr')
    Vmin=cv2.getTrackbarPos('Vmin', 'inr')
    Hmax=cv2.getTrackbarPos('Hmax', 'inr')
    Smax=cv2.getTrackbarPos('Smax', 'inr')
    Vmax=cv2.getTrackbarPos('Vmax', 'inr')
    inr=cv2.inRange(frame,(Hmin,Smin,Vmin),(Hmax,Smax,Vmax))
    #inr=cv2.inRange(frame,(0,0,157),(187,24,217))#rear
    #inr=cv2.inRange(hsv,(0,0,0),(187,187,187))#front
    mask=(255-inr)//255
    #mask=inr//255
    te=frame
    for i in range(3):
        te[:,:,i]= np.multiply(frame[:,:,i],mask)
    oo=cv2.cvtColor(te,cv2.COLOR_RGB2GRAY)
    kernel1=np.array([[0,-2,0],
    [-2,8,-2],[0,-2,0]])
    kernel2=np.array([[0.11,0.11,0.11],
    [0.11,0.11,0.11],[0.11,0.11,0.11]])
    kernele = np.ones((5, 5), np.uint8)
    #te = cv2.erode(te, kernele)
    #fil=cv2.filter2D(te,-1,kernel2)
    #fil=cv2.filter2D(te,-1,kernel2)
    fil=cv2.Canny(te,200,200*2.5)
    #fil_s=cv2.cvtColor(fil,cv2.COLOR_RGB2GRAY)
    binary,contours, hierarchy=cv2.findContours(oo,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cnttt=judge(hierarchy,contours)
    cc=np.zeros([frame.shape[0],frame.shape[1]],dtype='uint8')
    #cont=child_contours(hierarchy,contours)
    #cv2.drawContours(cc,contours,-1,(255,255,255),1)
    maxArea=0
    index=0
    cnt_dict={}
    #print(len(contours))
    # for i in range(len(cnttt)):
    #     cnt_dict[cv2.contourArea(cnttt[i])]=cnttt[i]
    # ordd=sorted(cnt_dict)
    #maxi1=ordd[-1]
    #maxc1=cnt_dict[maxi1]
    for i in range(len(cnttt)):
        if cv2.contourArea(cnttt[i])>maxArea:
            maxArea=cv2.contourArea(cnttt[i])
            index=i
    #maxi2=ordd[-2]
    maxc1=cnttt[index]
    cnt=[]
    #print(ordd)
    
    #maxc2=cnt_dict[maxi2]
    cnt.append(maxc1)
    #cnt.append(maxc2)
    epsilon = 0.1*cv2.arcLength(maxc1,True)
    recc=cv2.approxPolyDP(maxc1,epsilon,True)
    x, y, w, h = cv2.boundingRect(recc)
    cv2.rectangle(ori,(x,y),(x+w,y+h),(0,0,255),3)
    rect = cv2.minAreaRect(recc)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(ori,[box],0,(0,255,0),2)
    #print(rect)
    
    #print(len(cnt))
    dd=cc
    #cv2.drawContours(cc,maxc2,-1,(255,255,255),3)
    
    cv2.drawContours(cc,[recc],-1,(255,255,255),1)
    cv2.imshow("inr",inr)
    cv2.imshow("te",te)
    cv2.imshow("fil",fil)
    cv2.imshow('cc',cc)
    cv2.imshow('ori',ori)
    cv2.waitKey(20)