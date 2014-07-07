// simple sketch for led control over serial port
// led pins, single led will be chosen 
// chosen led => on
// the other two leds => off.
const int ledPins[3] = {2, 3, 4};
const char leds[] = {'A', 'B', 'C'};

// turn on one led by A, B, C from serial
void turnLedOn(char led)
{
    int led_on;
    
    switch(led)
    {
      case 'A':
      case 'a': led_on = 0; break;
      case 'B':
      case 'b': led_on = 1; break;
      case 'C':
      case 'c': led_on = 2; break;
      default:  led_on = -1; break; // return
    }
    
    for(int i=0; i < 3; i++)
    {
      if(i == led_on)
      {
        // turn on our led
        digitalWrite(ledPins[i], HIGH);
        // tell host
        Serial.print(leds[i]);
        Serial.println(" is On!");
      }
      else
        // turn the others off
        digitalWrite(ledPins[i], LOW);
    }
}

void setup()
{
  // start connection with 9600 baud rate.
  Serial.begin(9600);
  // setting led pins for output
  for(int i=0; i<3; i++)
    pinMode(ledPins[i], OUTPUT);
}


void loop()
{
  // check for input
  char chosen_led = '\0';
  // if any thing sent...
  if(Serial.available())
  {
    // read one char
    chosen_led = (char) Serial.read();
    // turn our led
    turnLedOn(chosen_led);
  }
}
    
