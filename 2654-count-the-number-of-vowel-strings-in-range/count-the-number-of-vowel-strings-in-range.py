class Solution(object):
    def vowelStrings(self, words, left, right):
        a="aeiouAEIOU"
        b=0
        for i in range(left,right+1):
            if words[i][0] in a and words[i][-1] in a :
                b+=1
        return b
        