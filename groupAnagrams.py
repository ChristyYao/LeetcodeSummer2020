# O(n) time: iterate through entire strs list
# O(n) space: strDict and resDict each hold a set of key+value per str

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        strDict = {}
        resDict = {}
        
        for s in strs:
            
            if sorted(s) in strDict.values():
                resDict[''.join(sorted(s))].append(s)
            else:                
                strDict[s] = sorted(s)
                resDict[''.join(sorted(s))] = [s]
                
        return resDict.values()