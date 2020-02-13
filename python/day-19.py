
 
class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        calculatedSum = 0
        for i in range(1,n+1):
            if n % i == 0:
                calculatedSum += i
        return calculatedSum

