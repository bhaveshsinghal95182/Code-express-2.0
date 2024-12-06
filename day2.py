test_cases = int(input())

for _ in range(test_cases):
    N, M = map(int, input().split())
    mountain_heights = list(map(int, input().split()))
    auspicious_numbers = list(map(int, input().split()))
    

    freq = {}
    for h in mountain_heights:
        freq[h] = freq.get(h, 0) + 1
    
    max_count = 0
    number_we_want = float('inf')
    
    for a in auspicious_numbers:
        count = 0
        multiplier = 1
        
        while a * multiplier <= 100000:
            if a * multiplier in freq:
                count += freq[a * multiplier]
            multiplier += 1
        
        if count > max_count or (count == max_count and a < number_we_want):
            max_count = count
            number_we_want = a
    
    print(number_we_want)
