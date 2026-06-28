Problem: Pop Remove Discard
Concept: Command
Platform: Hackerrank

n = int(input())
s = set(map(int, input().split())) # Read the initial set of integers

for _ in range(int(input())):
    command = input().split() # Read the command and its argument (if any)

    if command[0] == "pop":
        s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))  #gives error if element is not present
    elif command[0] == "discard":
        s.discard(int(command[1])) #doesn't gives error if element is not present

print(sum(s))
