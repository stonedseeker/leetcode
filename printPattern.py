class Solution:

    def print_sequence(self, n, initial_val, flag):

        print(n)
        
        if flag == False and n == initial_val:
            return 0
    
        if flag:
            if n - 5 > 0:
                self.print_sequence(n-5, initial_val, True)

            else:
                self.print_sequence(n+5, initial_val, False)

        else:
            self.print_sequence(n+5, initial_val, False)


    
    def print_sequence2(self, n, initial_val, flag, memo = []):
        
        memo.append(n)
        
        if flag == False and n == initial_val:
           return memo
    
        if flag:
            if n - 5 >= 0:
                self.print_sequence2(n-5, initial_val, True, memo)

            else:
                self.print_sequence2(n+5, initial_val, False, memo)

        else:
            self.print_sequence2(n+5, initial_val, False, memo)

        return memo
            
print(Solution().print_sequence2(16,16, True))
