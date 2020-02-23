tetrades=open('Arxeio.txt','w')

#Το αρχείο θα περιέχει όλους τους τετραψήφιους από το 0 έως το 9999 και όσοι αριθμοί έχουν λιγότερα από 4 ψηφία θα προστίθενται μποστά τους μηδενικά για να γίνουν και αυτοί τετραψήφιοι   
for i in range(0,10000):
    if i<10:
        x='0'+'0'+'0'+str(i)
    elif i<100:
        x='0'+'0'+str(i)
    elif i<1000:
        x='0'+str(i)
    else:
        x=str(i)
    tetrades.write(x+'\n')
tetrades.close()

#Έλεγχος εγκυρότητας αν αριθμός είναι εξαψήφιος 
ar=int(input('Dwse enan 6psifio arithmo'))
while ar<100000 or ar>999999:
    print ('O arithmos den einai 6psifios')
    ar=int(input('Dwse enan 6psifio arithmo'))

A=list(str(ar))

#Εδώ κάνω ταξινόμηση ευθείας ανταλλαγής με αύξουσα σειρά διότι από την εκφώνηση της άσκησης καταλαβαίνω ότι θα δέχεται έναν αριθμό με σειρά προτεραιότητας και στην περίπτωση που δεν είναι ο αλγόριθμος θα τον βάζει σε σειρά 
for i in range(len(A)-1):
    for j in range(len(A)-1,i,-1):
        if A[j]<A[j-1]:
            A[j],A[j-1]=A[j-1],A[j]
            
tetrades=open('Arxeio.txt','r')
arithmos=A[0]+A[1]+A[2]+A[3]+A[4]+A[5]

#Επειδή το αρχείο περιέχει όλες τις τετράδες από το 0 έως το 9999, εμφανίζω όλες τις διαθέσιμες τετράδες του αριθμού που εισήχθει
for line in tetrades:
    if arithmos[0:4] in line:
        print (line)
    elif arithmos[1:5] in line:
        print (line)
    elif arithmos[2:6] in line:
        print (line)
