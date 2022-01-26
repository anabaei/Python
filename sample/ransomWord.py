# you are given a an array of words and ask to check if that list exist or not

class Solution:
    def findRansom(self, arr, word):
        res = {}
        for i in arr:
            if (i in res):
                res[i] += 1
            else:
                res[i] = 1
        
        for w in word:
            if (w in res):
                if(res[w]== 1): 
                    del res[w]
                else:
                    res[w] -=1
            else:
                return False
        print(res)
        return True



res = Solution().findRansom(['a','b','b','b','c'], 'abbbbc')
print(res)
     