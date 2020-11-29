# This is the template code for the CNA337 Final Project
# Zachary Rubin, zrubin@rtc.edu
# CNA 337 Fall 2020

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by SAEID")
# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    import os
    name = "3.16.215.15"
    response = os.system("ping -n 4 " + name)
    # TODO - Call Ping method and print the results
    if response == 0:
        print(name, 'is up!')
    else:
        print(name, 'is down!')
