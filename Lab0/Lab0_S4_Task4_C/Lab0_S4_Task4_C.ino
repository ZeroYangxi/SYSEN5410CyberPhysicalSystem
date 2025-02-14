const int TEMP_SENSOR = 4;  // Temperature sensor is on ADC4

void setup() {
  Serial.begin(115200);
  
  while (!Serial) {
    delay(100);
  }
  
  Serial.println("ADC Performance Test Starting...");
  Serial.println("Time(s), Readings");
  
  // Configure ADC
  analogReadResolution(12);
  
  // Loop through durations from 1 to 15 seconds
  for (int duration = 1; duration <= 15; duration++) {
    // Initialize counter
    unsigned long counter = 0;
    
    // Set start time
    unsigned long startTime = millis();
    
    // While elapsed time is less than duration
    while (millis() - startTime < duration * 1000) {
      analogRead(TEMP_SENSOR);  // Read temperature sensor
      counter++;
    }
    
    // Print results
    Serial.print(duration);
    Serial.print(", ");
    Serial.println(counter);
    
    // Small delay between tests
    delay(100);
  }
  
  Serial.println("Test complete.");
}

void loop() {
  // Nothing to do here
}