"""The included code stub will read an integer. n. from STDIN.
Without using any string methods. try to print the following:
123 ...n
Note that n.. represents the consecutive values in between.
Example
Print the string 12345.
Input Format
The first line contains an integer n.
Constraints
Output Format
Print the list of integers from 1 through n as a string. without spaces.
Sample Input O
3
Sample Output O
123"""

if __name__ == '__main__':
    n = int(input())
    result = ""
    for i in range(1,n+1):
        result += str(i)
    print(result)
