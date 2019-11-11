# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:17:08 2019

@author: ACER
"""

class Solution(object):
    def merge(self, intervals):
        if len(intervals)==0:
            return intervals
        intervals.sort()
        length = len(intervals)
        flag = [intervals[0][:]]
        for i in range (1,length):
            if flag[-1][0] <= intervals[i][0] and flag[-1][1] >= intervals[i][1]:
                continue
            if intervals[i][0]>= flag[-1][0] and intervals[i][0] <=flag[-1][1]:
                flag.append([flag[-1][0],intervals[i][1]])
                index=len(flag)- 2 
                flag.pop(index)
            else:
                flag.append([intervals[i][0],intervals[i][1]])
        print(flag)
#        print(flag[-1][0])
                
                
    
ss=Solution()
intervals=[[2,2],[2,2],[1,3]]
#intervals=[[1,3],[2,5],[3,4],[8,10],[15,18]]
#intervals=[[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
s=ss.merge(intervals)
#print(s)
