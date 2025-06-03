#Smith-Waterman Tweak
#==============================================================================================
#                     Author: Johnny Carter (code) Smith and Waterman (algorithm)
#                                           Summary:
# The Smith-Waterman algorithm for nucleotide pairwise sequence scoring.
# Inputs: Two nucleotide sequences (strings, Bio.Seq, fasta files) of "A" "T" "C" "G" 
# Outputs: Sequence alignment score. Traceback match sequence.
#
#===============================================================================================

from Bio.Seq import Seq
import random
import numpy as np

nucleotides = ["A", "C", "G", "T"]

#Scoring
matchScore = 1.0
misMatchScore = -0.3
gapPenaltyScore = -1.3
nullScore = 0.0

def seqGen(length, seed):
    seq = []
    random.seed(seed)
    for i in range(1, length + 1):
        seq.append(random.choice(nucleotides))
    return "".join(seq) 

def matrixGen(sequence1, sequence2):
    print(sequence1)
    print(sequence2)
    #Generate Matrix shape with extra row/column of zeros
    #Nucleotide matches start at default matchScore
    seqMatrix = np.zeros([len(sequence2)+1, len(sequence1)+1])  
    for i in range(1, len(sequence2)+1):
        for j in range(1, len(sequence1)+1):
            if (sequence1[j-1] == sequence2[i-1]):
                seqMatrix[i][j] = matchScore
    return(matrixScoring(seqMatrix))

def matrixScoring(seqMatrix):
    #===============================================
    # Score the matrix from top left to bottom right.
    # Create a traceback matrix of 1 = largest num
    # in rows.
    #===============================================
    dimensions = seqMatrix.shape
    row, col = dimensions
    for i in range(1, row):
        for j in range(1, col):
            currentScore = seqMatrix[i][j]
            diagonalScore = 0
            upperScore = seqMatrix[i-1][j] + gapPenaltyScore
            leftScore = seqMatrix[i][j-1] + gapPenaltyScore
            if (currentScore == 1):
                diagonalScore = seqMatrix[i-1][j-1] + seqMatrix[i][j]
            elif (currentScore == 0):
                diagonalScore = seqMatrix[i-1][j-1] + misMatchScore
            maxNum = max(currentScore, diagonalScore, upperScore, leftScore)
            # Convert any negative scores to the nullScore
            if (maxNum <= nullScore):
                maxNum = nullScore
            seqMatrix[i][j] = maxNum
        
    #===============================        
    # Traceback Sequence
    # TODOO: find max num index pos
    # in seqMatrix and check each 
    # adjacent 3 cells for the largest
    # num. If any cells are equal then
    # sum the boxes for the largest 
    # then continue on that cell's 
    # box that is the largest sum 
    # until we find a cell value of 1.0
    # with the three adjecent cells 
    # with values of 0.0 or we hit
    # the zeroth row and col.
    #===============================    

    #===============================
    #Visuals and Returns
    #===============================
    #print(seqMatrix)
    print(tracebackMatrix)
    return(seqMatrix)

#mat = matrixGen(seqGen(10,0), seqGen(10,1))
mat = matrixGen("AGGTACT", "GGATCT")
print(mat)