def version_compare(version1, version2):

    # Make a list of all integers for both version strings.
    
    v1split = version1.split('.')
    v2split = version2.split('.')
    v1 = [int(i) for i in v1split]
    v2 = [int(i) for i in v2split]

    # If one version has less numbers than the other,
    # suppose we call this number of integers "N";
    #
    # We need to first compare the first N pairs of
    # numbers between the two versions. We will return
    # 1 if version1 > version2, or -1 if v2 > v1.
    
    mismatchFound = False
    res = 0
    for p in range( min( len(v1), len(v2) ) ):
        if v1[p] > v2[p]:
            mismatchFound = True
            res = 1
            break
        elif v1[p] < v2[p]:
            mismatchFound = True
            res = -1
            break
    
    if mismatchFound:
        return res

    # If we reach this point in the code,
    # then so far the two versions are equal.
    #
    # But if one version has more numbers than
    # the other, then that version will be greater
    # if any of its extra numbers are above 0.
    #
    # Once again, we will return 1 if
    # version1 > version2, -1 if v2 > v1, or 0 if
    # the versions are equal.
    
    if len(v1) > len(v2):
        for x in v1[min( len(v1), len(v2) ) : ]:
            if x > 0:
                return 1
    
    elif len(v1) < len(v2):
        for x in v2[min( len(v1), len(v2) ) : ]:
            if x > 0:
                return -1
        
    return 0
    
def program():
    v1 = input("Enter version #1 string: ")
    v2 = input("Enter version #2 string: ")
    try:
        result = version_compare(v1,v2)
        if result == 0:
            print(f"version {v1} == version {v2}")
        elif result == 1:
            print(f"version {v1} > version {v2}")
        elif result == -1:
            print(f"version {v1} < version {v2}")
            
    except (Exception):
        print("Something went wrong.")
    finally:
        print("Program completed.")
    

program()
