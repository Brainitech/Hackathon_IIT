Required dependencies need to be installed on the device:

1.uagents

2.response

3.json lib

Able to to run py scripts

Need access to the internet

Perms must be granted for
1. Location (optional) 
2. Notification deamon
3. Display on top

70% idea to be run on windows/mac/linux as a software
20% idea to be run on localhost/online domain
10% idea to be run on mobile as a apk installer

>>DECIDED TO MAKE UI USING HTML/CSS AND HOST IT     ON GITHUB.IO

Frontend must contain:
1. Temperature scale
2. Location list (searchable)
    a. Dictionary containing all cities
    b. Dataset containing all cities (using pandas)
3. Aesthetic and simple design
4. Way to select the alert priority
     a. Minimum (silent notification)
     b. Moderate (notification with sound)
     c. High (silent pop-up if screen on, else pop-up with sound)

Front end structure:
1st field: location with drop down menu

2nd field: default values (yes or no)

3rd field: (if 2nd field is no) max and min temp

4th field/button: start

bottom of the page: credits/details link to source code.
