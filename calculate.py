import math
from scipy.integrate import quad

SQRT2 = 2**0.5
蜗杆参数 = {"u": 90.492, "sig": 0.1171, "min": 90.14, "max": 90.875}
#蜗杆参数 = {"u": 90.3513, "sig": 0.0652, "min": 90.14, "max": 90.875}
壳体参数 = {"u": 90.807, "sig": 0.1104, "min": 90.45, "max": 91.35}
#壳体参数 = {"u": 91.0555, "sig": 0.0925, "min": 90.45, "max": 91.35}


def normal_distribution(x, u, sig):
    return math.exp(-(x - u)**2 /
                    (2 * sig**2)) / (math.sqrt(2 * math.pi) * sig)


def my_erf_between(a, b):
    return abs(math.erf(a)) + abs(
        math.erf(b)) if a * b < 0 else abs(math.erf(a) - math.erf(b))


def normal_to_std(x, u, sig):
    return (x - u) / sig


def nd_between(floor, ceil, u, sig):
    return my_erf_between(
        normal_to_std(floor, u, sig) / SQRT2,
        normal_to_std(ceil, u, sig) / SQRT2) * 0.5


def cal_unmatch(x):
    return normal_distribution(x, 蜗杆参数["u"], 蜗杆参数["sig"]) * nd_between(
        壳体参数["min"], x, 壳体参数["u"], 壳体参数["sig"])


不匹配率, 积分误差 = quad(cal_unmatch, 壳体参数["min"], 蜗杆参数["max"])
壳体合格率 = nd_between(壳体参数["min"], 壳体参数["max"], 壳体参数["u"], 壳体参数["sig"])
蜗杆合格率 = nd_between(蜗杆参数["min"], 蜗杆参数["max"], 蜗杆参数["u"], 蜗杆参数["sig"])


def my_print(desc, num):
    print(desc, "{:.3%}".format(num))


def main():
    my_print("壳体合格率：", 壳体合格率)
    my_print("蜗杆合格率：", 蜗杆合格率)
    my_print("不匹配率：", 不匹配率)
    my_print("总合格率：", 壳体合格率 * 蜗杆合格率 - 不匹配率)


if __name__ == "__main__":
    main()