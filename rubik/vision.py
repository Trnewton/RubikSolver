from ctypes.wintypes import PLARGE_INTEGER
import cv2

import numpy as np
from sklearn.mixture import BayesianGaussianMixture as BGMM
from sklearn.cluster import KMeans

from matplotlib import pyplot as plt
from matplotlib.axes import Axes

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


def main():
    pass



if __name__ == '__main__':
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




