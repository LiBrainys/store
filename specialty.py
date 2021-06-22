# 特产
# 1号商品
date1 = "1号"
rig1 = "过油肉"
price1 = 10
stock1 = 500
# 2号商品
date2 = "2号"
rig2 = "红果"
price2 = 5
stock2 = 300
# 3号商品
date3 = "3号"
rig3 = "烧大葱"
price3 = 8
stock3 = 3000
# 4号商品
date4 = "4号"
rig4 = "李圪抓"
price4 = 15
stock4 = 1000
# 5号商品
date5 = "5号"
rig5 = "糖醋溜丸"
price5 = 20
stock5 = 600
# 6号商品
date6 = "6号"
rig6 = "阳城烧肝"
price6 = 18
stock6 = 600
# 7号商品
date7 = "7号"
rig7 = "泽州甜柿"
price7 = 7
stock7 = 700
# 8号商品
date8 = "8号"
rig8 = "油糊角"
price8 = 13
stock8 = 900
# 9号商品
date9 = "9号"
rig9 = "毛头丸"
price9 = 14
stock9 = 900
print("-------------------山西晋城特产----------------------")
print("日期             名称               价格/件         销量     ")
print(date1,"\t\t\t\t",rig1,"\t\t\t\t",price1,"\t\t\t",stock1,"\t\t\t")
print(date2,"\t\t\t\t",rig2,"\t\t\t\t",price2,"\t\t\t",stock2,"\t\t\t")
print(date3,"\t\t\t\t",rig3,"\t\t\t\t",price3,"\t\t\t",stock3,"\t\t\t")
print(date4,"\t\t\t\t",rig4,"\t\t\t\t",price4,"\t\t\t",stock4,"\t\t\t")
print(date5,"\t\t\t\t",rig5,"\t\t\t\t",price5,"\t\t\t",stock5,"\t\t\t")
print(date6,"\t\t\t\t",rig6,"\t\t\t\t",price6,"\t\t\t",stock6,"\t\t\t")
print(date7,"\t\t\t\t",rig7,"\t\t\t\t",price7,"\t\t\t",stock7,"\t\t\t")
print(date8,"\t\t\t\t",rig8,"\t\t\t\t",price8,"\t\t\t",stock8,"\t\t\t")
print(date9,"\t\t\t\t",rig9,"\t\t\t\t",price9,"\t\t\t",stock9,"\t\t\t")
sum = price1*stock1 + price2*stock2 + price3*stock3 + price4*stock4 + price5*stock5 + price6*stock6 + price7*stock7 + price8*stock8 + price9*stock9
print("特产销售总金额：￥", sum)

gyr = (price1 * stock1)/sum
print("回锅肉销售占比：￥", round(gyr, 4) * 100, "%")
hg = (price2 * stock2)/sum
print("红果销售占比：￥", round(hg, 4) * 100, "%")
sdc = (price3 * stock3)/sum
print("烧大葱销售占比：￥", round(sdc, 4) * 100, "%")
lgz = (price4 * stock4)/sum
print("李圪抓销售占比：￥", round(lgz * 100, 2), "%")
tclw = (price5 * stock5)/sum
print("糖醋溜丸销售占比：￥", round(tclw, 4) * 100, "%")
ycsg = (price6 * stock6)/sum
print("阳城烧肝销售占比：￥", round(ycsg, 4) * 100, "%")
zzts = (price7 * stock7)/sum
print("泽州甜柿销售占比：￥", round(zzts * 100, 2), "%")
yhj = (price8 * stock8)/sum
print("油糊角销售占比：￥", round(yhj, 4) * 100, "%")
mtw = (price9 * stock9)/sum
print("毛头丸销售占比：￥", round(mtw * 100, 2), "%")