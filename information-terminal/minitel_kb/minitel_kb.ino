
HardwareSerial uart = HardwareSerial();
#define SERIAL_7E1 0x24

#define SOLENOID 4
#define M_KEY 9
#define FN_KEY 10
#define B_KEY 12
#define FOUR_KEY 13
#define V_KEY 14
#define A_KEY 15

#define SPACE_D1 21
#define SPACE_D2 20

boolean check_space() {
  pinMode(SPACE_D1,INPUT);
  digitalWrite(SPACE_D1,HIGH);
  pinMode(SPACE_D2, OUTPUT);
  digitalWrite(SPACE_D2, LOW);
  delay(20);
  boolean is_space = (digitalRead(SPACE_D1) == LOW);
  digitalWrite(SPACE_D1,LOW);
  digitalWrite(SPACE_D2,LOW);
  pinMode(SPACE_D1,INPUT);
  pinMode(SPACE_D2,INPUT);
  return is_space;
}

void setup() {
  //Serial.begin(9600);
  uart.begin(4800);
  UCSR1C = SERIAL_7E1;
  // flush
  delay(50);
  while (Serial.available()) { Serial.read(); }
  while (uart.available()) { uart.read(); }
  pinMode(SPACE_D1,INPUT);
  pinMode(SPACE_D2,INPUT);
  digitalWrite(SOLENOID,LOW); pinMode(SOLENOID,OUTPUT);
  digitalWrite(M_KEY,LOW); pinMode(M_KEY,OUTPUT);
  digitalWrite(FN_KEY,LOW); pinMode(FN_KEY,OUTPUT);
  digitalWrite(B_KEY,LOW); pinMode(B_KEY,OUTPUT);
  digitalWrite(FOUR_KEY,LOW); pinMode(FOUR_KEY,OUTPUT);
  digitalWrite(V_KEY,LOW); pinMode(V_KEY,OUTPUT);
  digitalWrite(A_KEY,LOW); pinMode(A_KEY,OUTPUT);
}

boolean is_awake = false;
unsigned long last_wake = 0;
boolean v_mode = true;

void press_key(int key, boolean fn) {
  if (fn) digitalWrite(FN_KEY,HIGH);
  delay(250);
  digitalWrite(key,HIGH);
  delay(400);
  digitalWrite(key,LOW);
  delay(250);
  if (fn) digitalWrite(FN_KEY,LOW);
  delay(250);
}

void set_baud() {
  press_key(B_KEY,true);
  press_key(FOUR_KEY,false);
}

void enter_mode(boolean mode) {
  if (v_mode != mode) {
    v_mode = mode;
    press_key(M_KEY,true);
    press_key(mode?V_KEY:A_KEY,false);
  }
}

void wake() {
  last_wake = millis();
  if (!is_awake) {
    // 0xED is our "woke up" code
    Serial.write("\xed");
    is_awake = true;
    digitalWrite(SOLENOID,HIGH);
    delay(2000);
    set_baud();
    if (!v_mode) {
      v_mode = true;
      delay(100);
      enter_mode(false);
    }
  }
}

// turn off system after 40 minutes inactivity
unsigned long timeout = 40L*60L*1000L;

void loop() {
  if (Serial.available() > 0) {
    wake();
    int b = Serial.read();
    if (b == 0xee) {
      enter_mode(true);
    } else if (b == 0xef) {
      enter_mode(false);
    }
    uart.write(b);
  }
  if (uart.available() > 0) {
    wake();
    int b = uart.read();
    Serial.write(b);
  }
  if (!is_awake) {
    if (check_space()) {
      wake();
    }
  }
  unsigned long curtime = millis();
  if ((curtime - last_wake) > timeout) {
    digitalWrite(SOLENOID,LOW);
    is_awake = false;
    delay(100);
    while (uart.available() > 0) { uart.read(); }
  }    
}

