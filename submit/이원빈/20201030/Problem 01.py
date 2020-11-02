try:
    fp = open('0000', 'r')
except:
    fp = open('0000', 'w')
finally:
    fp.close()
