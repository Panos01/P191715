x=int(input('Dwse arithmo:'))
while x>=10:
    x=x*3+1
    print(x)
    sum=0
    
    #Εδώ ο αριθμός μετατρέπεται σε string ώστε να προστεθούν τα ψηφία του και να γίνει μονοψήφιος
    for item in list(str(x)):
        sum=sum+int(item)    
    print (sum)
    x=sum
    
