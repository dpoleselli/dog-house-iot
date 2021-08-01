# Dog House IOT
After recently moving to Texas and experiencing the heat of summer I decided
to create a "smart" dog house for when my German Shepherd is outside. Using a 
Raspberry Pi, I connected a temperature sensor and motion sensor through the
GPIO pins. Every half hour the temperature sensor takes a reading of the 
current temperature, request the expected temperature from a public API,
and then sends the data to Google Sheets to be graphed.

Meanwhile, the motion sensor is setup such that it will detect whenever the 
dog walks into the dog house and then, using uhubctl, the program will give 
power to the USB ports which have a desk fan connected for 30 minutes. 
