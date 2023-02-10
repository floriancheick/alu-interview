#!/usr/bin/python3
"""
python Module
"""


def minOperations(n):
    """Calculates the number of operations needed to result in exactly i H characters"""
    # 2n => H-Co-Pa-HH
    # 3n => H-Co-Pa-HH-Pa-HHH
    # 4n => H-Co-Pa-HH-Co-Pa-HHHH
    # 5n => H-Co-Pa-HH-Pa-HHH-Pa-HHHH-Pa-HHHHH
    # 6n => H-Co-Pa-HH-Co-Pa-HHHH-Pa-HHHHHH
    # 7n => H-Co-Pa-HH-Pa-3H-Pa-4H-Pa-5H-Pa-6H-Pa-HHHHHHH
    # 8n => H-Co-Pa-HH-Co-Pa-HHHH-Pa-HHHHHH-Pa-HHHHHHHH
    # 9n => H-Co-Pa-HH-Pa-HHH-Co-Pa-HHHHHH-Pa-HHHHHHHHH

    file = 1
    copier = 0
    action = 0

    if n <= 1:
        return 0

    # As long as the number of H is not equal to n, run loop
    while file < n:
        if n % file == 0:
            # copy "H"
            copier = file
            action += 1

        # now you paste into file
        file += copier
        # that is another operation
        action += 1

    return action
