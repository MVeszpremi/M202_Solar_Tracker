#include <TMC2209.h>
//MUST INSTQALL TMC2209 by Peter Polidoro

// This example will not work on Arduino boards without HardwareSerial ports,
// such as the Uno, Nano, and Mini.
//
// See this reference for more details:
// https://www.arduino.cc/reference/en/language/functions/communication/serial/
//
// To make this library work with those boards, refer to this library example:
// examples/UnidirectionalCommunication/SoftwareSerial

HardwareSerial & serial_stream = Serial3;

const uint8_t STEP_PIN = 5; //7
const uint8_t DIRECTION_PIN = 4; //6
const uint8_t STEP_PIN_TOP = 7; //7
const uint8_t DIRECTION_PIN_TOP = 6; //6

const uint8_t TOP_TMR_PIN = 11;
const uint8_t BOTTOM_TMR_PIN = 9;


const int max_angle_top = 275;
const int min_angle_top = -600;
const int max_angle_bottom = 275;
const int min_angle_bottom = -275;

int current_angle_top = 0;
int current_angle_bottom = 0;

int desired_angle_top = 0;
int desired_angle_bottom = 0;


String s_serial_input = "";
uint8_t u8_serial_in_receipt = 0;


// current values may need to be reduced to prevent overheating depending on
// specific motor and power supply voltage
const uint8_t RUN_CURRENT_PERCENT = 50;


// Instantiate TMC2209
TMC2209 stepper_driver;

void setup()
{
  Serial.begin(115200);
  stepper_driver.setup(serial_stream);

  pinMode(STEP_PIN, OUTPUT);
  pinMode(DIRECTION_PIN, OUTPUT);
    pinMode(STEP_PIN_TOP, OUTPUT);
  pinMode(DIRECTION_PIN_TOP, OUTPUT);

  pinMode(TOP_TMR_PIN, INPUT);
  digitalWrite(TOP_TMR_PIN, HIGH);
  pinMode(BOTTOM_TMR_PIN, INPUT);
  digitalWrite(BOTTOM_TMR_PIN, HIGH);

  stepper_driver.setRunCurrent(RUN_CURRENT_PERCENT);
  stepper_driver.setHoldCurrent(20);
  stepper_driver.disableCoolStep();
  stepper_driver.disableStealthChop();
  stepper_driver.setMicrostepsPerStep(2); //10000 steps per revolution // 27.7 ... ~28 steps per degree. 
  stepper_driver.setStandstillMode(stepper_driver.NORMAL);
  stepper_driver.enable();

  calibrateTopMotorAndCenter();
  calibrateBottomMotorAndCenter();
  calibrateTopMotorAndCenter();
  calibrateBottomMotorAndCenter();

  Serial.print("r");
}

void loop()
{
 
if(Serial.available()){
  char r = Serial.read();
  if(r == 'a' && u8_serial_in_receipt == 0){
    u8_serial_in_receipt = 1;
    s_serial_input = "";
    }else if(r == 'b' && u8_serial_in_receipt == 1){
      u8_serial_in_receipt = 2;
      Serial.print('c');
      }else if(u8_serial_in_receipt == 1){
        s_serial_input += r;
        }
  }

  if(u8_serial_in_receipt == 2){
    String receivedString = s_serial_input;
    // Variables to store the split numbers

    // Find the position of the comma in the string
    int commaIndex = receivedString.indexOf(',');

    if (commaIndex != -1) {
      // Extract the substrings from the received string
      String firstNumberString = receivedString.substring(0, commaIndex);
      String secondNumberString = receivedString.substring(commaIndex + 1);

      // Convert the substrings to integers
      desired_angle_top = firstNumberString.toInt();
      desired_angle_bottom = secondNumberString.toInt();

    }
    u8_serial_in_receipt = 0;
    }

  if(desired_angle_top >= min_angle_top && desired_angle_top <= max_angle_top && desired_angle_bottom >= min_angle_bottom && desired_angle_bottom <= max_angle_bottom){

      int angle_to_move_top = desired_angle_top - current_angle_top;
      int angle_to_move_bottom = desired_angle_bottom - current_angle_bottom;

      if(angle_to_move_top !=0 || angle_to_move_bottom != 0){
      moveAngleTop(angle_to_move_top);
      moveAngleBottom(angle_to_move_bottom);
      
      current_angle_top = desired_angle_top;
      current_angle_bottom = desired_angle_bottom;

      Serial.print('d');
  
  }

    
    }

    

 
}

void moveAngleTop(int angle){
  if(angle < 0){
    digitalWrite(DIRECTION_PIN_TOP, HIGH);
    angle = angle * -1;
    }else if(angle > 0){
      digitalWrite(DIRECTION_PIN_TOP, LOW);
      }
    int steps = (int)(2.77*(float)angle);
     for(int i=0; i<steps; i++){
       digitalWrite(STEP_PIN_TOP, HIGH);
    delay(1);
    digitalWrite(STEP_PIN_TOP, LOW);
    delay(4);
      } 
  }

void moveAngleBottom(int angle){
  if(angle < 0){
    digitalWrite(DIRECTION_PIN, HIGH);
    angle = angle * -1;
    }else if (angle > 0){
      digitalWrite(DIRECTION_PIN, LOW);
      }
  int steps = (int)(2.77*(float)angle);
     for(int i=0; i<steps; i++){
       digitalWrite(STEP_PIN, HIGH);
    delay(1);
    digitalWrite(STEP_PIN, LOW);
    delay(4);
      } 
  }


void calibrateTopMotorAndCenter(){
    int counter = 0;
    
  //if clockwise rotated then sensor will be LOW
  if(digitalRead(TOP_TMR_PIN) == LOW){
      digitalWrite(DIRECTION_PIN_TOP, HIGH); //CCW 
   while(counter < 2500){
    counter++;
    digitalWrite(STEP_PIN_TOP, HIGH);
    delay(1);
    digitalWrite(STEP_PIN_TOP, LOW);
    delay(4);

    if(digitalRead(TOP_TMR_PIN) == HIGH){
 //     Serial.println("TMR TOP DETECTED");
      break;
      }
    }
 
  }else{//if ccw rotated the sensor will be HIGH.
      digitalWrite(DIRECTION_PIN_TOP, LOW); //CW 
    while(counter < 2500){
    counter++;
    digitalWrite(STEP_PIN_TOP, HIGH);
    delay(1);
    digitalWrite(STEP_PIN_TOP, LOW);
    delay(4);

    if(digitalRead(TOP_TMR_PIN) == LOW){
    //  Serial.println("TMR TOP DETECTED");
      break;
      }
    }
    }
    delay(500); 
    //Move position to exactly vertical
    digitalWrite(DIRECTION_PIN_TOP, HIGH); //CCW 
    for(int i=0; i<280; i++){
       digitalWrite(STEP_PIN_TOP, HIGH);
    delay(1);
    digitalWrite(STEP_PIN_TOP, LOW);
    delay(4);
      } 
  }

  
void calibrateBottomMotorAndCenter(){
    int counter = 0;
    
  //if CCW rotated then sensor will be LOW
  if(digitalRead(BOTTOM_TMR_PIN) == LOW){
      digitalWrite(DIRECTION_PIN, LOW); //CW 
   while(counter < 2500){
    counter++;
    digitalWrite(STEP_PIN, HIGH);
    delay(1);
    digitalWrite(STEP_PIN, LOW);
    delay(4);

    if(digitalRead(BOTTOM_TMR_PIN) == HIGH){
   //   Serial.println("TMR BOTTOM DETECTED");
      break;
      }
    }
 
  }else{//if cw rotated the sensor will be HIGH.
      digitalWrite(DIRECTION_PIN, HIGH); //CCW 
    while(counter < 2500){
    counter++;
    digitalWrite(STEP_PIN, HIGH);
    delay(1);
    digitalWrite(STEP_PIN, LOW);
    delay(4);

    if(digitalRead(BOTTOM_TMR_PIN) == LOW){
    //  Serial.println("TMR BOTTOM DETECTED");
      break;
      }
    }
    }
    delay(500); 
    //Move position to exactly vertical
    digitalWrite(DIRECTION_PIN, LOW); //CW 
    for(int i=0; i<360; i++){
       digitalWrite(STEP_PIN, HIGH);
    delay(1);
    digitalWrite(STEP_PIN, LOW);
    delay(4);
      } 
  }
