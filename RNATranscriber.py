#Transcribing RNA
#ID: RNA

def transcribeRNA(rnaString):
    rnaTemp = [n for n in rnaString]
    for i in range(len(rnaTemp)):
        if rnaTemp[i] == "T":
            rnaTemp[i] = "U"
        
    return ''.join(rnaTemp)

#Test code
#sampleRNA = "GATGGAACTTGACTACGTAAATT"
#newRNA = transcribeRNA(sampleRNA)
#print(newRNA)

            