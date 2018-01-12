import pandas as pd
import numpy as np
import pymongo,pymysql,requests,json
from config import *
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

client = pymongo.MongoClient(MONGO_URI, connect=False)
db = client[MONGO_DB]

bj=db.数据分析师.find({'gzdd':'北京'})
beijing=[]
for data1 in bj:
    beijing.append(data1)
print(len(beijing))


sh=db.数据分析师.find({'gzdd':'上海'})
shanghai=[]
for data2 in sh:
    shanghai.append(data2)
print(len(shanghai))


gz=db.数据分析师.find({'gzdd':'广州'})
guangzhou=[]
for data3 in gz:
    guangzhou.append(data3)
print(len(guangzhou))


sz=db.数据分析师.find({'gzdd':'深圳'})
shenzhen=[]
for data4 in sz:
    shenzhen.append(data4)
print(len(shenzhen))

tj=db.数据分析师.find({'gzdd':'天津'})
tianjing=[]
for data5 in tj:
    tianjing.append(data5)
print(len(tianjing))


wh=db.数据分析师.find({'gzdd':'武汉'})
wuhan=[]
for data6 in wh:
    wuhan.append(data6)
print(len(wuhan))


xa=db.数据分析师.find({'gzdd':'西安'})
xian=[]
for data7 in xa:
    xian.append(data7)
print(len(xian))


cd= db.数据分析师.find({'gzdd': '成都'})
chengdu=[]
for data8 in cd:
    chengdu.append(data8)
# print(len(chengdu))

hz= db.数据分析师.find({'gzdd': '杭州'})
hangzhou=[]
for data9 in hz:
    hangzhou.append(data9)
# print(len(hangzhou))

cs= db.数据分析师.find({'gzdd': '长沙'})
changsha=[]
for data10 in cs:
    changsha.append(data10)
# print(len(changsha))

# 去各地区数据
bj_ms=[]
# 薪资高低区间
bj_lows=[]
bj_highs=[]
for bj in beijing:
    bj=bj['zwyx']
    bj=bj.split('-')
    if len(bj)==2:
        bj_lows.append(bj[0])
        bj_highs.append(bj[1])
        bj_m=(int(bj[0])+int(bj[1]))/2
        bj_ms.append(bj_m)
bj_sum=0
for i in bj_ms:
    bj_sum = bj_sum + i
num= len(bj_ms)
bj_average=int(bj_sum/num)
bj_high=sorted(bj_highs)[-1]
bj_low = sorted(bj_lows)[0]
bj_num=len(beijing)



sh_ms=[]
sh_lows=[]
sh_highs=[]
for sh in shanghai:
    sh=sh['zwyx']
    sh=sh.split('-')

    if len(sh)==2:
        sh_lows.append(sh[0])
        sh_highs.append(sh[1])
        sh_m=(int(sh[0])+int(sh[1]))/2
        sh_ms.append(sh_m)
sh_sum=0
for i in sh_ms:
    sh_sum = sh_sum + i
num= len(sh_ms)
sh_average=int(sh_sum/num)
sh_high=sorted(sh_highs)[-1]
sh_low = sorted(sh_lows)[0]
sh_num=len(shanghai)

gz_ms=[]
gz_lows=[]
gz_highs=[]
for gz in guangzhou:
    gz=gz['zwyx']
    gz=gz.split('-')

    if len(gz)==2:
        gz_lows.append(gz[0])
        gz_highs.append(gz[1])
        gz_m=(int(gz[0])+int(gz[1]))/2
        gz_ms.append(gz_m)
gz_sum=0
for i in gz_ms:
    gz_sum = gz_sum + i
num= len(gz_ms)
gz_average=int(gz_sum/num)
gz_high=sorted(gz_highs)[-1]
gz_low = sorted(gz_lows)[0]
gz_num = len(guangzhou)

sz_ms=[]
sz_lows=[]
sz_highs=[]
for sz in shenzhen:
    sz=sz['zwyx']
    sz=sz.split('-')
    if len(sz)==2:
        sz_lows.append(sz[0])
        sz_highs.append(sz[1])
        sz_m=(int(sz[0])+int(sz[1]))/2
        sz_ms.append(sz_m)
sz_sum=0
for i in sz_ms:
    sz_sum = sz_sum + i
num= len(sz_ms)
sz_average=int(sz_sum/num)
sz_high=sorted(sz_highs)[-1]
sz_low = sorted(sz_lows)[0]
sz_num=len(shenzhen)

tj_ms=[]
tj_lows=[]
tj_highs=[]
for tj in tianjing:
    tj=tj['zwyx']
    tj=tj.split('-')

    if len(tj)==2:
        tj_lows.append(tj[0])
        tj_highs.append(tj[1])
        tj_m=(int(tj[0])+int(tj[1]))/2
        tj_ms.append(tj_m)
tj_sum=0
for i in tj_ms:
    tj_sum = tj_sum + i
num= len(tj_ms)
tj_average=int(tj_sum/num)
tj_high=sorted(tj_highs)[-1]
tj_low = sorted(tj_lows)[0]
tj_num =len(tianjing)


wh_ms=[]
wh_lows=[]
wh_highs=[]
for wh in wuhan:
    wh=wh['zwyx']
    wh=wh.split('-')
    if len(wh)==2:
        wh_lows.append(wh[0])
        wh_highs.append(wh[1])
        wh_m=(int(wh[0])+int(wh[1]))/2
        wh_ms.append(wh_m)
wh_sum=0
for i in wh_ms:
    wh_sum = wh_sum + i
num= len(wh_ms)
wh_average=int(wh_sum/num)
wh_high=sorted(wh_highs)[-1]
wh_low = sorted(wh_lows)[0]
wh_num = len(wuhan)

xa_ms=[]
xa_lows=[]
xa_highs=[]
for xa in xian:
    xa=xa['zwyx']
    xa=xa.split('-')
    if len(xa)==2:
        xa_lows.append(xa[0])
        xa_highs.append(xa[1])
        xa_m=(int(xa[0])+int(xa[1]))/2
        xa_ms.append(xa_m)
xa_sum=0
for i in xa_ms:
    xa_sum = xa_sum + i
num= len(xa_ms)
xa_average=int(xa_sum/num)
xa_high=sorted(xa_highs)[-1]
xa_low = sorted(xa_lows)[0]
xa_num=len(xian)


cd_ms=[]
cd_lows=[]
cd_highs=[]
for cd in chengdu:
    cd=cd['zwyx']
    cd=cd.split('-')
    if len(cd)==2:
        cd_lows.append(cd[0])
        cd_highs.append(cd[1])
        cd_lows.append(cd[0])
        cd_highs.append(cd[1])
        cd_m=(int(cd[0])+int(cd[1]))/2
        cd_ms.append(cd_m)
cd_sum=0
for i in cd_ms:
    cd_sum = cd_sum + i
num= len(cd_ms)
cd_average=int(cd_sum/num)
cd_high=sorted(cd_highs)[-1]
cd_low = sorted(cd_lows)[0]
cd_num=len(chengdu)


hz_ms=[]
hz_lows=[]
hz_highs=[]
for hz in hangzhou:
    hz=hz['zwyx']
    hz=hz.split('-')
    if len(hz)==2:
        hz_lows.append(hz[0])
        hz_highs.append(hz[1])
        hz_m=(int(hz[0])+int(hz[1]))/2
        hz_ms.append(hz_m)
hz_sum=0
for i in hz_ms:
    hz_sum = hz_sum + i
num= len(hz_ms)
hz_average=int(hz_sum/num)
hz_high=sorted(hz_highs)[-1]
hz_low = sorted(hz_lows)[0]
hz_num=len(hangzhou)


cs_ms=[]
cs_lows=[]
cs_highs=[]
for cs in changsha:
    cs=cs['zwyx']
    cs=cs.split('-')

    if len(cs)==2:
        cs_lows.append(cs[0])
        cs_highs.append(cs[1])
        cs_m=(int(cs[0])+int(cs[1]))/2
        cs_ms.append(cs_m)
cs_sum=0
for i in cs_ms:
    cs_sum = cs_sum + i
num= len(cs_ms)
cs_average=int(cs_sum/num)
cs_high=sorted(cs_highs)[-1]
cs_low = sorted(cs_lows)[0]
cs_num=len(changsha)


# print(cs_average)

# plt.rcParams['font.sas-serig']=['simhei'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

# # 薪资水平柱状图
y1=[bj_average,sh_average,gz_average,sz_average,tj_average,wh_average,xa_average,cd_average,hz_average,cs_average]
x1=[ 'bj', 'sh', 'gz', 'sz',
           'tj', 'wh', 'xa', 'cd','hz','cs']
plt.bar(x1,y1,label='moneny level')
#plt.bar(x2,y2,label='second line',color='r')
plt.xlabel('area')
plt.ylabel('money')
plt.title('area-money')
plt.legend()
plt.show()


# 薪资水平折线图
y1=[bj_average,sh_average,gz_average,sz_average,tj_average,wh_average,xa_average,cd_average,hz_average,cs_average]
x1=[ 'bj', 'sh', 'gz', 'sz',
           'tj', 'wh', 'xa', 'cd','hz','cz']

plt.plot(x1,y1,label='money',linewidth=3,color='r',marker='o',
markerfacecolor='blue',markersize=12)
plt.xlabel('area')
plt.ylabel('money')
plt.title('area-money')
plt.legend()
plt.show()


# 薪资区间柱状图

population_ages = [bj_high,bj_low,sh_high,sh_low,gz_high,gz_low,sz_high,sz_lows,tj_high,tj_low,wh_high,wh_low,xa_high,xa_low,cd_high,cd_low,hz_high,hz_low,cs_high,cs_low]
x=[ 'bj', 'sh', 'gz', 'sz',
           'tj', 'wh', 'xa', 'cd','hz','cz']

y1=[10,13,5,40,30,60,70,12,55,25]
x1=range(0,20,2)
x2=range(1,21,2)
y2=[5,8,0,30,20,40,50,10,40,15]
plt.bar(x1,y1,label='money')
#plt.bar(x2,y2,label='second line',color='r')
plt.xlabel('area')
plt.ylabel('money')
plt.title('area-money')
plt.legend()
plt.show()

y1=[bj_high,sh_high,gz_high,sz_high,tj_high,wh_high,xa_high,cd_high,hz_high,cs_high]
x1=range(0,20,2)
x2=range(1,21,2)
y2=[bj_low,sh_low,gz_low,sz_low,tj_low,wh_low,xa_low,cd_low,hz_low,cs_low]
plt.bar(x1,y1,label='high',color='b')
plt.bar(x2,y2,label='low',color='r')
plt.xlabel('area')
plt.ylabel('money')
plt.title('high-low')
plt.legend()
plt.show()


# # 职位需求量柱状图
y1=[bj_num,sh_num,gz_num,sz_num,tj_num,wh_num,xa_num,cd_num,hz_num,cs_num]
x1=[ 'bj', 'sh', 'gz', 'sz',
           'tj', 'wh', 'xa', 'cd','hz','cs']
plt.bar(x1,y1,label='moneny level')
#plt.bar(x2,y2,label='second line',color='r')
plt.xlabel('area')
plt.ylabel('require')
plt.title('require sum')
plt.legend()

