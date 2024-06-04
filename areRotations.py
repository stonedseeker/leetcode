def areRotations(s1,s2):
        temp = s1 + s1
        
        print(temp)
        return temp.count(s2) > 0


s1 = "geeksforgeeks"
s2 = "forgeeksgeeks"

print(areRotations(s1,s2))
