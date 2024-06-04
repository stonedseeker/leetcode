class Solution:
    def betterString(self, str1, str2):
        def generate_subsequences(s):
            def helper(index, current, result):
                if index == len(s):
                    result.add(current)
                    return

                # Include the current character
                helper(index + 1, current + s[index], result)

                # Exclude the current character
                helper(index + 1, current, result)

            result = set()  # Use a set to store unique subsequences
            helper(0, "", result)
            return result

        subsequences_str1 = generate_subsequences(str1)
        subsequences_str2 = generate_subsequences(str2)

        return str1 if len(subsequences_str1) >= len(subsequences_str2) else str2

# Example usage
a = "gboubwd"
b = "bekoilx"
print(Solution().betterString(a, b))



#a = "ljmolmti"
#b = "sqapzwbb"

#print(Solution().betterString(a,b))
