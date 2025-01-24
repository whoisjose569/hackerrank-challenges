"""Task
The provided code stub reads an integer. n. from STDIN. For all non-negative integersi < n. print t .
Example
The list of non-negative integers that are less than n = 3 is [0, 1, 2). Print the square of each number on a separate line.
1
4
Input Format
The first and only line contains the integer. n.
Constraints
Output Format
Print n lines. one corresponding to each i.
Sample Input O
5
Sample Output O
o
4
9
16"""

if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        print(i**2)