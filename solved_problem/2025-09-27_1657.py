class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Time complexity: O(NlogN + MlogM)
        # Space complexity: O(N+M)
        
        # Get frequency of each letter
        freq_word1 = Counter(word1)
        freq_word2 = Counter(word2)

        print(freq_word1)
        print(freq_word2)

        # operation 1: check if word1 and word2 have the same frequency character in sorted order
        sorted_val_word1 = sorted(freq_word1.values())
        sorted_val_word2 = sorted(freq_word2.values())

        # operation 2: check if word1 and word 2 has the same unique letter
        keys_match = set(freq_word1.keys()) == set(freq_word2.keys())


        return sorted_val_word1 == sorted_val_word2 and keys_match