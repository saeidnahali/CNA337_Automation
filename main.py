# This is the template code for the CNA337 Final Project
# Zachary Rubin, zrubin@rtc.edu
# CNA 337 Fall 2020
# I worked with Abdi, Dorin and Igor, Mohammad and Saeid on this code.
# Liviu Patrisco (Liviu_patrisco@hotmail.com) helped us to write the code.

from Server import Server


def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by SAEID")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    ec2_ip_address = "3.16.215.15"
    server = Server(ec2_ip_address)
    result = server.ping()
    print(result)
    if result == 0:
        print("Server with ip [%s] is up." % ec2_ip_address)
    else:
        print("Server with ip [%s] is down." % ec2_ip_address)
