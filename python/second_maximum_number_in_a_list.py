'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
'''

n = int(input())
arr = list(map(int, input().split()))

max = max(arr)
runner_up = -9999
for number in arr:
    if number < max and number > runner_up:
        runner_up = number


print(runner_up)



    
