#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    ''' Entry for HBNBCommand Console

        Attributes:
        prompt: overwrite default prompt with custom prompt
    '''

    prompt = '(hbnb) '

    class_list = ["BaseModel"]

    def do_create(self, arg):
        ''' creates a new instance of BaseModel, saves it to a JSON and prints the ID
        '''
        from models.base_model import BaseModel
        from models import storage

        if len(arg) == 0:
            print('** class name missing **')
        else:
            try:
                new_ins = eval("{}()".format(arg))
                storage.new(new_ins)
                storage.save()
                print(new_ins.id)
            except:
                print("** class doesn't exist **")

    def do_show(self, arg):
        ''' Prints the string representation of an instance based on the
            class name and id
        '''
        from models import storage
        from shlex import split

        token = arg.split()

        if len(token) == 0:
            print("** class name missing **")
        elif token[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(token) == 1:
            print("** instance id missing **")
        else:
            try:
                name_id = "{}.{}".format(token[0], token[1])
                print(storage.all()[name_id])
            except:
                print("** no instance found **")

    def do_destroy(self, arg):
        from models import storage
        from shlex import split

        token = arg.split()

        if len(token) == 0:
            print("** class name missing **")
        elif token[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(token) == 1:
            print("** instance id missing **")
        else:
            try:
                name_id = "{}.{}".format(token[0], token[1])
                del(storage.all()[name_id])
                storage.save()
            except:
                print("** no instance found **")

    def do_all(self, arg):
        from models import storage
        from shlex import split

        token = arg.split()

        obj_list = []
        if len(arg) == 0 or token[0] in self.class_list:
            for key, val in storage.all().items():
                if arg in key:
                    obj_list.append(storage.all()[key].__str__())
            print(obj_list)

        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        ''' Updates an instance based on the class name and ID by adding or updating
            attribute
        '''
        from shlex import split
        from models import storage

        token = arg.split()

        if len(token) == 0:
            print("** class name missing **")
        elif token[0] not in self.class_list:
            print("** class doesn't exist **")
        elif len(token) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(token[0], token[1]) not in storage.all().keys():
            print("** no instance found **")
        elif len(token) == 2:
            print("** attribute name missing **")
        elif len(token) == 3:
            print("** value missing **")
        else:

            attr_type = type(eval(token[3]))
            setattr(storage.all()["{}.{}".format(token[0], token[1])],
                    token[2],
                    attr_type(token[3].strip('\'"')))
            storage.all()["{}.{}".format(token[0], token[1])].save()

    def do_EOF(self, arg):
        ''' EOF argument that exits out of the console
        '''
        return True

    def do_quit(self, arg):
        ''' quit command that quits out of the console
        '''
        return True

    def emptyline(self):
        ''' overwrites emptyline method to not execute previous command
        '''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
