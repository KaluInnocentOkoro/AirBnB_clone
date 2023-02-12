#!/usr/bin/python3
"""Command console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter to implement """

    prompt = '(hbnb) '

    # method to handle 'quit command
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    # Method to handle 'EOF' command
    def deo_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    # method to handle empty line input
    def emptyline(self) -> bool:
        """Do nothing on an empty line"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
