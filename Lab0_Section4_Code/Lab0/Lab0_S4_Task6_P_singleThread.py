import time

def calculate_sum(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i
    return total


start_time = time.ticks_ms()
result = calculate_sum(1, 1000000)
end_time = time.ticks_ms()

# 计算执行时间(毫秒)
elapsed_time = time.ticks_diff(end_time, start_time)

print(f"Sum: {result}")
print(f"Time taken: {elapsed_time} ms")
