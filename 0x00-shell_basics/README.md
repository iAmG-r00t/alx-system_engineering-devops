# 0x00 Shell Basics

## Resources

- LinuxCommand.org [What is "the Shell"?](http://linuxcommand.org/lc3_lts0010.php).
- [Read the Manual](http://linuxcommand.org/lc3_man_pages/man1.html).
- [Keyboard Shortcuts for Bash](https://www.howtogeek.com/howto/ubuntu/keyboard-shortcuts-for-bash-command-shell-for-ubuntu-debian-suse-redhat-linux-etc/).

## Tasks

0. [Where am I?](./0-current_working_directory) : A script that prints the absolute path of the current working directory.
1. [What's in there?](./1-listit) : A script that displays the contents of your current directory.
2. [There is no place like home](./2-bring_me_home) : A script that changes the working directory to the user's home directory.
3. [The long format](./3-listfiles) : A script that displays the current directory contents in a long format.
4. [Hidden files](./4-listmorefiles) : A script that displays the current directory contents including hidden files.
5. [I loce numbers](./5-listfilesdigitonly) : A script that displays the current directory contents, using long format, while displaying group IDs in numeral and show hidden files.
6. [Welcome holberton](./6-firstdirectory) : A script that will create a directory named `holberton` in the `/tmp/` directory.
7. [Betty in Holberton](./7-movethatfile) : A scipt that will move a file called `betty` from home to the new directory created above.
8. [Bye bye Betty](./8-firstdelete) : A script that will delete file `betty` from the new location.
9. [Bye bye Holberton](./9-firstdirdeletion) : A script that will delete the directory `holberton` that is in the `/tmp/` directory path.
10. [Back to the future](./10-back) Change working directory to the previous one.
11. [Lists](./11-lists) List all files (*even ones with names beginning with a period character, which are normally hidden*) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
12. [File type](./12-file_type) A script that prints the type of the named file `iamafile`. The `iamafile` will be in the `/tmp/` directory when we will run your script.
13. [We are symbols, and inhabit symbols](./13-symbolic_link) Create a symbolic link to `/bin/ls`, named `__ls__`. The symbolic link should be created in the current working directory.
14. [Copy HTML files](./14-copy_html) Create a script that copies all `html` files from the current working directory to the parent working directory while only copying files that did not exist.
15. [Let's move](./100-lets_move) A script that moves all files beginning with an uppercase letter to the directory `/tmp/u`.
16. [Clean Emacs](./101-clean_emacs) A script that deletes all files in the current directory that end with the character `~`.
17. [Tree](./102-tree) A script that creates the directory `welcome/`, `welcome/to/` and `welcome/to/holberton`.
18. [Life is a series of commas, not periods](./103-commas) A script that lists all the files and directories of the current directory separated by commas `,`.
19. [File type: Holberton](./holberton.mgc) Create a magic file `holberton.mgc` that can be used with the command `file` to detect `Holberton` data files always contain the string `HOLBERTON` at offset 0.
