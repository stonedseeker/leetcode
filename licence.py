def licenseKeyFormatting(s: str, k: int):
        string_list = [c for c in s if c != '-']
        res = ''
        if len(string_list) % k == 0:
            res = ''.join(string_list[:k])
            res+= '-'
            res += ''.join( string_list[k:])

        else:
            res = string_list[0] + '-'
            for i in range((len(string_list) - 1 )% k):
                res = res[:i] + '-' + res[i:]

        return res

print(licenseKeyFormatting("2-5g-3-J", 4))
