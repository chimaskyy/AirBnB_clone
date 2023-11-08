#!/usr/bin/python3

import cmd
import sys
from models import storage
from models.base_model import  BaseModel

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

    def do_create(self, line):
        '''
 Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        '''

        if not line:
            print("** class name missing **")
            return
        '''retrieve class name as key'''
        class_objects = storage.Classes()
        if line in class_objects:
            '''retrieve class object'''
            class_obj = class_objects[line]
            '''create instance'''
            obj = class_obj()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

        '''if line not in storage.Classes():
            print("** class doesn't exist **")
            return
        obj = storage.Classes()[line]()
        obj.save()
        print(obj.id)'''

    def do_show(self, line):
        '''
Prints the string representation of an instance based on the class name and id
        '''
        if not line:
            print("** class name missing **")
            return
        else:
            lines = line.split(' ')
            class_name = lines[0]
            if class_name not in storage.Classes():
                print("** class doesn't exist **")
                return
            elif len(lines) < 2:
                print("** instance id missing **")
                return
            else:
                id_ = lines[1]
        
                key = "{}.{}".format(class_name, id_)
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    obj = storage.all()[key]
                    obj = storage.Classes()[class_name](**obj)
                    print(obj)




if __name__ == '__main__':
    HBNBCommand().cmdloop()
