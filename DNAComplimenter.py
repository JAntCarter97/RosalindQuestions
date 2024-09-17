#ID: REVC

#Method that takes in the sample dna string data, converts the string to a list,
#then exchanges A and T also C and G, then reverses the list and returns the list back to a string
def complimentDNA(dnaString):
    dnaTemp = [n for n in dnaString]
    for i in range(len(dnaString)):
        if dnaTemp[i] == "A":
            dnaTemp[i] = "T"
        elif dnaTemp[i] == "T":
            dnaTemp[i] = "A"
        elif dnaTemp[i] == "C":
            dnaTemp[i] = "G"
        elif dnaTemp[i] == "G":
            dnaTemp[i] = "C"
    dnaTemp.reverse()
    return ''.join(dnaTemp)


#Test cose 
#sampleDNA = "AAAACCCGGT"
#
#dnaComplemented = complimentDNA(sampleDNA)
#print(dnaComplemented)