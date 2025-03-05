# https://leetcode.com/problems/word-ladder/
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList) 
        if endWord not in wordSet:
            return 0  
        
        queue = deque([(beginWord, 1)]) 
        
        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + c + word[i+1:]
                    
                    if newWord in wordSet:
                        queue.append((newWord, steps + 1))
                        wordSet.remove(newWord)
        
        return 0
# TC:O(L)
# SC:O(N)
# Approach:make all possiblites of the present word and search for the word