#!/usr/bin/python3

import cmd
import sys

class HBNBCommand(cmd.Cmd):
    """
    command line shell interepreter
    """

    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_EOF(self, line):
        '''
exits the shell
        '''
        return True

    def do_quit(self, line):
        '''
Quit command to exit the program
        '''
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
