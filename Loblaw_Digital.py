
# coding: utf-8

# In[4]:


import timeit
import cv2
import numpy as np


# In[5]:


import pandas
df = pandas.read_csv('/Users/sarthakkatyal/Desktop/Loblaw_Assignment.csv')


# In[6]:


k = 0
while df['Img1'][k] != None or df['Img2'][k] != None:
    start_time = timeit.default_timer()
    first = df['Img1'][k]
    second = df['Img2'][k]
    
    print(first)
    print(second)
    
    original = cv2.imread(first)
    image_to_compare = cv2.imread(second)
    
    if original.shape == image_to_compare.shape:
        #print("The images have same size and channels")
        difference = cv2.subtract(original, image_to_compare)
        b, g, r = cv2.split(difference)
        
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
             print("The images are equal")
        else:
            print("The images are NOT equal")
        
    sift = cv2.xfeatures2d.SIFT_create()
    kp_1, desc_1 = sift.detectAndCompute(original, None)
    kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)
    
    index_params = dict(algorithm=0, trees=5)
    search_params = dict()
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    
    matches = flann.knnMatch(desc_1, desc_2, k=2)
    
    good_points = []
    ratio = 0.5
    for m, n in matches:
        if m.distance < ratio*n.distance:
            good_points.append(m)
    #print(len(good_points))
    result = cv2.drawMatches(original, kp_1, image_to_compare, kp_2, good_points, None)
    
    all_points = []
    for i, j in matches:
        if i.distance < j.distance:
            all_points.append(i)
    #print(len(all_points))
    result = cv2.drawMatches(original, kp_1, image_to_compare, kp_2, good_points, None)
    
    ratio_good = len(good_points)/len(all_points)
    similarity = 1 - ratio_good
    #print(similarity)
    
    elapsed = timeit.default_timer() - start_time
    #print(elapsed)
    
    df['Similarity'][k] = similarity
    df['Elapsed'][k] = elapsed
    df.to_csv('/Users/sarthakkatyal/Desktop/Loblaw_Assignment.csv')
    
    k = k + 1
    

