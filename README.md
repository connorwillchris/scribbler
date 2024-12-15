# Scribbler

Writing software for the terminal made in python.
Run it using `./scribbler.py` or
`python scribbler.py` on Windows. Very hackable and
moddable.

## Usage

Type a line number, followed by some text. The doc
will be written in the order of the line numbers.

### Commands

Commands are not-case sensitive.

- **Exit.** Exits the program.
- **List.** Lists the contents of the book in order of the line numbers.
- **Write.** Write the contents to a file.
- **Cls.** Clears the screen. (-Nix based systems only for the right now.)

# TODO

- [ ] Create a `HELP` command.
- [ ] API for creating your own commands.
- [ ] `READ` command for opening files and also
writing to them.
- [ ] System arguments for the application.
- [ ] Make any system specific changes such as the `CLS` command for Windows and Linux/MacOS.

## Bugs

- [X] Fixed bug where lists are sorted by string as opposed to integer.
- [X] Fix bug where you cannot update page numbers, only add them.
- [X] Fix bug where a new line produces an error message.

# License stuff

Licensed under `CC-BY-SA 4.0` but essentially, just
say you're using my software if you use it in any
software development projects. No credit required,
but always encourage if you are using it to write a
book or something!
