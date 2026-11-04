class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        counts=[0]*26
        for char in letters:
            counts[ord(char)-ord('a')]+=1
        def backtrack(index: int)->int:
            if index==len(words):
                return 0
            max_score=backtrack(index+1)
            word=words[index]
            word_counts=[0]*26
            word_score=0
            can_form=True
            for char in word:
                idx = ord(char)-ord('a')
                word_counts[idx]+=1
                word_score+=score[idx]
            for i in range(26):
                if counts[i]<word_counts[i]:
                    can_form=False
                    break
            if can_form:
                for i in range(26):
                    counts[i]-=word_counts[i]
                max_score=max(max_score, word_score+backtrack(index+1))
                for i in range(26):
                    counts[i]+=word_counts[i]
            return max_score
        return backtrack(0)