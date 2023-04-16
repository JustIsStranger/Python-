ttl_aot = input("How much is the total bill?")
tip = input("How much did he tip?")
ttl_aot = int(ttl_aot)
tip = int(tip)

percent = (tip * 100) / ttl_aot
percent = int(percent)

if percent >= 10 and percent <= 15:
    print("{}%.The tip was a little short!".format(percent))
if percent > 15 and percent <= 20:
    print("{}%.A good tip!".format(percent))
if percent > 20:
    print("{}%.What a fat tip!".format(percent))
if percent < 10:
    print("{}%.The tip is too small!".format(percent))




input()
