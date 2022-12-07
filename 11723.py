import sys
def add(number):
    if number not in answer:
        answer.append(number)
def remove(number):
    if number in answer:
        answer.remove(number)
    

def check(number):
    if number in answer:
        print(1)
        return 1
    print(0)
    return 0

def toggle(number):
    if number not in answer:
        answer.append(number)
        return
    answer.remove(number)
    return

def all():
    
    answer = [i for i in range(1,21)]
    return

def empty():
    answer.clear()
    return

command_dict = {'add':add,
            'remove':remove,
            'check':check,
            'toggle':toggle,
            'all':all,
            'empty':empty}
input = sys.stdin.readline
n = int(input())
answer = []

commands = [input().split() for _ in range(n)]
for command in commands:
    if len(command) != 2:
        command_dict[command[0]]()
        
        continue

    command_dict[command[0]](int(command[1]))


