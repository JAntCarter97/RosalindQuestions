#k_mer nucleotide pattern counting 

#Takes inputs of a string of nucleotides and a nucleotide pattern 
#then counts how many nucleotide patterns occur, including any 
#overlapping, and returns the number of times the pattern occurs in
#the nucleotide string.

def nucPatternCount(nucleotideString, pattern):
    #Func vars
    patternLength = len(pattern)
    patternCount = 0
    nucListLength = len(nucleotideString)
    print(patternLength)
    print(nucListLength)
    #Force uppercase on nucleotide string and pattern string.
    nucleotideString = nucleotideString.upper()
    pattern = pattern.upper()
    #Convert strings to lists
    nucList = [i for i in nucleotideString]
    patternList = [k for k in pattern]
    #print(nucList)
    #print(patternList)
    #Indexes that are numbers because python is inferior to C
    #and it throws an error when trying to use the indexes in
    #python's for loops for anything mathwise. 
    j = 0
    p = 0   
    #Loops through the nucleotide list and checks for the first 
    #element that matches the first element of our pattern.            
    while j < nucListLength:
        if nucList[j] == patternList[0]:
            #Loops through the nucleotide list's indexes at a length that is 
            #the same length of our pattern list. Also it makes sure the indexes 
            #are not overflowing the nucleotide list's length.
            while p < patternLength and j + p < nucListLength:
                if nucList[j + p] != patternList[p]:
                    #Does not match the full pattern and breaks.
                    break
                elif p == patternLength - 1 and nucList[j + p] == patternList[p]:
                    #Matches the full pattern and increments the pattern occurence count.
                    patternCount += 1  
                #Increment to the next pattern list index for the full check.  
                p += 1
        #Increment to next nucleotide list index and 
        #reset the pattern list index for a new pattern check.
        j += 1
        p = 0
                    
    return patternCount 
                
#Test code               
#nucleoPattern = "acacac"
#sampleNuc = "acacacacacac" 
#
#howMany = nucPatternCount(sampleNuc, nucleoPattern)
#print(howMany)