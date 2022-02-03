'''

For this program please write a method that calculate the LCM (least common multiple) of a pair of numbers.

Procedure to follow for determining lcm(a, b):

Steps:
1. If a = 0 or b = 0, then return with lcm(a, b) = 0, else go to step 2.
2. Calculate absolute values of the two numbers.
   * Hint: use the "abs()" function
3. Initialize a variable to hold the lcm as the higher of the two values computed in step 2.
4. If lcm is divisible by the lower absolute value, then return.
5. Increment lcm by the higher absolute value among the two and go to step 4.

Example:
Before we start with the implementation of this simple approach, let's do a dry-run to find lcm(12, 18).
As both 12 and 18 are positive, let's jump to step 3, initializing lcm = max(12, 18) = 18, and proceed further.
In our first iteration, lcm = 18, which isn't perfectly divisible by 12. So, we increment it by 18 and continue.
In the second iteration, we can see that lcm = 36 and is now perfectly divisible by 12. So, we can return from the algorithm and conclude that lcm(12, 18) is 36
'''


# All work should be done in this method, the header is provided for you.
# Reminder: "a" and "b" from the method are variables you can access in the code.
def lcm(a, b):
    if (int(a) * int(b) == 0):
        print("lcm(" + str(a) + ", " + str(b) + ") = 0")
    else:
        Num1 = abs(int(a))
        Num2 = abs(int(b))
        lcm = max(Num1,Num2)
        Oth = min(Num1,Num2)
        real_lcm = lcm
        while (real_lcm/Oth > int(real_lcm/Oth)):
            real_lcm += lcm
        print("lcm(" + str(a) + ", " + str(b) + ") = " + str(real_lcm))




###############################################################################
# Do all work above here.  Lines below are to help test the program.
lcm(12, 48)
lcm(100, 3)
lcm(-8, 14)
