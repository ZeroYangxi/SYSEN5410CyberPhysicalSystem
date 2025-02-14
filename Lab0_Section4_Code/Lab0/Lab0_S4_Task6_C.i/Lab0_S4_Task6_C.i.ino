void setup() {
    Serial.begin(115200);
    while (!Serial); // Wait for serial connection
    
    // Start time measurement
    unsigned long start_time = millis();
    
    // Calculate sum using formula: n(n+1)/2
    uint64_t n = 1000000;
    uint64_t result = (n * (n + 1)) / 2;
    
    // End time measurement
    unsigned long end_time = millis();
    unsigned long elapsed_time = end_time - start_time;
    
    // Print results by breaking it into decimal digits
    Serial.print("Sum result: ");
    
    // Convert to decimal digits
    char buf[21]; // Maximum length for uint64_t decimal representation plus null terminator
    uint64_t temp = result;
    int idx = 19; // Start from end of buffer (leaving room for null terminator)
    buf[20] = '\0';
    
    do {
        buf[idx] = '0' + (temp % 10);
        temp /= 10;
        idx--;
    } while (temp > 0);
    
    // Print from first digit
    Serial.println(&buf[idx + 1]);
    
    Serial.print("Elapsed time: ");
    Serial.print(elapsed_time);
    Serial.println(" ms");
}

void loop() {
}