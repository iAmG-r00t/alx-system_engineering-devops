# 0x03 Shell, init files, variables and expansions

## Resources

- Shell [Expansion](http://linuxcommand.org/lc3_lts0080.php).
- Shell [Arithmetic](https://www.gnu.org/software/bash/manual/html_node/Shell-Arithmetic.html).
- Bash [Variable](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_02.html).
- Bash [Shell initialization files](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_01.html).
- [The alias Command](http://www.linfo.org/alias.html).

## Tasks

0. [<o>](./0-alias) : A script that creates an alias.
   - Name of alias: `ls`
   - Value: `rm *` 
1. [Hello you](./1-hello_you) : A script that prints `hello user`, where user is the current Linux user.
2. [The path to success is to take massive, determined action](./2-path) : A script that adds `/action` to the `PATH`. `/action` should be the last directory the shell looks into when looking for a program.
3. [If the path be beautiful, let us not ask where it leads](./3-paths) : A script that counts the number of directories in the `PATH`.
4. [Global variables](./4-global_variables) : A script that prints all the enviroment variables.
5. [Local variables ](./5-local_variables) : A script that lists all local variables and enviroment variables, and functions.
   - Name of variable : `HOLBERTON`
   - Value : `Betty`
6. [Local variable](./6-create_local_variable) : A script that creates a new local variable.
7. [Global variable](./7-create_global_variable) : A script that creates a new global variable.
   - Name of variable : `HOLBERTON`
   - Value : `Betty`
8. [Every addition to true knowledge is an addition to human power](./8-true_knowledge) : A script that prints the results of the addition of 128 with the value stored in the enviroment variable `TRUEKNOWLEDGE`, followed by a new line.
   - Remember to export variable TRUEKNOWLEDGE : `export TRUEKNOWLEDGE=1209`
   - Run command this way: `./8-true_knowledge | cat -e`
9. [Divide and rule](./9-divide_and_rule) : A script that prints the result of `POWER` divide by `DIVIDE`, followed by a new line.
   - `POWER` and `DIVIDE` are environment variables.
   - Variables values;
    - export POWER=42784
    - export DIVIDE=32
   - Run command this way: `./9-divide_and_rule | cat -e`
10. [Love is anterior to life, posterior to death, initial of creation, and the exponent of breath](./10-love_exponent_breath) : A script that displays the result of `BREATH` to the power of `LOVE`.
   - `BREATH` and `LOVE` are enviroment variables.
   - The script should display the result, followed by a new line.
11. [There are 10 types of people in the world -- Those who understand binary, and those who don't](./11-binary_to_decimal) : A script that converts a number from base 2 to base 10.
   - The number in base 2 is stored in the enviroment variable `BINARY`.
   - The script should display the number in base 10, followed by a new line.
12. [Combination](./12-combinations) : A script that prints all possible combinations of two letters, except `oo`.
   - Letters are lower cases, from `a` to `z`.
   - One combination per line.
   - The output should be alpha ordered, starting with `aa`.
   - Do not print `oo`.
   - Your script file should contain maximum 64 characters.
