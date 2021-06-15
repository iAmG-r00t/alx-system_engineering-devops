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
13. [Being unique is better than being perfect](./13-unique) : A script that takes a list of words as input and prints only words that appear exactly once.
    - Input and Output format is; `One word per line`.
    - Words should be sorted. (use this [list](./list) as your input to see if the challenge will work. 😊) `cat list | ./13-unique`
14. [It must be in that file](./14-findthatword) : A script that prints lines containing the pattern `"root"` from the file `/etc/passwd`.
15. [Count that word](./15-countthatword) : A script that displays the number of lines that contain the pattern `"bin"` in the file `/etc/passwd`.
16. [What's next?](./16-whatsnext) : A script that containing the pattern `"root"` and 3 lines after them in the file `/etc/passwd`.
    - `B` : This shows the lines before your pattern match.
    - `A` : This shows the lines after your pattern match.
17. [I hate bins](./17-hidethisword) : A script that displays all the lines in the file `/etc/passwd` that do not contain the pattern `"bin"`.
18. [Letters only please](./18-letteronly) : A script that displays all lines of the file `/ect/ssh/sshd_config` starting with a letter, including capital letters as well.
    - This also works : `grep ^[[:alpha:]] /etc/ssh/sshd_config`
19. [A to Z](./19-AZ) : A script that replaces all characters `A` and `C` from input to `Z` and `E` respectively.
20. [Without C, you would live in hiago](./20-hiago) : A script that removes all letters `c` and `C` from input.
21. [esreveR](./21-reverse) : A script that reverse its input.
22. [DJ Cut Killer](./22-users_and_homes) : A scipt that displays all users and their home directories, sorted by users, based on the `/etc/passwd` file.
23. [Empty casks make the most noise](./100-empty_casks) : A script that finds all empty files and directories in the current directory and all sub-directories.
    - Only names of the files and directories should be displayed (not the entire path.)
    - Hidden files should be listed also, one file name per line and the listing should end with a new line.
    - You are not allowed to use `basename`, `grep`, `egrep`, `fgrep` or `rgrep`.
24. [A gif is worth ten thousand words](./101-gifs) : A script that lists all the files with a `.gif` extension in the current directory and all its sub-directories.
    - Hidden files should be listed.
    - Only regular files (not directories) should be listed.  
    - The names of the files should be displayed without their extensions. 
    - The files should be sorted by byte values, but case-insensitive (file `aaa` should be listed before file `bbb`, file `.b` should be listed before file `a`, and file `Rona` should be listed after file `jay`) 
    - One file name per line. 
    - The listing should end with a new line. 
    - You are not allowed to use `basename`, `grep`, `egrep`, `fgrep` or `rgrep`. 
25. [Acrostic](./102-acrostic) : A script that decodes acrostics that use the first letter of each line.
    - What to decode: `An acrostic is a poem (or other form of writing) in which the first letter (or syllable, or word) of each line (or paragraph, or other recurring feature in the text) spells out a word, message or the alphabet. The word comes from the French acrostiche from post-classical Latin acrostichis). As a form of constrained writing, an acrostic can be used as a mnemonic device to aid memory retrieval.` [Read more here](https://en.wikipedia.org/wiki/Acrostic)
    - The **‘decoded’** message has to end with a new line.
    - You are not allowed to use `grep`, `egrep`, `fgrep` or `rgrep`.
26. [The biggest fan](./103-the_biggest_fan) : A script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.
    - Download this file: `wget http://indeedeng.github.io/imhotep/files/nasa_19950801.tsv`
    - Run command this way: `./103-the_biggest_fan < nasa_19950801.tsv`.
    - Order by number of requests, most active host or IP at the top.
    - You are not allowed to use `grep`, `egrep`, `fgrep` or `rgrep`.
