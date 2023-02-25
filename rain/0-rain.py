#!/usr/bin/python3


""" Module 0-rain"""


def rain(walls):
    water_temp = 0
    water = 0
    size = len(walls)
    doom = 0

    if size <= 0:
        return water_temp
    for i in range(size):
        if walls[i] >= walls[doom]:
            doom = i
            water_temp = 0
        else:
            water += walls[doom] - walls[i]
            water_temp += walls[doom] - walls[i]

    if doom < size - 1:
        water -= water_temp

        # last peak wall

        peak_wall = doom
        doom = size - 1

        for i in range(size - 1, peak_wall, -1):
            if walls[i] >= walls[doom]:
                doom = i
            else:
                water += walls[doom] - walls[i]
    return water
