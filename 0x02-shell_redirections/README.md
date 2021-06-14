# 0x002 Shell, I/O Redirections and Filters

## Resources

- LinuxCommand.Org [I/O Redirection](http://linuxcommand.org/lc3_lts0070.php).
- BashGuide [SpecialCharacters](http://mywiki.wooledge.org/BashGuide/SpecialCharacters).

## Tasks

0. [Hello World](./0-hello_world) : A script that prints `Hello, World`, followed by a new line to the standard output.
1. [Confused smiley](./1-confused_smiley) : A script that displays a confused smiley: `"(Ôo)'`.
2. [Let's display a file](./2-hellofile) : A script that displays the content of the `/etc/passwd` file.
3. [What about 2?](./3-twofiles) : A scipt that displays content of `/etc/passwd` and `/etc/hosts`.
4. [Last lines of a file](./4-lastlines) : A script that displays the last 10 lines of `/etc/passwd`.
5. [I'd prefer the first ones actually](./5-firstlines) : A scipt that displays the first 10 lines of `etc/passwd`.
6. [Line #2](./6-third_line) : A script that displays the third line of the file `iacta`.
   - The file `iacta` will be in the working directory and you are not allowed to use `sed`.
7. [It is a good file that cuts iron without making a noise](./7-file) : A script that creates a file named exactly `\*\\'"Holberton School"\'\\*$\?\*\*\*\*\*:)` containing the text `Holberton School` ending by a new line.
   - For this challenge, remember to use a single backslash `\` to escape special characters and double backslash `\\` to escape the backslash itself.
