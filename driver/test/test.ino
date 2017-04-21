IntervalTimer hz_retrace;

volatile uint16_t cur_line;
const uint16_t MAX_LINE = 310;
const uint16_t SYNC_LINES = 2;

// Pin assignments
const int HZ_SYNC = 11;
const int R_CH = 8;
const int G_CH = 9;
const int B_CH = 10;

void setup() {
  pinMode(HZ_SYNC, OUTPUT);
  digitalWrite(HZ_SYNC, HIGH);
  pinMode(R_CH, OUTPUT);
  pinMode(G_CH, OUTPUT);
  pinMode(B_CH, OUTPUT);
  hz_retrace.begin(hz_interrupt, 63.98);
}

void hz_interrupt(void) {
  noInterrupts();
  // do interrupt for cur_line;
  digitalWrite(HZ_SYNC,LOW);
  // delay for 4.5uS
  delayMicroseconds(3);
  // nops to even out here
  for (uint8_t i = 0; i < 6; i++) __asm__ volatile( "nop;nop;nop;nop;");
  
  if (cur_line < MAX_LINE) { digitalWrite(HZ_SYNC, HIGH); }
  cur_line++;
  if (cur_line > MAX_LINE + SYNC_LINES) { cur_line = 0; }

  // test pattern
  delayMicroseconds(3);
  for (uint16_t j = 0; j < cur_line; j++) __asm__ volatile( "nop;nop;nop;" );
  digitalWrite(R_CH,HIGH);
  __asm__ volatile("nop;nop;nop;");
  digitalWrite(R_CH,LOW);
  interrupts();
}

void loop() {
  
}


