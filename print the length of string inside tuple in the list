print 'Enter 6 values'
a,b,c,d,e,f=raw_input().split()
tup=(d,e,f)
lis=[a,b,c,(tup)]
print 'The Entered Tuple is ',tup
print 'The Entered List is ',lis
for i in range(len(lis)):
    j=lis[i]
    if len(j) > 1:
        if  isinstance(j, str)==True:
            print len(lis[i])
        else :
            for k in range (len (j)):
                l=lis[i][k]
                if l.isdigit()==False:
                    print len (lis[i][k])
                else :
                        print 'It is a integer'        
    else :
        if j.isdigit()==False:
                print len(lis[i])
        else :
                print 'It is a integer'
