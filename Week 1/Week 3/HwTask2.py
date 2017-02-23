def harmonic(n): #returns harmTot which will be the nth value in the harmonic series 
    harmTot = 1
    harmStart = 1
    for i in range(0,n): #loops through n amount of times to genereate the nth value in the harmonic sereis
        harmTot=harmTot+harmStart/2.0 #makes the current total by added the previous total to half the previous harmonic value
        harmStart=harmStart/2.0 #halfs the value that is added
    return harmTot
    
n=10
print(harmonic(n)) #calls the functions and hands it the parameters
