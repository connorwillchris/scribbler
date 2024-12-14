# Scribbler

Writing software for the terminal made in python. Run it using `./scribbler.py` or `python scribbler.py` on Windows. Very hackable and moddable.

## Usage

Type a line number, followed by some text. The novel will be written in the order of the line numbers.

### Commands

Commands are not-case sensitive.

- **Exit.** Exits the program.
- **List.** Lists the contents of the book in order of the line numbers.
- **Write.** Write the contents to a file.
- **Cls.** Clears the screen. (-nix based systems only for the right now.)

# TODO

- [] Create a `HELP` command.
- [] API for creating your own commands.
- [] `READ` command for opening files and also writing to them.
- [] System arguments for the application.

## Bugs

- [X] Fixed bug where lists are sorted by string as opposed to integer.
- [X] Fix bug where you cannot update page numbers, only add them.
