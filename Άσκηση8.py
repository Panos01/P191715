import random
import time
import sys

#Εδώ είναι ένα πρόγραμμα από το ίντερνετ που εμφανίζει τα φανάρια με χρώματα 
try: color=sys.stdout.shell
except AttributeError:raise RuntimeError('Usage only on PYTHON IDLE window')

def eisodos():
    return random.randrange(0,6)

def eksodos(A):
    if A>=11:
        return random.randrange(5,11)
    elif A<=5:
        return random.randrange(1,A+1)
    else:
        return random.randrange(5,A)
    
#Εδώ βρήσκω το φανάρι με τον μέγιστο αριθμό αυτοκινήτων και τον βάζω στην λίστα MAX 
def megistos(A):
    MAX=[]

    maxar=-1
    for item in A:
        if item>maxar:
            maxar=item

    N=len(A)
    for i in range(N):
        if A[i]==maxar:
            MAX.append(i)

    N=len(MAX)
    return tyxaiaepilogi(MAX,N)

#Εδώ γίνεται τυχαία επιλογή αν κάποια φανάρια έχουν τον ίδιο αριθμό αυτοκινήτων 
def tyxaiaepilogi(MAX,N):
    if N==1:
        x=MAX[0]
    else:
        x=random.choice(MAX)
    return x

#Εδώ είναι ένα χρονόμετρο (που βρήκα από το ίντερνε) το οποίο έβαλα για να φαίνονται ξεκάθαρα πόσα αυτοκίνητα είναι κάθε φορά σε κάθε φανάρι  
def countdown(t):
    while t>0:
        t=t-1
        time.sleep(1)


A=[]
a1=eisodos()
a2=eisodos()
a3=eisodos()
A.append(a1)
A.append(a2)
A.append(a3)

#Εδώ γίνεται έλεγχος εγκυρότητας για όσο τα φανάρια δεν θα είναι μηδέν
while A[0]!=0 or A[1]!=0 or A[2]!=0:
    meg=int(megistos(A))
    print('- - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - - - - - - - -')
    x=eksodos(A[meg])
    color.write(str(meg+1)+'o fanari:','STRING')
    color.write('eixe '+str(A[meg])+' aytokinita, efygan '+str(x)+' aytokinita kai exei synolika '+str(A[meg]-x)+' aytokinita\n','stdin')
    A[meg]=A[meg]-x

    for i in range(0,3):
        if i!=meg:
            y=eisodos()
            color.write(str(i+1)+'o fanari:','stderr')
            color.write('eixe '+str(A[i])+' aytokinita, irthan '+str(y)+' aytokinita kai exei synolika '+str(A[i]+y)+' aytokinita \n','stdin')
            A[i]=A[i]+y
            
    countdown(10)
