import csv
from bokeh.models import Arrow, NormalHead, OpenHead, VeeHead
from bokeh.palettes import Muted3 as color
from bokeh.plotting import figure, show
from collections import defaultdict

circle_radious = 5

tasks = []
ins = []
lkd = {}
teams = set()
req = defaultdict(list)

with open("input.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        tasks.append(row)
        teams.add(row[3])
        # print(row)
        if row[1] == "":
            lkd[row[0]] = []
            ins.append(row[0])
            continue
        dependencies = row[1].split("-")
        lkd[row[0]] = dependencies
        for dep in dependencies:
            req[dep].append(row[0])

draw = [[0, int(x), len(ins), int(tasks[int(x)-1][2]), tasks[int(x)-1][3]] for x in ins]
max_height = 1
while ins:
    processing = ins.copy()
    max_height = max(max_height, len(processing))
    # print(processing)
    for inp in processing:
        ins.remove(inp)
        for remvng in req[inp]:
            lkd[remvng].remove(inp)
            if lkd[remvng] == []:
                ins.append(remvng)
                draw.append([int(inp), int(remvng), 0, int(tasks[int(inp)][2]), tasks[int(inp)][3]])
        req[inp] = []
    l = len(ins)
    for i in range(-1, -l-1, -1):
        draw[i][2] = l


team_time = {}
for i in teams:
    team_time[i] = []


p = figure(tools="", toolbar_location=None, background_fill_color="#efefef")
p.grid.grid_line_color = None
p.yaxis.visible = False

time = 0
height = max_height*2*circle_radious
p.circle(x=0, y=height/2, radius=circle_radious, color="#fafafa")
# print(draw)
ptr = 0
while ptr < len(draw):
    curr = [draw[ptr]]
    fetch = curr[0][2] - 1
    y_axis = height/(fetch + 2)
    while fetch > 0:
        ptr += 1
        fetch -= 1
        curr.append(draw[ptr])

    for point in curr:
        pass

    ptr += 1




# print(lkd, req)
# print(team_time)
# print(max_height)
# print(draw)
p.circle(x=(0, 100, 0.5), y=(0, 0, 0.7), radius=circle_radious, color="#fafafa")

show(p)