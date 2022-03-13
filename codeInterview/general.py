#fuzz and buzz
chk=[3,5,6,7,9]
for i in range(1,100):
    out=[i]+[c for c in chk if i%c==0]
    print ("{}".format(out))
    

