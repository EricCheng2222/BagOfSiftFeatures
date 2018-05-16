



import math
import cv2
import numpy as np 
import glob, os



















fileList = []
keypointList = []
dirList = getAllDirIn("")

#readDir
for dir in dirList:
	tmp = getAllFileIn(dir)
	fileList.append(tmp)

#readImg, extractFeature and use Kmean to extract important feature
importantFeatureList = []
for pictureList in fileList:
	oneCateFeatureList = []
	for picture in pictureList:
		keypoint = extractKeypoint(picture)
		tmpFeatureList = extractFeatureFrom(keypoint)
		oneCateFeatureList.append(tmpFeatureList)
	oneCateImportantFeature = kmean(oneCateFeatureList)
	importantFeatureList.append(oneCateImportantFeature)

#readTestImage
for image in testImage:
	cateLabel = 1
	currentLabel = 0
	currentScore = 255*10*10
	for importantFeature in importantFeatureList:
		cmpScore = score(image, importantFeature)
		if currentScore > cmpScore:
			currentLabel = cateLabel
			currentScore = cmpScore
		cateLabel = cateLabel + 1
	print (currentLabel, currentScore)



