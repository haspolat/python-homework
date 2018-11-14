def chengfabiao():
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            print("%d * %d = %d" % (i, j, i*j),end = " ")
            if i == j:
                print()
            j += 1
        i += 1