void setup() {
  Serial.begin(115200);
  while (!Serial);
  Serial.println("Starting Float Math Performance Test...");
  
  long test_sizes[] = {1, 10, 100, 1000, 10000, 100000, 1000000};
  int num_tests = sizeof(test_sizes) / sizeof(test_sizes[0]);
  
  for (int i = 0; i < num_tests; i++) {
    long N = test_sizes[i];
    
    unsigned long start_time = millis();
    
    float result = 1.0;
    for (long j = 0; j < N; j++) {
      float a = j * 3.14159;
      float b = j * 2.71828;
      
      if (a + b != 0) {
        result = (a * b)/(a + b);
      } else {
        result = 0.0;
      }
    }
    
    unsigned long elapsed_time = millis() - start_time;
    
    Serial.print("N = ");
    Serial.print(N);
    Serial.print(": Time = ");
    Serial.print(elapsed_time);
    Serial.print(" ms, Final result = ");
    Serial.println(result, 4); // 4 decimals
    
    delay(1000); 
  }
  
  Serial.println("Test complete.");
}

void loop() {
}