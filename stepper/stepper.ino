#include <AccelStepper.h>
 
const int DIR = 12;
const int STEP = 13;
const int no_of_rotations=10;
 
#define motorInterfaceType 1
AccelStepper motor(motorInterfaceType, STEP, DIR);
 
void setup() {
  Serial.begin(9600);
  motor.setMaxSpeed(200);
  motor.setAcceleration(500);
//  motor.setSpeed(200);
//  motor.moveTo(-1800);
  
}
 
void loop() {
  motor.runToNewPosition(0);
  motor.runToNewPosition(200*no_of_rotations);
  motor.runToNewPosition(0);
  
// if (motor.distanceToGo() == 0) {
//    motor.moveTo(-motor.currentPosition());
//    
//    Serial.println("Rotating Motor in opposite direction...");
//  }
//  motor.run();/
//  delay(1);
  delay(1000);
}
