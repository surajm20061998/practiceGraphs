#Intuition : For every edge going from a->b, do score[a]-=1 and score[b]+=1
#Finally check for end condition that is trust_scores[i] == n-1 in scores list, return index+1 if true elase -1
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        trust_scores = [0]*(n+1)

        for a,b in trust:
            trust_scores[a]-=1
            trust_scores[b]+=1

        for i in range(1,n+1):
            if trust_scores[i] == n-1:
                return i

        return -1

        print(trust_scores)

        
        