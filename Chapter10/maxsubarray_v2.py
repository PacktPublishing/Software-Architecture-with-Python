# Code Listing #2

"""

Maximum subarray problem - version #2

"""

def max_subarray(sequence):
    """ Find sub-sequence in sequence having maximum sum """

    sums = []
    
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            # Without bug: To reproduce bug uncomment
            # next line and comment the line after.
            # sub_seq = sequence[i:j]
            sub_seq = sequence[i:j+1]           
            sub_seq_sum = sum(sub_seq)
            print(sub_seq,'=>',sub_seq_sum)
            sums.append(sum(sub_seq))

    return max(sums)
