import cv2 as cv

def bgr_to_rgb(pic):
    b,g,r = cv.split(pic)
    return cv.merge([r,g,b])

def dec_to_bin(val):
    return str(bin(val).replace("0b", "")).zfill(8)

def bin_to_dec(val):
    return int(val, 2)