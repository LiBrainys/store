'''
    1、准备商品
    2、空的购物车
    3、钱包初始化金钱
    4、最后打印购物小条
    1、业务：
    看到商品
        商品存在
            看金钱够
                成功加入购物车
                余额减去对应价格
            不够
                穷鬼，去买其他商品
            商品不存在
                输入错误
            输入Q或q，退出并结算。打印小条
        任务：尽量多的添加商品
        任务：10个辣条优惠券（0.3折），20个机械革命优惠券（0.9折）
            在进入商城时，随机抽取优惠券，在最后结算使用该优惠券
'''
# 1、商品
import random
shop = [
    ["机械革命", 15000],
    ["HUAWEI watch", 1200],
    ["MAC PC", 13000],
    ["Iphone 54 plus", 45000],
    ["辣条", 2.5],
    ["老干妈", 13],
    ["机械师", 9000],
    ["vivo手机", 2000],
    ["水杯", 20],
    ["Apple mac", 8888],
    ["联想小新", 5499],
    ["惠普战66", 4799],
    ["荣耀笔记本", 3999],
    ["酷耶", 3399],
    ["攀升", 1999],
    ["华为 P40", 5999],
    ["红米", 4999],
    ["LG gram", 9999],
    ["iphone 12", 6799],
    ["redmi 9A", 599],
    ["一加9", 3499],
    ["OPPO", 2999]
]
# 2、初始化钱包余额
money = input("请输入您的钱包余额：")
money = int(money)

# 优惠券集合
'''lat = 0
while True:
    if lat >= 10:
        lat.append("辣条3折优惠券")
    elif jxgm >= 20:
        '''
favorable = [

    {
        'name': "抽中辣条3折优惠券",
        'zhekou': 0.3
    },
    {
        'name': "抽中辣条3折优惠券",
        'zhekou': 0.3
    },
    {
        'name': "抽中辣条3折优惠券",
        'zhekou': 0.3
    },
    {
        'name': "抽中辣条3折优惠券",
        'zhekou': 0.3
    },
    {
        'name': "抽中辣条3折优惠券",
        'zhekou': 0.3
    },
    {
        'name': "抽中辣条3折优惠券",
        'zhekou': 0.3
    },
    {
        'name': "抽中辣条3折优惠券",
        'zhekou': 0.3
    },
    {
        'name': "抽中辣条3折优惠券",
        'zhekou': 0.3
    },
    {
        'name': "抽中辣条3折优惠券",
        'zhekou': 0.3
    },
    {
        'name': "抽中辣条3折优惠券",
        'zhekou': 0.3
    },
    {
        'name': "抽中辣条3折优惠券",
        'zhekou': 0.3
    },
    {
        'name': "抽中机械革命9折优惠券",
        'zhekou': 0.9
    },
    {
        'name': "抽中机械革命9折优惠券",
        'zhekou': 0.9
    },
    {
        'name': "抽中机械革命9折优惠券",
        'zhekou': 0.9
    },
    {
        'name': "抽中机械革命9折优惠券",
        'zhekou': 0.9
    },
    {
        'name': "抽中机械革命9折优惠券",
        'zhekou': 0.9
    },
    {
        'name': "抽中机械革命9折优惠券",
        'zhekou': 0.9
    },
    {
        'name': "抽中机械革命9折优惠券",
        'zhekou': 0.9
    },
    {
        'name': "抽中机械革命9折优惠券",
        'zhekou': 0.9
    },
    {
        'name': "抽中机械革命9折优惠券",
        'zhekou': 0.9
    },
    {
        'name': "抽中机械革命9折优惠券",
        'zhekou': 0.9
    },
    {
        'name': "抽中机械革命9折优惠券",
        'zhekou': 0.9
    },
    {
        'name': "抽中机械革命9折优惠券",
        'zhekou': 0.9
    },
    {
        'name': "抽中机械革命9折优惠券",
        'zhekou': 0.9
    },
    {
        'name': "抽中机械革命9折优惠券",
        'zhekou': 0.9
    },
    {
        'name': "抽中机械革命9折优惠券",
        'zhekou': 0.9
    },
    {
        'name': "抽中机械革命9折优惠券",
        'zhekou': 0.9
    },
    {
        'name': "抽中机械革命9折优惠券",
        'zhekou': 0.9
    },
    {
        'name': "抽中机械革命9折优惠券",
        'zhekou': 0.9
    },
    {
        'name': "抽中机械革命9折优惠券",
        'zhekou': 0.9
    },
    {
        'name': "抽中机械革命9折优惠券",
        'zhekou': 0.9
    }
]

yh = 0
while True:
    if money <= 0:
        money = input("请输入你的钱包余额：")
        money = int(money)
    else:
        cj = random.randint(0, 29)
        # print(cj)
        print(favorable[cj]['name'])
        # print("恭喜您！抽中三折辣条优惠券")
        # print("恭喜您！抽中机械革命九折优惠券")
        break
# 3、准备一个空的购物车
mycart = []
# 4、买东西
while True:
    # 展示商品
        for index, value in enumerate(shop):    # 枚举，将角标和商品整体都打印
            print(index, "  ", value)
        # 请输入您要的商品
        chose = input("请输入您要的商品：")
        # 看是否存在
        if chose.isdigit():     # 是否能被看成数字:
            chose = int(chose)
            # 看商品是否存在
            if chose > len(shop) - 1:
                print("您要的商品不存在！")
            else:
                # 看钱是否足够
                if money > shop[chose][1] == 15000:
                    mycart.append(shop[chose])
                    # 钱减去
                    money = money - shop[chose][1]*0.9
                    '''if shop[chose][1] == 15000:
                        money = money - spice'''
                    print("恭喜，成功添加购物车，您的余额还剩：", money)
                elif money > shop[chose][1] == 2.5 :
                    mycart.append(shop[chose])
                    # 钱减去
                    money = money - shop[chose][1] * 0.3
                    print("恭喜，成功添加购物车，您的余额还剩：", money)
                elif money > shop[chose][1]:
                    mycart.append(shop[chose])
                    money = money - shop[chose][1]
                    print("恭喜，成功添加购物车，您的余额还剩：", money)
                else:
                    print("对不起，穷鬼，余额不足，请去购买其他商品！")
        elif chose == 'q' or chose == 'Q':
            print("欢迎下次光临！")
            break
        else:
            print("对不起，您输入的商品不存在，请重新输入！")
#  5、打印小条
print("下面时您的购物小条，请拿好：")
for index, value in enumerate(mycart):
    print(index, " ", value)
    print("您的钱包还剩：￥", money)