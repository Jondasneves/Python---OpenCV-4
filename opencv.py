import cv2
import numpy as np

imagem = cv2.imread('imagem 4.jpg')

from matplotlib import pyplot as plt

imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

plt.imshow(imagem)
plt.show()