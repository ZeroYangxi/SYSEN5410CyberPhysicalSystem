#include <math.h>

const int TEST_DURATION = 10000;  // 10 seconds
const int LED_PIN = LED_BUILTIN;  // Onboard LED

void setup() {
  Serial.begin(115200);
  
  while (!Serial) {
    delay(100);
  }
  
  Serial.println("PWM LED Test Starting...");
  
  // Initialize PWM
  analogWriteResolution(8);  // Set PWM resolution to 8 bits (0-255)
  analogWriteFreq(1000);    // Set PWM frequency to 1000 Hz
  
  unsigned long counter = 0;
  unsigned long startTime = millis();
  
  while (millis() - startTime < TEST_DURATION) {
    // Calculate the phase of the sine wave (0 to 2π)
    // Use integer division to get time within one second (0-999)
    unsigned long timeInCycle = (millis() - startTime) % 1000;
    float phase = (2 * PI * timeInCycle) / 1000.0;
    
    // Calculate LED brightness (0-255) using sine function
    // sin() returns -1 to 1, so we need to scale and offset it
    int brightness = (int)((sin(phase) + 1) * 127.5); // 乘以127.5是为了把0-2的范围映射到0-255
    
    // Set LED brightness
    analogWrite(LED_PIN, brightness);
    
    counter++;
  }
  
  // Turn off LED after test
  analogWrite(LED_PIN, 0);
  
  Serial.print("Test duration: ");
  Serial.print(TEST_DURATION);
  Serial.println(" ms");
  
  Serial.print("Total PWM updates: ");
  Serial.println(counter);
  
  Serial.print("Updates per second: ");
  Serial.println((float)counter * 1000 / TEST_DURATION);
  
  Serial.println("Test complete.");
}

void loop() {
}