#include <Servo.h>
Servo myservo;  // create servo object to control a servo

String serial_in;
const uint8_t led_pin = 8;

// Global temp variables
static uint8_t temp_sensors[] = {A0, A1};
static double prev_temps[] = {0.0, 0.0};
static double temps[] = {0.0, 0.0};
static uint8_t num_temp_sensors = 2;

static unsigned long TELEMETRY_PERIOD = 1000; // 1000 ms default between telemetry grabs
int fullpos = 0; // servo position angles  *SHOULD THESE ALL BE STATIC? WHAT DATA TYPE IS BEST?*
int halfpos = 90;
int closepos = 180;
int currentservopos = 180;
int fancontrol_pin = 11;
int fanfeedback_pin = 2; //define the interrupt pin (must be pin 2 or 3)
int InterruptCounter;
int fanspeed;

double updateTempData(uint8_t sensor_id);
void sendTelemetry();
void runCommand(String serial);
void refreshTelemetryData();

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  pinMode(led_pin, OUTPUT);
  pinMode(fancontrol_pin, INPUT);
  myservo.attach(9); // attaches the servo on pin 9 to the servo object
  myservo.write(closepos); // initial servo position
}

void loop() {
  static unsigned long last_refresh_time = 0;

  // Check if commands are available and run them
  if(Serial.available())
  {
    serial_in = Serial.readString();
    runCommand(serial_in);
  }

  // Check if 1 second has passed, and if so send telemetry data
  if(millis() - last_refresh_time >= TELEMETRY_PERIOD)
  {
    last_refresh_time += TELEMETRY_PERIOD;
    sendTelemetry();
  }

  refreshTelemetryData();
}

void runCommand(String serial)
{
  static uint8_t cmd = serial.substring(0,1).toInt(); // Grabs just the first character
  static String args = serial.substring(2); // Grabs everything past the first comma

  if(cmd == 0)  // Config Parameters
  {
//    Serial.println(args.substring(0,4));
    double freq = args.substring(0,4).toDouble();
    TELEMETRY_PERIOD = (1.0/freq)*1000; // convert freq to period in millis
  }
  if(cmd == 1)  // SetServoPosition
  {
    String servoCMD = args.substring(0,4); // Grabs the first substring within "args" string
    if (servoCMD == "full")
    {
      myservo.write(fullpos);
      currentservopos = 0;
    }
    else if (servoCMD == "half")
    {
      myservo.write(halfpos);
      currentservopos = 90;
    }
    else if (servoCMD == "clse")
    {
      myservo.write(closepos);
      currentservopos = 180;
    }
    
  }
  if(cmd == 2)  // SetFanSpeed
  {
    int fanCMD = args.substring(0,3).toInt(); // Grabs the first substring within "args" string
    if (fanCMD == "max"); //**fix the code so any value between 0% and 100% will map to an analog value
    {
      analogWrite(fancontrol_pin,255);
    }
    if (fanCMD == "75%");
    {
      analogWrite(fancontrol_pin,191);
    }
    if (fanCMD == "50%");
    {
      analogWrite(fancontrol_pin,127);
    }
    if (fanCMD == "25%");
    {
      analogWrite(fancontrol_pin,63);
    }
    // should we add a shutdown command to totally turn the fan off?
  }
  if(cmd == 3)  // SetFanState
  {
    //**On or off
  }
}

void sendTelemetry()
{
  static double temp = 0;
  for(int i = 0; i < num_temp_sensors; i++){
    String serial_data = "1," + String(i) + "," + String(temps[i], 2);
    Serial.println(serial_data);
  }
}

void refreshTelemetryData(){
  // TODO: Include other data updates here
  updateTempData();
}

double updateTempData()
{
  for(int i = 0; i < num_temp_sensors; i++){
    temps[i] = (analogRead(temp_sensors[i])*(5000/1024.0) + prev_temps[i])/2; // Averaging filter
    temps[i] = (temps[i]-110)/10;     // 110 is magic offset for TMP35
    prev_temps[i] = temps[i];
  }
}

double getFanSpeed()
{
  // TODO: Get this into telemetry serial string
  static double fanspeed;
  InterruptCounter = 0;
  attachInterrupt(digitalPinToInterrupt(fanfeedback_pin), counter, RISING);
  delay(1000);
  detachInterrupt(digitalPinToInterrupt(fanfeedback_pin));
  fanspeed = (InterruptCounter / 2) * 60;
  return fanspeed;
}

void counter()
{
  InterruptCounter++;
}
