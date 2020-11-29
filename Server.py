import os
class Server:
    def __init__(self, server_ip):
        # TODO -""" Create a ServerClass with a server_ip instantiated"""
        self.server_ip = server_ip
    def get_server_ip(self):
        # TODO - Use os module to ping the server
        return self.server_ip
    def ping(self):
         response = os.system("ping -n 4 -W 5 " + self.server_ip + " > /dev/null 2>&1")
        # if command response is 0, then server is up and running
         if response == 0:
            return (self.server_ip + " is Up and Running")
        # else the server is not running and is down
         else:
            return (self.server_ip + " is Down")
