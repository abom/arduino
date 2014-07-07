int inPin = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  // more stable
  int value = map(analogRead(inPin), 0, 1023, 0, 9);
  // not stable
  //float value = (analogRead(inPin)/1023.0) * 9.0;
  Serial.println(value);
  //Serial.flush();

  // test
  //float R = (value / 1023.0) * 30;
  //Serial.print(R);
  //Serial.println(" K");
  //delay(10);
}
