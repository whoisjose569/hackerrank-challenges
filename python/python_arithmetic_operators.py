"""Task
The provided code stub reads two integers from STDIN. a and b. Add code to print three lines where:
1. The first line contains the sum of the two numbers.
2. The second line contains the difference of the two numbers (first - second).
3. The third line contains the product of the two numbers.
Example
Print the following:
8
-2
15
Input Format
The first line contains the first integer. a.
The second line contains the second integer. b."""

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a+b)
    print(a-b)
    print(a*b)
