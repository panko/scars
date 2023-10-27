# scars
Speed control and reporting system

## Rules
If the driving speed is less than 50km/h, nothing shall happen.  
If the driving speed is faster than 50km/h but no more than 55km/h, a warning shall be issued to the driver.  
If the driving speed is faster than 55km/h but no more than 60km/h, a fine shall be issued to the driver.  
If the driving speed is faster than 60km/h, the driver's driving licence shall be suspended.  
The speed in km/h shall be available to the system as an integer value.

## Source
https://www.youtube.com/watch?v=lqX6k4I-qAw

## Example
```
prike@xamito:~/scars/scars$ ./scars.py 
Usage: ./scars.py <input number>
prike@xamito:~/scars/scars$ ./scars.py asd
Usage: ./scars.py <input number>; where the input is an integer
prike@xamito:~/scars/scars$ ./scars.py 1
nothing
prike@xamito:~/scars/scars$ ./scars.py 50
warning
prike@xamito:~/scars/scars$ ./scars.py 55
warning
prike@xamito:~/scars/scars$ ./scars.py 56
fine
prike@xamito:~/scars/scars$ ./scars.py 60
fine
prike@xamito:~/scars/scars$ ./scars.py 61
license_suspended
prike@xamito:~/scars/scars$ ./scars.py -69
nothing
```