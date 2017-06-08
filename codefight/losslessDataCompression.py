'''
Given a string, apply sliding window compression to it.
'''

def losslessDataCompression(inputString, width):
    result = ""
    i = 0
    while i < len(inputString):
        j = max(i - width, 0)
        longestMatch = None
        k = i
        maxl = 0
        while j < i and k < len(inputString):
            if inputString[j] == inputString[k]:
                l = 1
                startIndex = j
                k += 1
                j += 1
                while j < i and k < len(inputString) and inputString[j] == inputString[k]:
                    j += 1
                    k += 1
                    l += 1
                print('l = ', l)
                print('maxl = ', maxl)
                if l > maxl:
                    maxl = l
                    longestMatch = (startIndex, maxl)                
                k = i
            else:
                j += 1
        if longestMatch == None:
            result += inputString[i]
            i = k + 1
        else:
            result += "("+str(longestMatch[0])+','+str(longestMatch[1])+")"
            i = k + longestMatch[1]
    return result
        
                
            
