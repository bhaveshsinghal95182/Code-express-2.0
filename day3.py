# inefficient brute force
test_cases = int(input())

for _ in range(0, test_cases):
    
    directions = list(map(int, input().split()))
    given_array = list(map(int, input().split()))
    
    if directions[0] == 0:
        for i in range(0, directions[1]):
            temp = given_array[0]
            for j in range(0, len(given_array)-1):
                given_array[j] = given_array[j+1]
            given_array[len(given_array)-1] = temp
    else:
        for i in range(0, directions[1]):
            temp = given_array[len(given_array)-1]
            for j in range(len(given_array)-2, -1, -1):
                given_array[j+1] = given_array[j]
            given_array[0] = temp
    
    answer = ""
    for k in given_array:
        answer += f"{k} "
        
    print(answer)

# efficient approach
test_cases = int(input())

for _ in range(test_cases):
    # Reading the inputs
    direction, no_of_rotations, N = map(int, input().split())
    given_array = list(map(int, input().split()))
    
    # Normalize the number of rotations
    no_of_rotations %= N

    if direction == 0:  # Left rotation
        rotated_array = given_array[no_of_rotations:] + given_array[:no_of_rotations]
    else:  # Right rotation
        rotated_array = given_array[-no_of_rotations:] + given_array[:-no_of_rotations]
    
    # Print the result as a space-separated string
    print(" ".join(map(str, rotated_array)))
