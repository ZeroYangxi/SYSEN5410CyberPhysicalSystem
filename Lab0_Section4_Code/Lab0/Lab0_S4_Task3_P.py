from machine import Pin
import time

# Initialize the built-in LED
led = Pin("LED", Pin.OUT)

print("Starting Digital Output Test...")

# Test from 1 second to 15 seconds
for duration in range(1, 16):
    start_time = time.ticks_ms()
    end_time = start_time + (duration * 1000)  # Convert to milliseconds
    toggle_count = 0
    
    # Toggle the pin as fast as possible for the specified duration
    while time.ticks_ms() < end_time:
        led.value(1)  # HIGH
        led.value(0)  # LOW
        toggle_count += 2  # Count both HIGH and LOW transitions
    
    print(f"Duration: {duration} seconds, Toggle count: {toggle_count}")
    time.sleep_ms(100)  # Brief delay to allow for serial output

print("Test complete.")

