# -*- coding: utf-8 -*-
# =============================================================================
# #4.时间下一秒
# timeStr = input()
# #格式：  12:36:22
# timeList = timeStr.split(":")
# 
# hour = int(timeList[0])
# minute = int(timeList[1])
# second = int(timeList[2])
# 
# second += 1
# if second == 60:
#     minute += 1
#     second = 0
#     if minute ==60:
#         hour += 1
#         minute = 0
#         if hour == 24:
#             hour = 0
# print("%.2d:%.2d:%.2d" %(hour,minute,second))
# 
# =============================================================================
#歌词解析
import time

musicLrc ='''[00:00.50]蔡健雅 - 依赖
[00:07.94]词、曲：蔡健雅、陶晶莹
[00:11.60]关了灯把房间整理好
[00:15.48]凌晨三点还是睡不著
[00:19.64]你应该是不在　所以把电话挂掉
[00:30.39]在黑暗手表跟着心跳
[00:34.57]怎么慢它停也停不了
[00:39.70]我应该只是心情不好
[00:45.00]那又怎样
[00:48.50]但本来是这样
[01:21.36]朋友们对我的安慰
[01:25.20]都是同样的一个话题
[01:29.73]我一定要变得更坚强
[01:34.68]说很简单
[00:38.50]但是做却很难
[00:53.00][01:43.88][02:11.23]虽然无所谓写在脸上
[00:58.21][01:48.44][02:15.79]我还是舍不得让你离开
[01:02.97][01:53.50][02:20.60]虽然闭着眼假装听不到
[01:07.84][01:58.23][02:25.11][02:33.15]你对爱　已不再　想依赖
'''

musicLrcList = musicLrc.splitlines()

lrcDict = {}

for lrcLine in musicLrcList:
    lrcLineList = lrcLine.split("]")
    for index in range(len(lrcLineList) - 1):
        timeStr = lrcLineList[index][1:]
        #print(timeStr)
        #timeStr格式：02:33.15
        timeList =timeStr.split(":")
        time0 = float(timeList[0]) * 60 + float(timeList[1])
        lrcDict[time0] = lrcLineList[-1]
    
print(lrcDict)
        
allTimeList = []
for t in lrcDict:
    allTimeList.append(t)
allTimeList.sort()
#print(allTimeList)

'''
while 1:
    getTime = float(input("请输入时间："))
    
    for n in range(len(allTimeList)):
        tempTime = allTimeList[n]
        if getTime < tempTime:
            break
    if n == 0:
        print("时间太小")
    else:
        print(lrcDict[allTimeList[n - 1]])

'''


getTime = 0
while 1:  
    for n in range(len(allTimeList)):
        tempTime = allTimeList[n]
        if getTime < tempTime:
            break
    lrc = lrcDict.get(allTimeList[n - 1])
    if lrc == None:
        pass
    else:
        print(lrc)
    time.sleep(1)
    getTime += 3






































