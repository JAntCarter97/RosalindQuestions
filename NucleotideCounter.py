#Nucleotide Counter 
#ID: DNA

def countNucleotides(nucleotideString):
    #Get the length of the string in the number of nucleotides
    numNucleotides = len(nucleotideString)
    #Initiate nucleotide variables for incrementation
    countersDict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for i in nucleotideString:
        countersDict[i] += 1
            
    return ' '.join([str(val) for key, val in countersDict.items()])

#Test code
#sampleString = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
#result = countNucleotides(sampleString)
#print(result)


