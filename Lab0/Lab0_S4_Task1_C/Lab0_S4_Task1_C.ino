void setup() {
  Serial.begin(115200);
  while (!Serial) {
    delay(10);
  }
  Serial.println("Starting Integer Math Performance Test...");
}

void loop() {
  long test_sizes[] = {1, 10, 100, 1000, 10000, 100000, 1000000};
  int num_tests = sizeof(test_sizes) / sizeof(test_sizes[0]);

  for (int i = 0; i < num_tests; i++) {
    long N = test_sizes[i];
    
    unsigned long start_time = millis();
    
    // More intensive calculation
    long result = 1;
    for (long j = 0; j < N; j++) {
      long a = j * 42;
      long b = j * 73;
      result = (result + a * b) % 1000000007;  // Using modulo to prevent overflow
    }
    
    unsigned long elapsed_time = millis() - start_time;
    
    Serial.print("N = ");
    Serial.print(N);
    Serial.print(": Time = ");
    Serial.print(elapsed_time);
    Serial.print(" ms, Final result = ");
    Serial.println(result);
    
    delay(1000);
  }
  
  Serial.println("Test complete. Waiting 10 seconds before repeating...");
  delay(10000);
}