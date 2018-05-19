class TextCompressor:
    def longestRepeat(self, sourceText):
        sourceTextOrig = sourceText
        start_point = 0
        end_point = 1
        max_substring = ''
        test_substring = sourceText[start_point:end_point]
        while True:
            sourceText = sourceTextOrig[end_point:]
            if test_substring in sourceText:
                max_substring = test_substring if len(test_substring) > len(max_substring) else max_substring
                end_point = end_point + 1
            else:
                start_point = end_point
                end_point = end_point + 1
            if end_point < len(sourceText):
                test_substring = sourceTextOrig[start_point:end_point]
            else: return max_substring

sourceText = "Testing testing 1 2 3."
print(TextCompressor().longestRepeat(sourceText))
sourceText = "The quick brown fox jumps over the lazy dog."
print(TextCompressor().longestRepeat(sourceText))
sourceText = "ABABA"
print(TextCompressor().longestRepeat(sourceText))
sourceText = "a"
print(TextCompressor().longestRepeat(sourceText))
