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
8. [Save current state of directory](./8-cwd_state) : A script that writes into the file `ls_cwd_content` the result of the command `ls -la`. If the file `ls_cwd_content` already exists, it should be overwritten. If the file `ls_cwd_content`does not exist, create it.
9. [Duplicate last line](./9-duplicate_last_line) : A script that duplicates the last line of the file `iacta`.
10. [No more javascript](./10-no_more_js) : A script that deletes all the regular files (not the directories) with a `.js` extension that are present in the current directory and all its subfolders.
11. [Don't just count your directories, make your directories count](./11-directories) : A script that counts the number of directories and sub-directories in the current directory.
   - The current and present directories should not be taken into account.
   - Hidden directories should be counted.
     - **Solution:** `mindepth 1` ; To exclude root directory
     - **Others:** `maxdepth 1` ; To avoid parsing sub directories. (*you may need this in future.*)
12. [Whats12's new](./12-newest_files) : A script that prints the 10 newest files in the current directory.
   - The output should be; one file per line and sorted from the newest to the oldest.
13. [13. Being unique is better than being perfect](./13-unique) : A script that takes a list of words as input and prints only words that appear exactly once.
   - Input and Output format is; `One word per line`.
   - Words should be sorted.
