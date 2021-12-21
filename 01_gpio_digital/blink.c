#include <wiringPi.h>
#define Y 7
#define G 8
#define R 9
int main (void)
{
  //wiringPiSetup();
  wiringPiSetupGpio();
  pinMode (R, OUTPUT);
  pinMode (G, OUTPUT);
  pinMode (Y, OUTPUT);
  for (int i = 0; i < 10; i++)
  {
    digitalWrite(Y, HIGH) ;
    delay (2000) ;
    digitalWrite(Y, LOW);
    digitalWrite(G, HIGH) ;
    delay (2000) ;
    digitalWrite(G, LOW);
    digitalWrite(R, HIGH) ;
    delay (2000) ;
    digitalWrite(R, LOW);
  }
  return 0 ;
}