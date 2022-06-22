import numpy as np
import matplotlib.pylab as plt


img = plt.imread("peppers.ppm")
imgr = np.zeros((512, 512), dtype=np.uint8)
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        imgr[x,y]=img[x,y,0]
plt.imshow(imgr,cmap='Reds')
plt.axis('off')
plt.title('peppers.ppm - Czerwony')
plt.show()

hist, bin_edges = np.histogram(imgr, bins=25)
plt.plot(bin_edges[0:-1], hist)
plt.title("peppers.ppm - histogram czerwonego")
plt.show()


imgg = np.zeros((512, 512), dtype=np.uint8)
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        imgg[x,y]=img[x,y,1]
plt.imshow(imgr,cmap='Greens')
plt.axis('off')
plt.title('peppers.ppm - Zielony')
plt.show()

hist, bin_edges = np.histogram(imgg, bins=25)
plt.plot(bin_edges[0:-1], hist)
plt.title("peppers.ppm - histogram zielonego")
plt.show()

imgb = np.zeros((512, 512), dtype=np.uint8)
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        imgb[x,y]=img[x,y,2]
plt.imshow(imgb,cmap='Blues')
plt.axis('off')
plt.title('peppers.ppm - Niebieski')
plt.show()

hist, bin_edges = np.histogram(imgb, bins=25)
plt.plot(bin_edges[0:-1], hist)
plt.title("peppers.ppm - histogram niebieskiego")
plt.show()
