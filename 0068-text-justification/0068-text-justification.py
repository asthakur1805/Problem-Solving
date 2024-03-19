class Solution:
    
    def fullJustify(self,words,maxWidth):
        
        currLine, lineLength, index = [], 0, 0
        
        result = []
        
        while index < len(words):
            
            numWords = len(currLine)
            
            if lineLength + numWords + len(words[index]) > maxWidth:
                
                extraSpaces = maxWidth - lineLength
                
                spaces = extraSpaces // (max(1,numWords-1))
                remainder = extraSpaces % (max(1,numWords-1))
                
                for currIndex in range(max(1,numWords-1)):
                    
                    currLine[currIndex] += ' ' * spaces
                    if remainder:
                        currLine[currIndex] += ' '
                        remainder -= 1
                        
                result.append(''.join(currLine))
                currLine, lineLength = [], 0 
                
            
            currLine.append(words[index])
            lineLength += len(words[index])
            index += 1
                
        currLine = ' '.join(currLine)
        extra = maxWidth - len(currLine)
        result.append(currLine + ' ' * extra)
        
        return result 