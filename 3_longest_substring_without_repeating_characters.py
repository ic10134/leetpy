class Solution:
    def lengthOfLongestSubstring(self, s):
        window = {}
        left_window = 0
        longest = 0
        for right_window in range(len(s)):
            current_char = s[right_window]
            prev_seen_char = window.get(current_char)
            if prev_seen_char is not None and prev_seen_char >= left_window:
                left_window = prev_seen_char +1
            window[current_char] = right_window
            longest = max(longest, right_window - left_window +1)
        return longest

if __name__ == '__main__':
    str = input("Enter the elements of the array as first list: ")    
    s = Solution()
    print(s.lengthOfLongestSubstring(str))