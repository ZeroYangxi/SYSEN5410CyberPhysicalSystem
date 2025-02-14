void setup() {
  Serial.begin(115200);
  while (!Serial);
  
  // 设置LED引脚为输出模式
  pinMode(LED_BUILTIN, OUTPUT);
  
  Serial.println("Starting Digital Output Test...");
  
  // 测试从1秒到15秒
  for (int duration = 1; duration <= 15; duration++) {
    unsigned long startTime = millis();
    unsigned long endTime = startTime + (duration * 1000); // 转换为毫秒
    unsigned long toggleCount = 0;
    
    // 在指定时间内尽可能快地切换引脚状态
    while (millis() < endTime) {
      digitalWrite(LED_BUILTIN, HIGH);
      digitalWrite(LED_BUILTIN, LOW);
      toggleCount += 2; // 计数加2因为完成了一次开和一次关
    }
    
    Serial.print("Duration: ");
    Serial.print(duration);
    Serial.print(" seconds, Toggle count: ");
    Serial.println(toggleCount);
    
    delay(100); // 短暂延迟，让串口有时间输出
  }
  
  Serial.println("Test complete.");
}

void loop() {
  // 空循环，因为只需要运行一次
}