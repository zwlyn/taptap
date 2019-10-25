import math
import time
import matplotlib.pyplot as plt
import matplotlib

class Plot(object):

    def __init__(self):
        super(Plot, self).__init__()
        self.plt = plt

    def plot(self, xData, yData):
        self.plt.clf()
        self.plt.title("Test Run Graph")
        self.plt.xlabel("Elapsed Time in Minutes")
        self.plt.ylabel("Trade-Result Transcations Per Second")
        self.plt.plot(xData, yData)
        self.plt.axis([min(xData), max(xData), min(yData), max(yData) + 2])
        self.plt.ioff()

    def savefig(self, path):
        self.plt.savefig(path)

# def handle_plot(xData, yData):

def standard_deviation(numList):
    '''
    输入 数字列表
    输出 标准差 
    '''
    Xi_cut_Xaverage_list = list()
    for num in numList:
        Xi_cut_Xaverage_list.append((num - average(numList))**2)

    n = len(numList)
    standard_deviation = math.sqrt(1/n * sum(Xi_cut_Xaverage_list))

    return standard_deviation

def average(numList):
    '''
    输入 数字列表
    输出 列表中数字的平均值 
    '''
    numSum = 0.0
    for num in numList:
        numSum += num
    average = numSum / len(numList)

    return average

def Manhattan_distance(x1, y1, x2, y2):
    ''' 
    输入两个坐标
    输出 曼哈顿距离
    '''
    c = abs(x1 - x2) + abs(y1 - y2)

    return c

def Gaussian_distribution(o, u, x):
    ''' 
    高斯分布的 概率密度函数
    '''
    y = 1 / (math.sqrt(2 * math.pi) * o) * math.e**(-1 * (x - u)**2 / (2 * o**2))

    return y

def Gaussian_distribution_plot(o, u):
    '''
    输入o 和 u
    动态绘制 高斯分布的概率密度函数 
    '''
    x = []
    y = []
    i = 0
    plot = Plot()

    while True:
        x.append(i)
        y.append(Gaussian_distribution(o, u, i))

        plot.plot(x, y)
        print(x, y ,i)

        plt.pause(1)  #暂停一秒
        plt.ioff()
        i += 1
        time.sleep(1)

if __name__ == '__main__':
    #Gaussian_distribution_plot(1,5)
    pass
