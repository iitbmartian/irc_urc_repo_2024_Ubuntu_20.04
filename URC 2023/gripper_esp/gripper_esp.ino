#include <string>
#include <iostream>
#define MAX_BUFF_LEN   6
char c;
char str[MAX_BUFF_LEN];
uint8_t idx=0;
//#define TXD_PIN (GPIO_NUM_17)
//#define RXD_PIN (GPIO_NUM_16)

//#define UART UART_NUM_2
//static const int RX_BUF_SIZE = 1024;
//int num = 0;
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
//
//  const uart_config_t uart_config = {
//        .baud_rate = 115200,
//        .data_bits = UART_DATA_8_BITS,
//        .parity = UART_PARITY_DISABLE,
//        .stop_bits = UART_STOP_BITS_1,
//        .flow_ctrl = UART_HW_FLOWCTRL_DISABLE,
//        .source_clk = UART_SCLK_APB,
//};
//
//uart_driver_install(UART, RX_BUF_SIZE * 2, 0, 0, NULL, 0);
//    uart_param_config(UART, &uart_config);
//    uart_set_pin(UART, TXD_PIN, RXD_PIN, UART_PIN_NO_CHANGE, UART_PIN_NO_CHANGE);

}


void loop() {
  if (Serial.available()>0){ 
    c=Serial.read() ;    //Read one byte
    if(c!='\n'){ //Still Reading
      str[idx++]=c;
    }
    else{
      str[idx]='\0';//Convert into a string
      idx=0;
    }
//    String command_sentence=str;
    int command=0;
    int gripper_cmd=command/10;
    int gripper_rot_cmd=command%10;
    Serial.println(str[0]);
//    Serial.println(str[1]);
//    Serial.println(str[2]);
//    Serial.println(str[3]);
   
//    Serial.println(command_sentence);
    
    switch(str[0]){
      case 'a':
        dutycycle_gripper=0;
        dutycycle_gripper_rotation=7;
        break;
      case 'b':
        dutycycle_gripper=0;
        dutycycle_gripper_rotation=8;
        break;
      case 'c':
        dutycycle_gripper=0;
        dutycycle_gripper_rotation=6;
        break;
      case 'd':
        dutycycle_gripper=11.5;
        dutycycle_gripper_rotation=7;
        
        break;
      case 'e':
        dutycycle_gripper=11.5;
        dutycycle_gripper_rotation=8;
        break;
      case 'f':
        dutycycle_gripper=11.5;
        dutycycle_gripper_rotation=6;
        break;
      case 'g':
        dutycycle_gripper=5.5;
        dutycycle_gripper_rotation=7;
        break;
      case 'h':
        dutycycle_gripper=5.5;
        dutycycle_gripper_rotation=8;
        break;
      case 'i':
        dutycycle_gripper=5.5;
        dutycycle_gripper_rotation=6;
        break;
    }

     
    
    // dutyCycle = Serial.parseInt();  // Read the duty cycle value from the serial monitor
    ledcWrite(0, map(dutycycle_gripper, 0, 100, 0, 255)); // Set the PWM duty cycle based on the received value
    ledcWrite(1, map(dutycycle_gripper_rotation, 0, 100, 0, 255)); // Set the PWM duty cycle based on the received value
//    dutycycle_gripper++;
//    dutycycle_gripper_rotation++;
//    sleep(1000);
    //Serial.println("Duty Cycle set to: " + String(dutycycle_gripper) + "and"+String(dutycycle_gripper_rotation)); // Print the received duty cycle value
}
}
