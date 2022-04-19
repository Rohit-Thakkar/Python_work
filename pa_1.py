import numpy as np
 
def prCharWithFreq(str) :
     
    n = len(str)
     
    freq = np.zeros(26, dtype = int)

    for i in range(0, n) :
        freq[ord(str[i]) - ord('A')] += 1
                 
    for i in range(0, n) :
         
        if (freq[ord(str[i])- ord('A')] != 0) :
             
            print (str[i], freq[ord(str[i]) - ord('A')],
                                                end = "\n")

            freq[ord(str[i]) - ord('A')] = 0
         
     
if __name__ == "__main__" :
     
    str = "AABBBCCDE";
    prCharWithFreq(str);
