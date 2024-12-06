test_cases = int(input())

for test_case in range(0, test_cases):
    
    
    number_of_trekkers = int(input())
    
    count_even = 0
    count_odd = 0
    
    stamina_str = input()
    stamina = stamina_str.split()
    for S in stamina:
        S = int(S)
        if S%2 != 0:
            count_odd = count_odd + 1
        else:
            count_even = count_even + 1
            
    if count_even > count_odd:
        print("Yes")
    else:
        print("No")