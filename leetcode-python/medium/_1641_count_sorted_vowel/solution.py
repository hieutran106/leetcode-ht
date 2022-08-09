class Solution:
    def countVowelStrings(self, n: int) -> int:
        base = [1] * 5
        result = [base]
        for i in range(2, n+1):
            row_sum = 0
            row = [0] * 5
            for j in reversed(range(5)):
                row[j] = result[-1][j] + (row[j+1] if j <4 else 0)
                row_sum += result[-1][j]

            result.append(row)

        final = sum(result[-1])
        return final

