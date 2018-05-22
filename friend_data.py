# -*- coding:utf-8 -*-
import itchat
import numpy as np
import matplotlib.pyplot as plt


# 绘制性别分布柱形图
def draw_gender_distribution(fig, g_plt, x, y1, y2):
    fig.add_subplot(2, 2, 1)
    g_plt.title("The sex distribution of kikoxxxi's friends")
    ax = g_plt.gca()
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    g_plt.bar(x, +y1, color=['r', '#ffad73', '#ff6840'],
              edgecolor='white', alpha=0.6)
    g_plt.bar(x, -y2, color=['r', '#ffad73', '#ff6840'],
              edgecolor='white', alpha=0.4)
    g_plt.yticks(np.linspace(-100, 200, 7, endpoint=True))
    xy1 = zip(x, y1)
    xy2 = zip(x, y2)
    for x, y1 in xy1:
        g_plt.text(x, y1, '%s' % y1, ha='center', va='bottom')
    for x, y2 in xy2:
        g_plt.text(x, -y2 - 5, '%s%%' % y2, ha='center', va='top')
    g_plt.ylabel("Number & Proportion")


# 绘制city分布柱形图
def draw_city_distribution(fig, g_plt, x, y1):
    fig.add_subplot(2, 2, 2)
    plt.title("The city distribution of kikoxxxi's friends")
    ax = plt.gca()
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    plt.bar(x, +y1, color=['r', '#ffad73', '#ff6840', '#60b9ce', '#ab2b52'],
            edgecolor='white', alpha=0.6)
    plt.yticks(np.linspace(0, 100, 11, endpoint=True))
    xy1 = zip(x, y1)
    for x, y1 in xy1:
        plt.text(x, y1, '%s' % y1, ha='center', va='bottom')
    plt.ylabel("Number")


def main():
    itchat.auto_login(hotReload=True)
    friends = itchat.get_friends(update=True)[0:]

    # 计算各性别的人数以及各城市分布人数
    male = female = other = 0
    city_dict = {}
    for friend in friends[1:]:
        sex = friend["Sex"]
        if sex == 1:
            male += 1
        elif sex == 2:
            female += 1
        else:
            other += 1
        city = friend["City"]
        if city:
            if city_dict.get(city, None):
                city_dict[city] += 1
            else:
                city_dict[city] = 1

    # 总人数
    total = len(friends) - 1
    # 各性别人数的占比
    male_pro = round((male / total) * 100, 2)
    female_pro = round((female / total) * 100, 2)
    other_pro = round((other / total) * 100, 2)
    # 数据准备
    x = np.array(["male", "female", "other"])
    y1 = np.array([male, female, other])
    y2 = np.array([male_pro, female_pro, other_pro])
    # 绘制性别分布柱形图
    fig = plt.figure()
    plt.rcParams['font.sans-serif'] = ['SimHei']
    draw_gender_distribution(fig, plt, x, y1, y2)

    # 数据准备
    city_sort = sorted(city_dict.items(),
                       key=lambda asd: asd[1], reverse=True)  # 按频率降序
    city_list, number_list = [], []
    for item in city_sort[:10]:
        city_list.append(item[0])
        number_list.append(item[1])
    x = np.array(city_list)
    y1 = np.array(number_list)
    # 绘制city分布柱形图
    draw_city_distribution(fig, plt, x, y1)
    plt.show()


if __name__ == "__main__":
    main()
