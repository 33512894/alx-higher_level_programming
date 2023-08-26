#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc

a = 10
b = 5

r_add = calc.add(a, b)
r_sub = calc.sub(a, b)
r_mul = calc.mul(a, b)
r_div = calc.div(a, b)


print("{} + {} = {}".format(a, b, r_add))
print("{} - {} = {}".format(a, b, r_sub))
print("{} * {} = {}".format(a, b, r_mul))
print("{} / {} = {}".format(a, b, r_div))
