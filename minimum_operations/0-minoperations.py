#!/usr/bin/python3

def minOperations(i):
    file = 1
    copier = 0
    action = 0

    if i <= 1:
        return 0

    while file < i:
        if i % file == 0:
            copier = file
            action += 1

        file += copier
        action += 1

    return action
