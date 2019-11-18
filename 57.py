# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 21:39:03 2019

@author: vip
"""

class Solution(object):
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort()
        flag=[[intervals[0][0],intervals[0][1]]]
        for i in range (1,len(intervals)):
            if intervals[i][0]>=flag[-1][0] and intervals[i][1]<= flag[-1][1]:
                continue
            elif intervals[i][0]>=flag[-1][0] and intervals[i][0]<=flag[-1][1]:
                flag.append([flag[-1][0],intervals[i][1]])
                flag.pop(len(flag)-2)
            else:
                flag.append(intervals[i])
        print(flag)                          
ss=Solution()
#intervals = [[1,3],[6,9]]
#newInterval = [2,5]
#intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
#newInterval = [0,8]
intervals =[[0,0]]
newInterval =[0,0]
#intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
#newInterval = [4,8]
s=ss.insert(intervals,newInterval)
