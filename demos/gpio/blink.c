#include <stdio.h>
#include <wiringPi.h>
 
int led_pin = 1;

int main(void)
{
  if (wiringPiSetup() == -1)
    return 1;

  pinMode(led_pin, OUTPUT);
  
  int i;
  for (i = 0; i < 30; ++i)
  {
    digitalWrite(led_pin, 1);
    delay(1000);
    digitalWrite(led_pin, 0);
    delay(1000);
  }

  return 0;
}
