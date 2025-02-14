import _thread
import time

# Shared variables
sum1 = 0
sum2 = 0
lock = _thread.allocate_lock()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def core1_task(start, end):
    """Core 1 计算"""
    global sum2
    local_sum = 0
    for n in range(start, end + 1):
        if is_prime(n):
            local_sum += n
    with lock:
        sum2 = local_sum

def core0_task(start, end):
    """Core 0 计算"""
    global sum1
    for n in range(start, end + 1):
        if is_prime(n):
            sum1 += n

def calc_prime_sum(start, end):
    """双核心计算质数和"""
    global sum1, sum2
    sum1 = sum2 = 0
    
    # 分成两半
    mid = start + (end - start) // 2
    
    # 计时开始
    t0 = time.ticks_ms()
    
    # 启动两个核心
    _thread.start_new_thread(core1_task, (mid + 1, end))
    core0_task(start, mid)
    
    # 等待Core 1
    while sum2 == 0:
        time.sleep_ms(1)
    
    return sum1 + sum2, time.ticks_diff(time.ticks_ms(), t0)

# 测试代码
print("Testing range 1-500,000...")
total, ms = calc_prime_sum(1, 500000)
print(f"Sum: {total}")
print(f"Time: {ms}ms")
