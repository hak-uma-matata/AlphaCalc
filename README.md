# AlphaCalc
AlphaCalc is an application that takes verbal input in the form of text or audio, such as "multiply 4 by 3 subtracted by 2" and converts it into a mathematical expression which it evaluates.

Features
-------------
- comes with a memory that can be accessed or cleared at any time
- the way the calculator evaluates expressions is through presets, which can be added or removed at any time
- there are default presets in built, don't worry, you won't need to add "multiply" and "divide" from scratch, we've already done that, for an application that noone's probably going to use (_pain_)

Prerequisites
-------------
The machine must have MySQL installed. The password asked for by AlphaCalc is the MySQL password.

The following modules are to be installed:
- PyQt5
- mysql.connector
- Pyaudio
- playsound
- SpeechRecognition
- gTTS

If these modules are not already installed, just install them from the Command Prompt using:
```pip install <module_name>```

How to Use This
-----------
If this is the first time you are using this application, first run "start_up.py". After this, on all subsequent uses, just run "main.py".



