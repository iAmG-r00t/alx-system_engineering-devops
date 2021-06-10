# 0x01 Shell Permissions

## Resources

- LinuxCommand.org [Permissions](http://linuxcommand.org/lc3_lts0090.php).

## Tasks

0. [My name is Betty](./0-iam_betty) : A script that switches the current user to the user betty.
1. [Who am I](./1-who_am_i) : A script that prints the effective username of the current user.
2. [Groups](./2-groups) : A script that prints all the groups the current user is part of.
3. [New owner](./3-new_owner) : A script that changes the owner of the file `hello` to the user `betty`.
4. [Empty!](./4-empty) : A script that creates an empty file called `hello`.
5. [Execute](./5-execute) : A script that adds execute permission to the owner of the file `hello`.
6. [Multiple permissions](./6-multiple_permissions) : A script that adds execute permission to the owner and the group owner, and read permission to the other users, to the file `hello`.
7. [Everybody!](./7-everybody) : A script that adds execution permissions to the owner, the group owner and the other users, to the file `hello`.
8. [James Bond](./8-James_Bond) : A script that gives the gives the rest of the users permission and removes all permission for the owner and the group owner.
9. [John Doe](./9-John_Doe) : A script that sets the mode of the file `hello`; where owner has all the permissions set, group owner has execute permissions set and others have only write and read permissions set.
10. [Look in the mirror](./10-mirror_permissions) : A script that sets the mode of the file `hello` the same as `olleh`'s mode.
11. [Directories](./11-directories_permissions) : A script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. (**NB:** *Regular files should not be changed.*)
12. [More directories](./12-directory_permissions) : A script that creates a directory called `dir_holberton` with permissions **751** in the working directory.
13. [Change group](./13-change_group) : A script that changes the group owner to `holberton` for the file `hello`.
14. [Owner and group](./100-change_owner_and_group) : A script that changes the owner to `betty` and the group owner to `holberton` for all the files and directories in the working directory.
15. [Symbolic links](./101-symbolic_link_permissions) : A script that changes the owner and the group owner of `_hello` to `betty` and `holberton` respectively.
16. [If only](./102-if_only) : A script that changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume`.
17. [Star Wars](./103-Star_Wars) : A script that will play the StarWars IV episode in the terminal.
