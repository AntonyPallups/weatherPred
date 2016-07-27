import difflib
import math
import numpy

#data hardcoded from AccuWeather for Kochi with center as 18 Jul 2015/2016

#bracket of 11-Jul-2015 and 25-Jul-2015
pastYearFortnyt=[32,32,32,32,29,31,28,30,27,29,29,28,30,30,30]

#Fetching one more entry from past year. In case the last set is the most similar
theNextDay=30

#fetch last weeks data
pastWeek=[30,30,31,30,31,31,31]

#Splitting pastYearFortnyt to multiple sets with 7 items in each
start = range(len(pastYearFortnyt) + 1)
stop = start[7:]
L = [pastYearFortnyt[i:j] for i, j in zip(start, stop)]

#iterating through the sets and comparing with the current
#week to find the most similar set and the first value in the next set
similarity = 0
reqArray = 0
for x in xrange(9):
    sm = difflib.SequenceMatcher(None,pastWeek,L[x])
    if sm.ratio()>=similarity:
    	similarity = sm.ratio()
    	reqArray = x

if reqArray<8:
	lastYearTemp = L[reqArray+1][1]
else:
	lastYearTemp = theNextDay

#forecasting the next value
#ideally this next step should be done using a forecasting model. For now, I have used
#weighted average. Two thirds to yday's temp and one third to lastYearTemp
prediction = numpy.average([lastYearTemp,pastWeek[len(pastWeek)-1]],weights=[1./3, 2./3])

print "The temperature prediction for the next day is : " + str(prediction)
