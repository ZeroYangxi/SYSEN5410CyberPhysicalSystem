from machine import ADC, Pin
import time

# Initialize the temperature sensor ADC (connected to ADC4)
sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)  # Convert raw ADC reading to voltage

def test_adc_performance(duration):
    """
    Test how many ADC readings can be performed in a given duration.
    
    Args:
        duration (int): Test duration in seconds
    
    Returns:
        int: Number of ADC readings performed
    """
    counter = 0
    start_time = time.ticks_ms()
    
    # Run until the duration is reached
    while time.ticks_diff(time.ticks_ms(), start_time) < duration * 1000:
        # Read the temperature sensor
        reading = sensor_temp.read_u16()
        counter += 1
    
    return counter

# Main test loop
print("Starting ADC Performance Test...")
print("Duration (s) | Readings")
print("------------|----------")

# Test for durations from 1 to 15 seconds
for duration in range(1, 16):
    readings = test_adc_performance(duration)
    print(f"{duration:10d} | {readings:8d}")
    time.sleep(0.1)  # Small delay between tests

print("\nTest complete.")