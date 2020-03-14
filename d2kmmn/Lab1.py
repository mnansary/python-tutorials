for a in range(0, 5):
    for b in range(0, a+1):
        print('*', end=' ')
    print('\r')
if a<=5:
    for c in range(0, 5):
        for d in range(4, c, -1):
            print('*', end=' ')
        print('\r')
