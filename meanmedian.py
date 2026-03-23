#prompt the user to enter 5 numbers. Store them in a list.
#Display the list as entered, small to large, and large to small
#Calculate and display the mean and median
#This is a guided practice. You can follow the video or your instructor will go
#over this in class
# video url: https://youtu.be/VGrRdUunjXg

numbers = []
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)
print("\nOrignal list:", numbers)
print("Small to large:", sorted(numbers))
print("Large to small:", sorted(numbers, reverse=True))

mean = sum(numbers) / len(numbers)
print("Mean:", mean)

nums = sorted(numbers)
mid = len(nums) // 2

if len(nums) % 2 == 1:
    median = nums[mid]
else:
    median = (nums[mid - 1] + nums[mid]) / 2
print("Median:", median)