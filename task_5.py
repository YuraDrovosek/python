proceeds = int(input())
costs = int(input())

if proceeds - costs > 0:
    print("cool!")
else:
    print("bad :(")
    costs *= -1

print("profitability ={:.1f}{}".format((proceeds / costs * 100), "%"))

employee = int(input())

print((proceeds - costs) / employee)
