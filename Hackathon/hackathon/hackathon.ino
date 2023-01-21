/*
  Ultrasonic Sensor HC-SR04 and Arduino Tutorial

  by Dejan Nedelkovski,
  www.HowToMechatronics.com

#include "DHT.h"
#define DHTPIN 2

*/
char ui;

const int trigPin1 = D7;
const int echoPin1 = D8;

const int sp=A0;

const int relay1 = 2;

// defines variables
long duration1;
int distance1;

void setup() {
  Serial.begin(9600); 
  pinMode(trigPin1, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin1, INPUT); // Sets the echoPin as an Input
  pinMode(relay1, OUTPUT);
  digitalWrite(relay1, HIGH);
  // Starts the serial communication
}
void loop() {
  // Clears the trigPin
  digitalWrite(trigPin1, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin1, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin1, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration1 = pulseIn(echoPin1, HIGH);
  // Calculating the distance
  distance1 = duration1 * 0.034 / 2;
  // Prints the distance on the Serial Monitor
  Serial.print(distance1);
  Serial.print(",");
  float moisture_percentage;
  float x=1/analogRead(sp);
  Serial.print(analogRead(sp));
  Serial.print("\n");
  delay(1000);
  ui = Serial.read();
  if(ui=='g'){
      digitalWrite(relay1, LOW);
      delay(1000);
    }
    else{
      digitalWrite(relay1, HIGH);
    }
  
}
