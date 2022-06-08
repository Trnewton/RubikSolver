from ctypes.wintypes import PLARGE_INTEGER
from http.client import UNSUPPORTED_MEDIA_TYPE
import cv2

import numpy as np
from sklearn.mixture import BayesianGaussianMixture as BGMM
from sklearn.cluster import KMeans

from matplotlib import pyplot as plt

COLOUR_MASKS = {
    'w' : ((0, 0, 220), (179, 15, 359)),
    'g' : ((50, 130, 180), (60, 160, 210)),
    'r' : ((170, 160, 200), (10, 240, 240)),
    'b' : ((105, 45, 190), (140, 255, 255)),
    'y' : ((25, 140, 210), (40, 255, 255)),
    'o' : ((5, 120, 210), (20, 255, 255))
}

MAX_HUE = 179
MAX_SAT = 255
MAX_VAL = 255

def plot_4filters(img):

    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)
    img_edge = cv2.Canny(img_blur, 100, 400)

    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(16,16))

    axs[0,0].imshow(img)
    axs[0,1].imshow(img_gray)
    axs[1,0].imshow(img_blur)
    axs[1,1].imshow(img_edge)

    [axi.set_axis_off() for axi in axs.ravel()]

    plt.show()

def plot_line_segments(img):
    lines = cv2.detect(img)[0]
    img_lines = cv2.drawSegments(img, lines)

    plt.figure(figsize=(16,16))
    plt.imshow(img_lines)
    plt.show()

def hsv_vis(path, start_vals=None):
    ''''''

    img = cv2.imread(path)
    img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    win_name = 'HSV Mask'
    if start_vals is None:
        start_vals = ((0, 0, 0), (MAX_HUE, MAX_SAT, MAX_VAL))

    def _on_tracker(val):
        h_min = cv2.getTrackbarPos('Hue Min', win_name)
        h_max = cv2.getTrackbarPos('Hue Max', win_name)
        s_min = cv2.getTrackbarPos('Sat Min', win_name)
        s_max = cv2.getTrackbarPos('Sat Max', win_name)
        v_min = cv2.getTrackbarPos('Val Min', win_name)
        v_max = cv2.getTrackbarPos('Val Max', win_name)

        # Check for wrapping hue range
        if h_min > h_max:
            mask_1 = cv2.inRange(img_HSV, (h_min, s_min, v_min), (MAX_HUE, s_max, v_max))
            mask_2 = cv2.inRange(img_HSV, (0, s_min, v_min), (h_max, s_max, v_max))
            mask = mask_1 | mask_2
        else:
            mask = cv2.inRange(img_HSV, (h_min, s_min, v_min), (h_max, s_max, v_max))
        cv2.imshow(win_name, mask)

    cv2.namedWindow('Original', 0)
    cv2.imshow('Original', img)
    cv2.resizeWindow('Original',400,400)

    cv2.namedWindow(win_name, 0)
    cv2.resizeWindow(win_name,400,400)

    cv2.createTrackbar('Hue Min', win_name, start_vals[0][0], MAX_HUE, _on_tracker)
    cv2.createTrackbar('Hue Max', win_name, start_vals[1][0], MAX_HUE, _on_tracker)
    cv2.createTrackbar('Sat Min', win_name, start_vals[0][1], MAX_SAT, _on_tracker)
    cv2.createTrackbar('Sat Max', win_name, start_vals[1][1], MAX_SAT, _on_tracker)
    cv2.createTrackbar('Val Min', win_name, start_vals[0][2], MAX_VAL, _on_tracker)
    cv2.createTrackbar('Val Max', win_name, start_vals[1][2], MAX_VAL, _on_tracker)

    _on_tracker(0)

    cv2.waitKey(0)

def HSV_mask(img, HSV_range):
    # Check for wrapping hue range
    if HSV_range[0][0] > HSV_range[1][0]:
        mask_1 = cv2.inRange(img, HSV_range[0], (MAX_HUE, HSV_range[1][1], HSV_range[1][2]))
        mask_2 = cv2.inRange(img, (0, HSV_range[0][1], HSV_range[0][2]), HSV_range[1])
        mask = mask_1 | mask_2
    else:
        mask = cv2.inRange(img, HSV_range[0], HSV_range[1])

    return mask

def read_face(face):
    face_HSV = cv2.cvtColor(face, cv2.COLOR_BGR2HSV)
    # for each colour get contours with position and label data then take 9 largest contours
    store = []
    for colour, HSV_range in COLOUR_MASKS.items():
        mask = HSV_mask(face_HSV, HSV_range)
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        store += [(c, colour) for c in contours]

    store = sorted(store, key=lambda val: cv2.contourArea(val[0]), reverse=True)
    # use 9 largest contours to get orientation and relative positions

    _ = cv2.drawContours(face, [cont for cont,_ in store][:9], -1,  (0,255,0), 3)

    for cont, colour in store[:9]:
        M = cv2.moments(cont)
        x, y = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
        print(x, y, colour)
        cv2.circle(face, (x, y), 50, (0,0,0),-1)

    cv2.namedWindow('Foo', 0)
    cv2.resizeWindow('Foo',400,400)
    cv2.imshow('Foo', face)
    cv2.waitKey(0)

def main():
    img_dir = '../img/'
    colours = [f'w_{n}' for n in range(1,7)]

    imgs = []
    for colour in colours:
        img_name = f'{colour}.jpg'
        img = cv2.imread(img_dir + img_name)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        img_blur = cv2.GaussianBlur(img, (5,5), 100)
        img_blur = cv2.resize(img_blur, (256, 256))

        imgs.append(img_blur)

        # fig, axs = plt.subplots(ncols=2, figsize=(16,8))
        # axs[0].imshow(img)
        # axs[1].hist(img.flatten(), bins=100)
        # plt.show()

    full_sample = np.array(imgs)
    full_sample = full_sample.reshape((-1,3))

    bgm_model = KMeans(n_clusters=10).fit(full_sample)

    fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(16,24))
    for i, img in enumerate(imgs):
        axs[i%3, i//3].imshow(img)
        axs[i%3, i//3].set_title(f'{colours[i]}')
        axs[i%3, i//3].axis('off')

    fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(16,24))
    for i, img in enumerate(imgs):
        bgm_labels = bgm_model.predict(img.reshape((-1,3)))
        segments = bgm_labels.reshape(img.shape[0], img.shape[1])

        axs[i%3, i//3].imshow(segments)
        axs[i%3, i//3].set_title(f'{colours[i]}')
        axs[i%3, i//3].axis('off')

    fig, axs = plt.subplots(nrows=3, ncols=2, figsize=(16,24))
    for i, img in enumerate(imgs):
        edges = cv2.Canny(img, 50, 200, 255)


        axs[i%3, i//3].imshow(edges)
        axs[i%3, i//3].set_title(f'{colours[i]}')
        axs[i%3, i//3].axis('off')

    plt.show()

if __name__ == '__main__':
    img_arr = [f'../img/{val}.jpg' for val in range(1, 2)]
    for img_name in img_arr:
        img = cv2.imread(img_name)
        read_face(img)