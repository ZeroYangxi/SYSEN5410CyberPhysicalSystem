import _thread
import time

# 共享变量
partial_sum1 = 0  # Core 0 的结果
partial_sum2 = 0  # Core 1 的结果
lock = _thread.allocate_lock()  # 创建锁用于同步

# Core 1 上运行的函数
def calculate_partial_sum_core1(start, end):
    global partial_sum2
    local_sum = 0
    for i in range(start, end + 1):
        local_sum += i
    
    # 使用锁来安全地更新共享变量
    with lock:
        global partial_sum2
        partial_sum2 = local_sum

# Core 0 上运行的函数
def calculate_sum_core0(start, end):
    global partial_sum1
    local_sum = 0
    for i in range(start, end + 1):
        local_sum += i
    partial_sum1 = local_sum

# 记录开始时间
start_time = time.ticks_ms()

# 在 Core 1 上启动第二个线程
_thread.start_new_thread(calculate_partial_sum_core1, (500001, 1000000))

# 在 Core 0 (主线程) 上执行计算
calculate_sum_core0(1, 500000)

# 等待 Core 1 完成计算
while partial_sum2 == 0:
    time.sleep(0.001)  # 小睡一下，避免忙等待

# 计算总和
total_sum = partial_sum1 + partial_sum2

# 记录结束时间
end_time = time.ticks_ms()

# 计算执行时间
elapsed_time = time.ticks_diff(end_time, start_time)

# 打印结果
print(f"Sum: {total_sum}")
print(f"Time taken: {elapsed_time} ms")