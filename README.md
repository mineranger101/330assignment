What is this repository for?
  This repository contains python code for trvial security device like on a door using a pin pad.
  
  this code uses a FSM to gather wether the entered passcode will change the state to or from lock or unlock.

  Any input that cannot be interpreted as an integer will be discarded before it reaches the FSM.

How do I get set up?
Instructions in this README file are for a Linux environment (Ubuntu 22.04).

Summary of set up
You must have python3 installed before you can complete the setup.

Configuration
Clone the repository:

"$ git clone "
Make sure all the unit tests pass:

$ ./gradlew test
Use your browser to view the test html report, it's at ./app/build/reports/tests/test/packages/edu.iit.cs330.fall2022.html
Build an executable jar:

$ ./gradlew jar
Run the executable:

$ java -jar ./app/build/libs/app.jar
Enter characters from the keyboard, one at a time, followed by Enter/Return and notice how anything other than 1 and 4 will be ignored.
Alternatively you can use the keyboard to enter multiple characters separated by space, e.g. '2 9 7 4 a r 4 1 4' followed by Enter/Return: the application will consume the symbols in the string one at a time and print 'Lock'/'Unlock' as it encounters 4 or 1 respectively.

You could also put data in a file and feed that data to the application, like this:

$ cat mydata | java -jar ./app/build/libs/app.jar
or like this:

$ java -jar ./app/build/libs/app.jar < mydata
Generate jacoco unit-test coverage report:
$ ./gradlew jacocoTestReport
Use your browser to load the html report, it's at ./app/build/reports/jacoco/test/html/edu.iit.cs330.fall2022/index.html
Known bugs
Strings that represent integers bigger than 9 will raise an exception.
Strings that represent negative integers are returned by readInput() as positive integers, need to look into the Scanner class as to why.
License
GNU Public License

Who do I talk to?
Email bistriceanu@iit.edu
