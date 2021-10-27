import cv2
import os
import numpy as np
import pytesseract

def get_frames(video='video.mp4'):
    cam = cv2.VideoCapture(video)
    os.makedirs('data', exist_ok=True)

    prev_frame = None
    prev_change = False
    currentframe = 1
    special = []

    while True:
        ret, frame = cam.read()
        if not ret: 
            break
        if prev_frame is not None:
            result = float(cv2.matchTemplate(frame, prev_frame, cv2.TM_CCOEFF_NORMED)[0, 0])
            if result < 0.1:
                if prev_change:
                    special.append((currentframe - 1, prev_frame))
                prev_change = True
            else:
                prev_change = False

        currentframe += 1
        prev_frame = frame

    cam.release()
    cv2.destroyAllWindows()

    return special

def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

def transform(image):
    im_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh, im_bw = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    se1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    se2 = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
    mask = cv2.morphologyEx(im_bw, cv2.MORPH_CLOSE, se1)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, se2)
    # mask = np.dstack([mask, mask, mask])
    mask = mask // 255

    return im_bw * mask

    #find all your connected components (white blobs in your image)
    nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(im_bw, connectivity=8)
    #connectedComponentswithStats yields every seperated component with information on each of them, such as size
    #the following part is just taking out the background which is also considered a component, but most of the time we don't want that.
    sizes = stats[1:, -1]; nb_components = nb_components - 1

    # minimum size of particles we want to keep (number of pixels)
    #here, it's a fixed value, but you can set it as you want, eg the mean of the sizes or whatever
    min_size = 150  

    #your answer image
    img2 = np.zeros((output.shape))
    #for every component in the image, you keep it only if it's above min_size
    for i in range(0, nb_components):
        print(sizes[i])
        if sizes[i] >= min_size:
            img2[output == i + 1] = 1
    print(img2)
    return img2

custom_config = r'--oem 3 --psm 6'
# frames = get_frames()

frames = []
for file in os.listdir('data'):
    img = cv2.imread('data/' + file)
    frames.append((0, img))

for num, frame in frames:
    img = transform(frame)
    txt = pytesseract.image_to_string(img, config=custom_config)
    print(txt)
    cv2.imwrite('image.png', img)
    break


# name = './data/frame' + str(currentframe - 1) + '.jpg'
# print('Creating...' + name)
# cv2.imwrite(name, prev_frame)

