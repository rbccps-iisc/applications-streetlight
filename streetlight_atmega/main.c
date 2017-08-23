
/*
This file bifurcates the working state of device into 
two states based on the working of  the established connection 
between device and STM. 
*/
#include<avr/interrupt.h>
#include<avr/io.h>
#include<avr/eeprom.h>
#include <util/delay.h>
#include <stdio.h>
#include <stdint.h>
#include <compat/deprecated.h>
#define BAUD 9600                                 // define baud
#define BAUDRATE ((16000000)/(BAUD*16UL)-1)            // set baud rate value for UBRR,16000000 is the clock frequency
const uint16_t *lower_address=0x00, *higher_address=0x02;
uint16_t lux_threshold_lower=700,lux_threshold_higher=100;    //to be set via setup policy
volatile int i=0,act=0;
volatile unsigned long count = 0;
volatile char command[10];
char lux1[4], lux2[4], temperature[4], voltage[4], current[4];
char bright = 'a';
char off='0'; // when LED has to be switched off
uint16_t current_temp,current_lux;
enum State{Fallback,Active,Waiting};
enum State state=Active;
char delimiter = ',';
char newline = '\n';
void uart_transmit(char b)
{
  while (!( UCSRA & (1<<UDRE)));	// wait for the data register to clear
  UDR = b;
}
ISR(USART_RXC_vect)							// Interrupt called whenever receive complete falg is set 
{
  char ReceivedByte;
  ReceivedByte = UDR;
  if(ReceivedByte == 10)
  {
    act = 1;
    i=0;
  } 
  else
  { 
    command[i]=ReceivedByte;
    i++;
    act =0;
  }
  state = Active;
  TCNT1 = 0;
  count=0;
}
ISR(TIMER1_COMPA_vect)						// timer interrupt
{
  count++;
  if((count!=0)&&(count%900==0))
    state = Fallback;
}
uint16_t ReadADC(uint8_t ch)
//unsigned char ReadADC(uint8_t ch)
{
   //Select ADC Channel ch must be 0-7
   uint8_t channel;
   channel=ch&0b00000111;
   ADMUX|=channel;

   //Start Single conversion
   ADCSRA|=(1<<ADSC);

   //Wait for conversion to complete
   while(ADCSRA & (1<<ADSC));
   while(!(ADCSRA & (1<<ADIF)));

   //Clear ADIF by writing one to it
   //Note you may be wondering why we have write one to clear it
   //This is standard way of clearing bits in io as said in datasheets.
   //The code writes '1' but it results in setting bit to '0' !!!

   ADCSRA|=(1<<ADIF);

   return(ADC);
   //return(ADCH);
}
void InitADC()
{
  ADMUX=(1<<REFS0);                         // For Aref=AVcc;
  ADCSRA=(1<<ADEN)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0); //Prescalar div factor =128, pg
}
void set_brightness(char b)
{
	if(b=='0'){		
		sbi(PORTD,7);
		sbi(PORTB,2);
		sbi(PORTB,5);
		sbi(PORTD,5);
		sbi(PORTD,6);
		sbi(PORTB,3);
		sbi(PORTB,4);
		sbi(PORTD,4);
		sbi(PORTD,2);
		sbi(PORTD,3);}
    else if(b=='1'){
		cbi(PORTD,7);
		sbi(PORTB,2);
		sbi(PORTB,5);
		sbi(PORTD,5);
		sbi(PORTD,6);
		sbi(PORTB,3);
		sbi(PORTB,4);
		sbi(PORTD,4);
		sbi(PORTD,2);
		sbi(PORTD,3);}
	else if(b=='2'){
		cbi(PORTD,7);
		cbi(PORTB,2);
		sbi(PORTB,5);
		sbi(PORTD,5);
		sbi(PORTD,6);
		sbi(PORTB,3);
		sbi(PORTB,4);
		sbi(PORTD,4);
		sbi(PORTD,2);
		sbi(PORTD,3);}
	else if(b=='3'){
		cbi(PORTD,7);
		cbi(PORTB,2);
		cbi(PORTB,5);
		sbi(PORTD,5);
		sbi(PORTD,6);
		sbi(PORTB,3);
		sbi(PORTB,4);
		sbi(PORTD,4);
		sbi(PORTD,2);
		sbi(PORTD,3);}
    else if(b=='4'){
		cbi(PORTD,7);
		cbi(PORTB,2);
		cbi(PORTB,5);
		cbi(PORTD,5);
		sbi(PORTD,6);
		sbi(PORTB,3);
		sbi(PORTB,4);
		sbi(PORTD,4);
		sbi(PORTD,2);
		sbi(PORTD,3);}	     
	else if(b=='5'){
		cbi(PORTD,7);
		cbi(PORTB,2);
		cbi(PORTB,5);
		cbi(PORTD,5);
		cbi(PORTD,6);
		sbi(PORTB,3);
		sbi(PORTB,4);
		sbi(PORTD,4);
		sbi(PORTD,2);
		sbi(PORTD,3);}
	else if(b=='6'){
		cbi(PORTD,7);
		cbi(PORTB,2);
		cbi(PORTB,5);
		cbi(PORTD,5);
		cbi(PORTD,6);
		cbi(PORTB,3);
		sbi(PORTB,4);
		sbi(PORTD,4);
		sbi(PORTD,2);
		sbi(PORTD,3);}  	
    else if(b=='7'){
		cbi(PORTD,7);
		cbi(PORTB,2);
		cbi(PORTB,5);
		cbi(PORTD,5);
		cbi(PORTD,6);
		cbi(PORTB,3);
		cbi(PORTB,4);
		sbi(PORTD,4);
		sbi(PORTD,2);
		sbi(PORTD,3);}	        
	else if(b=='8'){  
		cbi(PORTD,7);
		cbi(PORTB,2);
		cbi(PORTB,5);
		cbi(PORTD,5);
		cbi(PORTD,6);
		cbi(PORTB,3);
		cbi(PORTB,4);
		cbi(PORTD,4);
		sbi(PORTD,2);
		sbi(PORTD,3);}
	else if(b=='9'){	 
		cbi(PORTD,7);
		cbi(PORTB,2);
		cbi(PORTB,5);
		cbi(PORTD,5);
		cbi(PORTD,6);
		cbi(PORTB,3);
		cbi(PORTB,4);
		cbi(PORTD,4);
		cbi(PORTD,2);
		sbi(PORTD,3);}	
	else if(b=='a'){	 
                cbi(PORTD,7);
		cbi(PORTB,2);
		cbi(PORTB,5);
		cbi(PORTD,5);
		cbi(PORTD,6);
		cbi(PORTB,3);
		cbi(PORTB,4);
		cbi(PORTD,4);
		cbi(PORTD,2);
		cbi(PORTD,3);}
}
void get_temperature()			// read temperature from sensor connected to channel 4
{
  int n=0;
  uint16_t adc_result1;
  ADCSRA &= ~((1<<ADEN));
  InitADC();
  _delay_ms(10);
  adc_result1=ReadADC(4);
  //itoa(adc_result1,temperature,10);
  sprintf(temperature,"%d",adc_result1);
  for(n=0;temperature[n]!='\0';n++)
	{
		uart_transmit(temperature[n]);
	}
}
void get_lux()					// read ambient lux channel(0) and led lux (2)
{
  int n;
  uint16_t adc_result1;
  ADCSRA &= ~((1<<ADEN));
  InitADC();
  _delay_ms(10);
  
  adc_result1=ReadADC(2);
  //itoa(adc_result1,lux1,10);
  sprintf(lux1,"%d",adc_result1);
  for(n=0;lux1[n]!='\0';n++)
    {
		uart_transmit(lux1[n]);
	}
  uart_transmit(delimiter);

  ADCSRA &= ~((1<<ADEN));
  InitADC();
  _delay_ms(10);
  
  adc_result1=ReadADC(0);
  //itoa(adc_result1,lux1,10);
  sprintf(lux2,"%d",adc_result1);
  for(n=0;lux1[n]!='\0';n++)
    {
		uart_transmit(lux2[n]);
	}
}
uint16_t get_lux_Fallback()
{
  uint16_t adc_result1;
  ADCSRA &= ~((1<<ADEN));
  InitADC();
  _delay_ms(10);
  
  adc_result1=ReadADC(2);
  
  return (adc_result1);      // assuming ambient lux sensor is connected to channel 0
}
void get_voltage()
{
  int n;
  uint16_t adc_result1;
  ADCSRA &= ~((1<<ADEN));
  InitADC();
  _delay_ms(10);

  adc_result1=ReadADC(1);
  //itoa(adc_result1,voltage,10);
  sprintf(voltage,"%d",adc_result1);
  for(n=0;voltage[n]!='\0';n++)
   {
	uart_transmit(voltage[n]);
   }	
}
void get_current()
{
  int n;
  uint16_t adc_result1;
  ADCSRA &= ~((1<<ADEN));
  InitADC();
  _delay_ms(10);
  adc_result1=ReadADC(3);
  //itoa(adc_result1,current,10);
  sprintf(current,"%d",adc_result1);
  for(n=0;current[n]!='\0';n++)
   {
	uart_transmit(current[n]);
   }	
}

void send_lux()						// send the threshold values for lux when device goes into fallback
{
  int n;
  uint16_t lux_lower, lux_higher;
  char str1[4],str2[4];
  lux_lower = eeprom_read_word(lower_address);
  lux_higher = eeprom_read_word(higher_address);
  sprintf(str1,"%d",lux_lower);
  for(n=0;str1[n]!='\0';n++)
   {
	uart_transmit(str1[n]);
   }
  uart_transmit(delimiter);
    sprintf(str2,"%d",lux_higher);
  for(n=0;str2[n]!='\0';n++)
   {
	uart_transmit(str2[n]);
   }
}
void main(void)
{
  // set uart interrupt when data register receives a character
  UBRRH = (BAUDRATE>>8);                      // shift the register right by 8 bits
  UBRRL = BAUDRATE;                           // set baud rate
  UCSRB  = (1<<TXEN)|(1<<RXEN);                // enable receiver and transmitter
  UCSRC  = (1<<URSEL)|(1<<UCSZ0)|(1<<UCSZ1);   // 8bit data format
  UCSRB |= (1<<RXCIE);
  //set timer1 interrupt at 1Hz
  TCCR1A = 0;// set entire TCCR1A register to 0
  TCCR1B = 0;// same for TCCR1B
  TCNT1  = 0;//initialize counter value to 0
  // set compare match register for 1hz increments
  OCR1A =15624;// = [(16*10^6) / (1*1024) - 1] (must be <65536) for 1 second 
  // turn on CTC mode
  TCCR1B |= (1 << WGM12);
  // Set CS12 and CS10 bits for 1024 prescaler
  TCCR1B |= (1 << CS12) | (1 << CS10);  
  // enable timer compare interrupt
  TIMSK |= (1 << OCIE1A);
  sei();
  DDRB |= 0x3C; 
  DDRD |= 0xFC;
  set_brightness('0');
  eeprom_write_word(lower_address,lux_threshold_lower);
  eeprom_write_word(higher_address,lux_threshold_higher);
  int interval =0, multiplier = 0;
  char bright_level = '0';
  while(1)
  {
    switch(state)
	{
    case(Active):
    { 
      if(act == 1)
      {
        act = 0;
        switch(command[1])
        {
          case('s'):
          {
            get_temperature();
			uart_transmit(delimiter);
            get_lux();
			uart_transmit(delimiter);
            get_voltage();	
			uart_transmit(delimiter);		
            get_current();
			uart_transmit(delimiter);
            send_lux();
			uart_transmit(newline);
            state=Waiting;
            break;
          }
          case('b'):
          {
            set_brightness(command[2]);
            state=Waiting;
            break;  
          }
          case('p'):
          {
            lux_threshold_lower = 4*command[2];
             lux_threshold_higher = 4*command[3];
			eeprom_write_word(lower_address,lux_threshold_lower);
			eeprom_write_word(higher_address,lux_threshold_higher);
            state=Waiting;
            break;
          }
        }
      }
      break;
    }
    case(Fallback):
    {
      current_lux=get_lux_Fallback();
	  interval = (lux_threshold_lower-lux_threshold_higher)/10;			// map the lux and brightness level assuming linear curve 
	  multiplier = (current_lux - lux_threshold_higher)/interval;
	  if(multiplier < 0) set_brightness('0');
	  else
	  if(multiplier > 9) set_brightness('a');
	  else 
	  {
		bright_level = multiplier+48;
		set_brightness(bright_level);
	  }	  
      state = Waiting;
      break;
    }
    case(Waiting):
    {
      break;
    }
  }
  if(act == 1)
    state = Active;
  }

}

AVRGCC2.c
Displaying AVRGCC2.c.