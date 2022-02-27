class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index1,index2= -1,-1
      
        shortest=len(wordsDict)
        
        for i in range(len(wordsDict)):
            if word1==wordsDict[i]:
                index1=i
            elif word2==wordsDict[i]:
                index2=i
           
            if index1!=-1 and index2!=-1:
                shortest=min(abs(index1-index2),shortest)
        
        
        
        return shortest
