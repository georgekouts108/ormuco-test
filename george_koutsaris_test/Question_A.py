"""
line1: a tuple with two values (x1,x2)
line2: another tuple with two values (x3,x4)

NOTE: each line will begin at the lower x-value and end at the higher one.
For example: either (5, 15) or (15, 5) will draw a line from x=5 to x=15.
"""
def check_overlap(line1, line2):
    
    x1, x2 = (min(line1), max(line1))
    x3, x4 = (min(line2), max(line2))

    print(f"Lines entered: ({x1}, {x2}) and ({x3}, {x4})")
    overlapped = True

    # case 1: line2 is on the right of line1 without overlapping
    if x3 > x2:
        overlapped = False

    # case 2: line2 overlaps line1: only line2's lower bound falls within line1
    elif x4 > x2 and x2 >= x3:
        overlapped = True

    # case 3: line2 overlaps line1: only line2's upper bound falls within line1
    elif x4 >= x1 and x1 > x3:
        overlapped = True
        
    # case 4: line2 is on the left of line1 without overlapping
    elif x1 > x4:
        overlapped = False

    # case 5: line2 overlaps line1: line2 is entirely within line1
    elif x3 >= x1 and x4 <= x2:
        overlapped = True

    # case 5: line2 overlaps line1: line1 is entirely within line2
    elif x1 >= x3 and x4 >= x2:
        overlapped = True

    return overlapped
    
def program():
    try:
        x1 = float(input("Enter line1's first x point: "))
        x2 = float(input("Enter line1's second x point: "))
        x3 = float(input("Enter line2's first x point: "))
        x4 = float(input("Enter line2's second x point: "))

        result = check_overlap((x1,x2), (x3,x4))

        print(f"The lines {('do not' if not result else '')}overlap.")

    except (ValueError):
        print("Inputs must be numeric values.")
    except (Exception):
        print("An error occurred.")

program()

