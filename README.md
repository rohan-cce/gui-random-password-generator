# gui-random-password-generator
GUI PASSWORD GENERATOR:
Almost everyone of us have our own Gmail account right? We are using our Gmail account to access Google play store ,YouTube and other apps. Do you think your account is safe? While creating your Google account you will be setting for a password. Most probably we used to set our name, our birthday date  and other common things as our password right? Sometimes we even type the word “PASSWORD “ as our password. Do you think your password is safe and nobody could crack it? I shocked! When I hear that most of our passwords are weak and it is easy to crack. Not only in Gmail but we use passwords everywhere. And most of  use same password everywhere as we tend to forget it soon. And if your password is once cracked, then think all your accounts will be easily hacked. It is a big risk right? You know what? A password which is a combination of upper case, lower case letters, numbers and special characters is said to be strong. Don’t scratch your head for finding a stronger password. We are here to help you out! we had created  a GUI password generator for you using python. All you need to do is a simple thing. just enter the length of the password which should be generated. And that’s it! your random password will be  generated within few seconds. You can copy and paste the password into your notes so that it will be helpful when you forget it. Without further delay, let us move into our code.
1>In the first step we are importing tkinter module as we used tkinter as our framework. Followed by pyperclip module to copy generated module to clipboard and random module to generate random password.
2>next we are setting the width and height of GUI
3>after that we are declaring a variable to store the generated password and another variable to get the password length from user.
4>Next we are defining a function to generate password  and storing the  keys to generate password  
5>Then we are using a loop to generate password of required length followed by setting  password to entry widget.
6>now another function is defined to copy password to clipboard and then we are creating a text label widget.
7>Now buttons are created to call the copytoclipboard function
8>Mainloop is an infinite loop used to run the application when it’s in ready state.
