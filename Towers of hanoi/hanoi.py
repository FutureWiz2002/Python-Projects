from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []

left_stack = Stack('Left')
middle_stack = Stack('Middle')
right_stack = Stack('Right')

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3\n"))

for i in range(num_disks, 0, -1):
    left_stack.push(i)

num_optimal_moves = (2 ** num_disks) -1
print(f"\nThe fastest you can solve this game is in {num_optimal_moves} moves")
#Get User Input
def get_input():

    choices = [stack.get_name()[0] for stack in stacks]
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print(f"Enter {letter} for {name}")
        user_input = input('provide your input here: ')
        if user_input in choices:
            for i in range(len(stacks)):
                return stacks[i]


#Play the Game
num_user_moves = 0
while right_stack.get_size() != num_disks:
    print("\n\n\n...Current Stacks...")
    for i in stacks:
        i.print_items()
    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()

        if from_stack.get_size() == 0:
            print("\nInvalid Move, try again\n")
        elif to_stack.get_size() == 0 or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            
        
        elif to_stack.get_size() == num_disks:
            print("\nThe stack is full")
        else:
            print("Something may have went wrong, contact the software engineer working on it")

print(f"You have completed the game in {num_user_moves} moves. Congrats!")