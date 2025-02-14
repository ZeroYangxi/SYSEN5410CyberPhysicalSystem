from machine import Pin
import math
import time

led = Pin("LED", Pin.OUT)

def soft_pwm(pin, duty, cycle_length_us=2000):
    """
    Software PWM implementation
    duty: 0-100 (duty cycle percentage)
    cycle_length_us: total length of one PWM cycle in microseconds
    """
    if duty <= 0:
        pin.off()
        time.sleep_us(cycle_length_us)
        return
    elif duty >= 100:
        pin.on()
        time.sleep_us(cycle_length_us)
        return
    
    on_time = int(cycle_length_us * duty / 100)
    off_time = cycle_length_us - on_time
    
    pin.on()
    time.sleep_us(on_time)
    pin.off()
    time.sleep_us(off_time)

print("Starting LED PWM fade test...")
start_time = time.ticks_ms()
duration = 10000  # 10 seconds
counter = 0

try:
    while time.ticks_ms() - start_time < duration:
        # Calculate sine wave value (0 to 100)
        current_time = (time.ticks_ms() - start_time) / 1000  # Time in seconds
        # Complete one fade cycle per second
        duty = int(50 + 50 * math.sin(2 * math.pi * current_time))
        
        # Apply PWM
        soft_pwm(led, duty)
        counter += 1
        
    elapsed_time = time.ticks_ms() - start_time
    print(f"Test completed in {elapsed_time} ms")
    print(f"PWM updates: {counter}")
    print(f"Average updates per second: {counter / (elapsed_time / 1000):.2f}")
    
except KeyboardInterrupt:
    print("\nTest interrupted by user")
except Exception as e:
    print(f"\nError occurred: {e}")
finally:
    led.off()
    print("Test ended.")