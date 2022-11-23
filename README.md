# What is this repository for?  
   This repository contains python code for trvial security device like on a door using a pin pad.
  
   this code uses a FSM to gather wether the entered passcode will change the state to or from lock or unlock.

   Any input that cannot be interpreted as an integer will be discarded before it reaches the FSM.

# How do I get set up?
   Instructions in this README file are for a Linux environment (Ubuntu 22.04).

# Summary of set up
   You must have python3 installed before you can complete the setup.

# Configuration

   Clone the repository in terminal(everything between the quotations of course):

   $(this should already be here but has been added since it was seen in previous examples by the professor)
   " git clone https://github.com/mineranger101/330assignment.git"
  
  "cd 330assignment"

  then run program using:
   "python3 FA_PT_1.py"
   
   "python3 FA_PT_2.py"

  Once the code has been run enter single digits from 0-9. If a non integer is entered the machine will restart your code input. After the correct passcode is entered     it will prompt you for the key enter 1 or 4 for the corresponding lock and unlock. If anything else is entered as the key the machine will ask you for the passcode    again.

   This lockCheck function takes in a key, which is a numerical unlock or lock value and the current LockStatus which tells us if the access is currently locked and # unlocked. This code block, or method, is called when the correct sequence is entered to the keypad.

# Known Bugs

   none



# Who do I talk to?
    Email Sburton5@hawk.iit.edu
