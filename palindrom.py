class Solution:
    def solution(self, S: str) -> str:
        # Count the frequency of each digit
        freq = [0] * 10
        for char in S:
            freq[int(char)] += 1
        
        # Prepare to build the palindrome
        half_palindrome = []
        center_digit = ""
        
        # Go through the digits from highest to lowest
        for digit in range(9, -1, -1):
            if freq[digit] > 0:
                # Add the largest possible half palindrome part
                half_count = freq[digit] // 2
                half_palindrome.append(str(digit) * half_count)
                
                # Check if there's a center digit
                if freq[digit] % 2 == 1 and center_digit == "":
                    center_digit = str(digit)
        
        # Create the first half and the mirrored second half
        first_half = "".join(half_palindrome)
        second_half = first_half[::-1]
        
        # Construct the full palindrome
        largest_palindrome = first_half + center_digit + second_half
        
        # Ensure there are no leading zeros, except for the single '0'
        if largest_palindrome and largest_palindrome[0] == '0':
            return '0'
        
        return largest_palindrome

# Take user input
user_input = input("Enter a string of digits: ")
sol = Solution()
result = sol.solution(user_input)
print(Solution(8798))