/*
Components:
  0-10KOhm Potentiometer
  Arduino Uno
  Breadboard Wires
  
*/
void setup(){
  Serial.begin(9600);
}

void loop(){
 int sensorValue = analogRead(A0);
 Serial.println(sensorValue);
  delay(1000);
}
