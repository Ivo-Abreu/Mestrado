def timer(seconds,text="Done in"):
    day = seconds // (24 * 3600)
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    day= int(day)
    hour = int(hour)
    minutes = int(minutes)
    seconds = int(seconds)
    if day > 0:
        text = text + " " + str(day) + "d"
    if hour > 0:
        text = text + " " + str(hour) + "h"
    if minutes > 0:
        text = text + " " + str(minutes) + "m"
    text = text + " " + str(seconds) + "s"
    print(text)