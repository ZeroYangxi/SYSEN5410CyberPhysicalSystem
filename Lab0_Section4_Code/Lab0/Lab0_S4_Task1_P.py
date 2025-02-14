import time

print("Starting Integer Math Performance Test...")
test_sizes = [1, 10, 100, 1000, 10000, 100000, 1000000]

for N in test_sizes:
    start_time = time.ticks_ms()
    
    result = 1
    for j in range(N):
        first_int = j * 42
        second_int = j * 73
        third_int = (first_int + second_int) * (first_int - second_int) % 1000000007
        result = (result + third_int) % 1000000007
        
    elapsed_time = time.ticks_diff(time.ticks_ms(), start_time)
    
    print(f"N = {N}: Time = {elapsed_time} ms, Final result = {result}")

print("Test complete.")