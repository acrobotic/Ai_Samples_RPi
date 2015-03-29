var wpi = require('wiring-pi');
wpi.setup('wpi');

var led_pin = 1;

wpi.pinMode(led_pin, wpi.OUTPUT);

var value = 1;

var iv = setInterval(function() {
  wpi.digitalWrite(led_pin, value);
  value = +!value;
}, 1*1000);

setTimeout(function () {
  clearInterval(iv);
  wpi.pinMode(led_pin, wpi.INPUT);
}, 60*1000);

