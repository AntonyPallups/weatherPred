import difflib
s1=[1,8,3,9,4,9,3,8,1,2,3]
s2=[1,8,1,3,9,4,9,3,8,1,2,3]
sm=difflib.SequenceMatcher(None,s1,s2)
print sm.ratio()
