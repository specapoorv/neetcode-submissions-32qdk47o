class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []  # store indices
        results = [0] * len(temperatures)

        for i, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                prev = stack.pop()
                results[prev] = i - prev

            stack.append(i)

        return results