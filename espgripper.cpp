#include <string>
#include <iostream>
const int gripper_Pin = 32;
const int gripper_rotation_Pin=33;  // Define the PWM output pin
int dutycycle_gripper=11.5; 
int dutycycle_gripper_rotation=7;    // Variable to store the received duty cycle value

void setup() {
  Serial.begin(115200);  // Start serial communication
  ledcSetup(0, 50, 8); // Configure PWM channel: Channel 0, 50 Hz frequency, 8-bit resolution
  ledcAttachPin(gripper_Pin, 0);
  ledcSetup(1, 50, 8); // Configure PWM channel: Channel 0, 50 Hz frequency, 8-bit resolution
  ledcAttachPin(gripper_rotation_Pin, 1); // Attach the PWM channel to the output pin
}

void loop() {
//  if (Serial.available()){ 
    String message=String(Serial.parseInt());
    Serial.write(message.encode());

  if(Serial.parseInt()!=0){
  
//    String command_string=Serial.readString();
    int command=Serial.parseInt();
    int gripper_cmd=command/10;
    int gripper_rot_cmd=command%10;
    switch(gripper_cmd){
      case 0:
        dutycycle_gripper=25;
        break;
      case 1:
        dutycycle_gripper=11.5;
        break;
      case 2:
        dutycycle_gripper=5.5;
        break;
      
    }
    switch(gripper_rot_cmd){
      case 0:
        dutycycle_gripper_rotation=50;
        break;
      case 1:
        dutycycle_gripper_rotation=6;
        break;
      case 2:
        dutycycle_gripper_rotation=8;
        break;
    }

     
    
    // dutyCycle = Serial.parseInt();  // Read the duty cycle value from the serial monitor
    ledcWrite(0, map(dutycycle_gripper, 0, 100, 0, 255)); // Set the PWM duty cycle based on the received value
    ledcWrite(1, map(dutycycle_gripper_rotation, 0, 100, 0, 255)); // Set the PWM duty cycle based on the received value
//    dutycycle_gripper++;
//    dutycycle_gripper_rotation++;
//    sleep(1000);
    Serial.println("Duty Cycle set to: " + String(dutycycle_gripper) + "and"+String(dutycycle_gripper_rotation)); // Print the received duty cycle value
}
}//}