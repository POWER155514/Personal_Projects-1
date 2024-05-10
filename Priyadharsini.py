import cv2
import numpy as np


def  Priyadharsini(ImgRGB):

    #Stage 1
    #-------

    #Step 2: Splitting ImgRGB in RGB color space 
    #---------------------------------------------
    bluechannel , greenchnnel, redchannel = cv2.split(ImgRGB)

    redchannel = ImgRGB[:,:,0]
    greenchannel = ImgRGB[:,:,1]
    bluechannel = ImgRGB[:,:,2]


    #Step 3: Calculate the variance of blue channel.
    #-------------------------------------------------
    var_blue = np.var(bluechannel)

    #step 4: Converting ImgRGB into Lab color space 
    #----------------------------------------------
    LabImg = cv2.cvtColor(ImgRGB, cv2.COLOR_BGR2Lab)
    L_channel, a_channel, b_channel = cv2.split(LabImg)

    #Step 5: Setting the variance threshold for the blue channel
    #------------------------------------------------------------
    var_threshold = 1500

    #Step 6: Checking if variance of blue channe; is greater than threshold value
    #--------------------------------------------------------------------------- 
    clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(8,8))
    L_Channel_row, L_channel_col=L_channel.shape
    ImgLab=np.zeros((L_Channel_row,L_channel_col,3),dtype=np.uint8)

    if var_blue<=var_threshold:
        clahe_img=clahe.apply(a_channel)+20
        ImgLab[:,:,0]=L_channel
        ImgLab[:,:,1]=clahe_img
        ImgLab[:,:,2]=b_channel        

    else:
        clahe_img=clahe.apply(b_channel)+20
        ImgLab[:,:,0]=L_channel
        ImgLab[:,:,1]=a_channel
        ImgLab[:,:,2]=clahe_img

    ImgRGB_Out=cv2.cvtColor(ImgLab, cv2.COLOR_Lab2BGR)


    #Stage 2
    #-------

    #Step 1: Splitting of fundus image in (RGB)’ color space to red, green, and blue channels
    #-----------------------------------------------------------------------------------------
    red,green,blue=cv2.split(ImgRGB_Out)

    #Step 2: Apply CLAHE on the green channel from Step 1 and merge the enhanced green channel with red and blue from Step 1
    #-----------------------------------------------------------------------------------------------------------------------

    clahe_green=clahe.apply(green)
    merged_img = cv2.merge([red,clahe_green,blue])

    #Step 3: Apply bilateral filter on an image in (RG’B)’ format
    #------------------------------------------------------------
    bilateral=cv2.bilateralFilter(merged_img,5,100,100)

    #Step 4: Auto-optimization of brightness and contrast
    #----------------------------------------------------

    img_gray = cv2.cvtColor(bilateral, cv2.COLOR_BGR2GRAY)
    gray_min=np.min(img_gray)
    gray_max = np.max(img_gray)
    alpha = 255 / (gray_max - gray_min)
    beta = -1 * gray_min * alpha
    img_out = cv2.convertScaleAbs(merged_img, alpha=alpha, beta=beta)


    return img_out

    #cv2.imshow('After', img_out)
    #cv2.imshow('Before',ImgRGB)
    #cv2.waitKey()
#img=cv2.imread('Image.jpg')
#Priyadharsini(img)