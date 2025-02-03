'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
'''

# n = int(input())
# arr = list(map(int, input().split()))
numbers_list = [ -2,-3,-7,-5,-6, -7, -6 ]
new_list = []

# max = max(arr)
# runner_up = -9999
# for number in arr:
#     if number < max and number > runner_up:
#         runner_up = number


# print(runner_up)

max_number = max(numbers_list)
for n in numbers_list:
    if n != max_number:
        new_list.append(n)
second_max_number = max(new_list)
print(second_max_number)
