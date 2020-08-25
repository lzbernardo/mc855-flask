import sys

import numpy as np
import cv2


def flatten(img):
    return img.reshape((1,img.shape[0]*img.shape[1]))

model = cv2.ml.KNearest_create()
trainingdir = 'training_data/'
samples = np.loadtxt(trainingdir + 'MC855_sample.data', np.float32)
responses = np.loadtxt(trainingdir + 'MC855_resp.data', np.float32)
model.train(samples, cv2.ml.ROW_SAMPLE, responses)

counter = 0;
keys = [i for i in range(48,49)]

for i in range(0,401):
    im = cv2.imread('testdata/numbers/roi-%s.png' % i)
    flat_gray = flatten(cv2.cvtColor(im,cv2.COLOR_BGR2GRAY))
    float_vals = np.float32(flat_gray)
    nearest_float = model.findNearest(float_vals, k=1)[0]
    print("Prediction: ", str(int(nearest_float)))
    cv2.imshow('norm',im)
    key = cv2.waitKey(0)
    if key == 27:  # (escape to quit)
        sys.exit()
    elif key == 49:
        counter += 1
    if((i+1)%10 == 0):
        print(counter,"/",(i+1),"=",counter/(i+1))

print("testing complete, results: ", counter/i)
