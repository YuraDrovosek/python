time_seconds = int(input())

hours = time_seconds // (60 * 60)
remainder = time_seconds - hours * 60
minutes = remainder // 60
remainder -= minutes * 60
seconds = remainder % 60

print("%d:%d:%d" % (hours, minutes, seconds,))
