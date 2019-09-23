# SIMILARITY_OF_IMAGES

## Methodology and Solution Approach

```
Case 1 
Images are SAME

	Condition 1
	Check if shape of both the images is equal. If equal, check condition 2

	Condition 2 
	If true, subtract both the images i.e. Image_1 and Image_2
	If B, G and R components after subtraction are zero, Condition 2 is satisfied

	If both Condition 1 and 2 are satisfied, we give similarity index = 0
	Else, move to Case 2

Case 2
Images are NOT SAME

	We use the approach of Feature Detection and Feature Matching here. 
	We find the features of both the images. 

	Step 1 : SIFT Algorithm is loaded 
	Step 2 : Key-points and descriptors of the original image and of the image to compare are found
	Step 3 : FlannBasedMatcher is loaded which is used to find matches between the descriptors of the 2 images.
	Step 4 : We store matches between the 2 images in array ‘matches’ which contains true as well as false matches
	Step 5 : Ratio Test is applied to select good matches. Distance is used to measure quality of a match. Therefore a lower number (representing distance) implies high similarity of features. 
	Step 6 : Assumption is to take only the matches with lower distance i.e. high quality (ratio is chosen as 0.5). These points are saved in good_points. When ratio is 1 i.e. all the points are saved in all_points.
	Step 7 : ratio_good is the ratio of good_points to all_points. This ratio represents the ratio of visual similarity in both the images. 
	Step 8 : similarity index is 0 for similar images hence similarity can be calculated as “1 - ratio_good”. Time elapsed can be calculated for each pair of image depending upon the execution time. 

```

## Installation Requirements

```
Language : Python, Version : 3

To run it, you need to install some packages and libraries as follows:
Opencv and opencv-python-contrib , version 3.4.2 
pandas
numpy

To install these, write this on the command line terminal:
"pip install package-name"
```

## To run

```
Clone this repo

In python Loblaw_Digital.py :
REPLACE 
df = pandas.read_csv(‘/Users/sarthakkatyal/Desktop/Loblaw_Assignment.csv') 
WITH
Path of the CSV File with image pairs

Open command line terminal

cd into this repo

Enter the command: "python Loblaw_Digital.py" 
```



This project was made by [Sarthak Katyal](https://github.com/sarthak409)
