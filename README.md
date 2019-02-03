# Open Sesame


A Python module for biometric verification of a person by voice.

The solution of this problem can find application safety of access to physical objects, information and financial resources. The important case of identification consist in definition of whether two signals belong to a voice of the same speaker. At verification the user shows the identifier in this or that look and the system of recognition should confirm or reject this identifier.

# Installing

You should have Python3.6-3.7 and Linux installed on your machine.

To install this project on your machine, you should download zip or execute the following commands in the terminal:
```sh
git clone https://github.com/DinoTheDinosaur/open_sesame.git\
```
You should also use the modules listed in the requirements.txt file. If you do not have them, run in the Terminal:
```sh
pip install -r requirements.txt
```

# Basic Usage

At first the program asks whether the user has an account. If there is no account, then it is offered to create it, having entered the Username and having recorded a voice which characteristics will be saved in the database. If the account exists, three attempts to log in by means of voice authentication are provided to the user.

Go to open_sesame/src directory:
```sh
cd open_sesame/src
```
Run main.py:
```sh
python main.py
```
If the program works correctly, then on the screen the message will appear:
```sh
---Open SESAME---
A Python module for speech authentification

```
Further the program will ask you: for the first time you use this program or you already have an account:
```sh
Have you got an account?
```
If there is no account, you will be offered to create it: you will need to pronounce randomly generated text within twelve seconds.

If you already have an account, you will be offered to read aloud randomly generated text within four seconds. The program will give confirmation of an entrance to the account:
```sh
Accepted
```
3 attempts are given to the user to try to log in. If the user failed to log in after the 3rd attempt, then the program will display the message:
```sh
Permission denied!
```

# Contributors

- Zorkin Alexandr 
- Baryshev Kirill
- Murtazin Emil
- Popov Daniel 
- Shalgynov Evgeny
- Radnaev Tumen
- Kandryukov Mikhail 
- Burdukovskaya Galina
- Shelest Andrey
- Selezneva Darya

# References

1. https://appliedmachinelearning.blog/2017/06/14/voice-gender-detection-using-gmms-a-python-primer/ - Voice Gender Detection using GMMs : A Python Primer.
2. https://appliedmachinelearning.blog/2017/11/14/spoken-speaker-identification-based-on-gaussian-mixture-models-python-implementation/ - Spoken Speaker Identification based on Gaussian Mixture Models : Python Implementation.
3. https://basegroup.ru/community/articles/em - About ЕМ.
4. https://www.python.org/downloads/ -Download Python.
5. http://practicalcryptography.com/miscellaneous/machine-learning/guide-mel-frequency-cepstral-coefficients-mfccs/ - Mel Frequency Cepstral Coefficient (MFCC) tutorial.

# License

Copyright © 2019 Zorkin Alexander, Baryshev Kirill, Murtazin Emil, Popov Daniel, Shalgynov Evgeny, Radnaev Tumen, Kandryukov Mikhail, Burdukovskaya Galina, Shelest Andrey, Selezneva Darya

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
