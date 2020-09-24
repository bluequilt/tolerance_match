import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import special
from calculate import 蜗杆参数, 壳体参数

plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['savefig.dpi'] = 200
plt.rcParams['figure.dpi'] = 200


def normal_distribution(x, u, sig):
    return np.exp(-(x - u)**2 / (2 * sig**2)) / (math.sqrt(2 * math.pi) * sig)


fig_names = ["蜗杆", "壳体"]
fig_paras = {"蜗杆": 蜗杆参数, "壳体": 壳体参数}
def 壳体蜗杆对比():
    fig, axes = plt.subplots(2, 1, True)
    #fig.canvas.set_window_title(fig_name)
    for j, name in enumerate(fig_names):
        u=fig_paras[name]["u"]
        half_sec=max(abs(fig_paras[name]["min"]-u),abs(fig_paras[name]["max"]-u))
        plot_min_x,plot_max_x=u-half_sec,u+half_sec
        X = np.linspace(plot_min_x, plot_max_x, 500)
        Y = normal_distribution(X,u,fig_paras[name]["sig"])
        #====
        min_x, max_x = fig_paras[name]["min"], fig_paras[name]["max"]
        min_y, max_y = min(Y), max(Y)
        axes[j].plot(X, Y, label=name + "分布")
        axes[j].set(ylim=(0,axes[j].get_ylim()[1]))
        axes[j].set_xlabel("长度")
        axes[j].set_ylabel("密度")
        #====
        axes[j].plot((min_x, min_x), (min_y, max_y), label=f"公差下限")
        axes[j].plot((max_x, max_x), (min_y, max_y), label=f"公差上限")
        axes[j].legend()

    fig.suptitle("壳体和蜗杆尺寸分布")
    fig.subplots_adjust(wspace=0, hspace=0)
    fig.savefig(f'壳体和蜗杆尺寸分布.png', bbox_inches="tight")
    plt.show()

def 正态erf对比():
    fig, axes = plt.subplots(2, 1, True)
    #fig.canvas.set_window_title(fig_name)
    X = np.linspace(-4, 4, 500)
    ztY = normal_distribution(X,0,1)
    axes[0].plot(X, ztY, label="标准正态分布")
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("p")
    axes[0].legend()
    #====
    erfY=special.erf(X)
    axes[1].plot(X, erfY, label="误差累积函数")
    axes[1].set_xlabel("x")
    axes[1].set_ylabel("p")
    axes[1].legend()
    fig.subplots_adjust(wspace=0, hspace=0)
    fig.savefig(f'aa.png', bbox_inches="tight")
    plt.show()

壳体蜗杆对比()