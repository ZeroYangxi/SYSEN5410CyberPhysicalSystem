import time

print("Starting Float Math Performance Test...")

test_sizes = [1, 10, 100, 1000, 10000, 100000, 1000000]

while True:
    for N in test_sizes:
        start_time = time.ticks_ms()
        result = 1.0  # initialize为浮点数
        
        for j in range(N):
            a = j * 3.14159  # 用pi来确保是浮点运算
            b = j * 2.71828  # 用e来确保是浮点运算
            
            result = (a * b)/(a + b) if (a + b) != 0 else 0.0
            
        elapsed_time = time.ticks_diff(time.ticks_ms(), start_time)
        
        print(f"N = {N}: Time = {elapsed_time} ms, Final result = {result:.4f}") 
        
        time.sleep(1)
    
    print("Test complete. Waiting 10 seconds before repeating...")
    time.sleep(10)