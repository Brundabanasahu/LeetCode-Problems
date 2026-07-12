class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        ans = sorted(freq.items(), key=lambda x: -x[1])

        result = ""
        for ch, f in ans:
            result += ch * f

        return result