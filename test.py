import difflib

#data fetch part
#data from AccuWeather for Kochi with center as 18 Jul
pastWeek=[30,30,31,30,31,31,31]
pastYearFortnyt=[32,32,32,32,29,31,28,30,27,29,29,28,30,30,30]

start = range(len(pastYearFortnyt) + 1)
stop = start[7:]
L = [pastYearFortnyt[i:j] for i, j in zip(start, stop)]

similarity = 0

for 
sm = difflib.SequenceMatcher(None,pastWeek,L1)
similarity = sm.ratio()

sm=difflib.SequenceMatcher(None,pastWeek,L2)
if sm.ratio()>similarity:
	similarity = sm.ratio()
else


