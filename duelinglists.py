#Create two seperate lists for player one and player two. 
#Each one should contain 10 random numbers between 1 and 50.
#Again, your lists should be random numbers
#Do NOT sort the lists.
#Compare the lists in order. Whichever list has the higher number wins.
#Keep track of how many times each list wins.
#Find the highest number in each list and it's index. If the number occers multiple times take the first instsance.
#Find the lowest number in each list and it's index. If the number occers multiple times take the first instsance.
#A tie is not record as a win for either player
#Display the lists
#Report to the user how many times each player won and the information from lines 6 and 7.
#For the example output I am limiting the range to 1 to 9 to keep it more readable.

#Player One = 5,7,2,9,1,1,3,8,6,9
#Player Two = 3,8,5,5,8,1,4,7,4,7
#Player one won 5 times
#Player two won 4 times
#Player one's highest number is 9 at index 3
#Player two's highest number is 8 at index 1
#Player one's lowest number is 1 at index 4
#Player two's lowest number is 1 at index 5

import random
player_one = [random.randint(1, 50) for _ in range(10)]
player_two = [random.randint(1, 50) for _ in range(10)]
print("Player One =", player_one)
print("Player Two =", player_two)

p1_wins = 0
p2_wins = 0

for i in range(10):
    if player_one[i] > player_two[i]:
        p1_wins += 1
    elif player_two[i] > player_one[i]:
        p2_wins += 1

p1_max = max(player_one)
p2_max = max(player_two)
p1_max_index = player_one.index(p1_max)
p2_max_index = player_two.index(p2_max)

p1_min = min(player_one)
p2_min = min(player_two)
p1_min_index = player_one.index(p1_min)
p2_min_index = player_two.index(p2_min)

print(f"Player one won {p1_wins} times")
print(f"Player two won {p2_wins} times")
print(f"Player one's highest number is {p1_max} at index {p1_max_index}")
print(f"Player two's highest number is {p2_max} at index {p2_max_index}")
print(f"Player one's lowest number is {p1_min} at index {p1_min_index}")
print(f"Player two's lowest number is {p2_min} at index {p2_min_index}")