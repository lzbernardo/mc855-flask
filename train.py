import sys

import numpy as np
import cv2


def flatten(img):
    return img.reshape((1,img.shape[0]*img.shape[1]))

samples =  np.empty((0,54))
responses = []
keys = [i for i in range(48,58)]

for i in range(0,660):
    im = cv2.imread('training_data/numbers/roi-%s.png' % i)
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    cv2.imshow('norm',im)
    key = cv2.waitKey(0)
    print(i)
    if key == 27:  # (escape to quit)
        sys.exit()
    elif key in keys:
        responses.append(int(chr(key)))
        sample = np.float32(flatten(gray))
        samples = np.append(samples,sample,0)

responses = np.array(responses,np.float32)
responses = responses.reshape((responses.size,1))
print("training complete")

np.savetxt('generalsamples.data',samples)
np.savetxt('generalresponses.data',responses)
