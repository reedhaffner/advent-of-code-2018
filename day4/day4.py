import re

# day 4 part 1

slines = []
with open("sheet.txt", "r") as f:
    slines = sorted(f)


def get_total_mins_slept(slines):
    guards = {}

    reg_timestamp = re.compile("\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\]")
    reg_begin_shift_guard = re.compile("Guard #(\d{1,4}) begins shift")
    reg_fall_asleep = re.compile("falls asleep")
    reg_wake_up = re.compile("wakes up")

    current_guard = 0
    asleep = 0

    for line in slines:
        minute = reg_timestamp.search(line).group(5)
        if reg_begin_shift_guard.search(line):
            current_guard = reg_begin_shift_guard.search(line).group(1)
        if reg_fall_asleep.search(line):
            asleep = minute
        if reg_wake_up.search(line):
            try:
                guards[current_guard] = guards[current_guard] + (int(minute)-int(asleep))
            except:
                guards[current_guard] = (int(minute)-int(asleep))
            asleep = 0

    return(guards)


def get_slept_by_min(guard, slines):
    minutes = {}

    reg_timestamp = re.compile("\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\]")
    reg_begin_shift_guard = re.compile("Guard #(\d{1,4}) begins shift")
    reg_fall_asleep = re.compile("falls asleep")
    reg_wake_up = re.compile("wakes up")

    asleep = 0
    wrong_guard = True

    for line in slines:
        minute = reg_timestamp.search(line).group(5)
        if reg_begin_shift_guard.search(line):
            if reg_begin_shift_guard.search(line).group(1) == guard:
                wrong_guard = False
            else:
                wrong_guard = True

        if reg_fall_asleep.search(line):
            if wrong_guard:
                continue
            asleep = minute
        if reg_wake_up.search(line):
            if wrong_guard:
                continue
            for i in range(int(minute)-int(asleep)):
                i = i + int(asleep)
                try:
                    minutes[i] += 1
                except:
                    minutes[i] = 1
            asleep = 0
    return(minutes)


sleepiest_guard = max(get_total_mins_slept(slines), key=get_total_mins_slept(slines).get)
time_most_slept = max(get_slept_by_min(sleepiest_guard, slines), key=get_slept_by_min(sleepiest_guard, slines).get)
print(str(int(sleepiest_guard)*int(time_most_slept)))

# day 4 part 2

slines = []
with open("sheet.txt", "r") as f:
    slines = sorted(f)


def get_guards_mins(slines):
    minutes = {}

    reg_timestamp = re.compile("\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\]")
    reg_begin_shift_guard = re.compile("Guard #(\d{1,4}) begins shift")
    reg_fall_asleep = re.compile("falls asleep")
    reg_wake_up = re.compile("wakes up")

    current_guard = 0
    asleep = 0

    for line in slines:
        minute = reg_timestamp.search(line).group(5)
        if reg_begin_shift_guard.search(line):
            current_guard = reg_begin_shift_guard.search(line).group(1)

        if reg_fall_asleep.search(line):
            asleep = minute
        if reg_wake_up.search(line):
            for i in range(int(minute)-int(asleep)):
                i = i + int(asleep)
                try:
                    minutes[current_guard][i] += 1
                except:
                    try:
                        minutes[current_guard].update({i: 1})
                    except:
                        minutes[current_guard] = {i: 1}
            asleep = 0
    return(minutes)

top_guard = 0
top_min = 0
top_min_time = 0

for guards, minutes in get_guards_mins(slines).items():
    for minute, time in minutes.items():
        if time > top_min_time:
            top_min_time = time
            top_min = minute
            top_guard = guards

print(str(int(top_guard) * int(top_min)))