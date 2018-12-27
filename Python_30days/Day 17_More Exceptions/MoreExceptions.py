#Write your code here
class Calculator:
    @staticmethod
    def power(n, p):

        # The condition is not true, then raise assert error.
        # assert(n >= 0 and p >= 0), "n and p should be non-negative"

        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        else:
            return n ** p


myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)