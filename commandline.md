Introduction: Basic Linux Commands 

## cd:
 
### In simple Terms:
The cd command changes your current directory. In other words, it moves you to a new place in the filesystem.

## Some Detail:
If you are changing to a directory that is within your current directory, you can simply type cd and the name of the other directory.

cd work

If you are changing to a directory elsewhere within the filesystem directory tree, provide the path to the directory with a leading /.

cd /usr/local/bin

To quickly return to your home directory, use the ~ (tilde) character as the directory name.

cd ~

![cd ~](./images/cd.png)

## mkdir

### In simple Terms:

Definition: The mkdir command allows the user to create directories. This command can create multiple directories at once as well as set the permissions for the directories. It is important to note that the user executing this command must have enough permissions to create a directory in the parent directory, or he/she may recieve a ‘permission denied’ error.
  
### Some Detail:

**mkdir--version** It displays the version number, some information regarding the license and exits.  

**mkdir -v** It displays a message for every directory created.

**mkdir -help** It displays the help related information and exits.

**mkdir-m a=rwx [directory]** This option is used to set the file modes, i.e. permissions, etc. for the created directories. The syntax of the mode is the same as the chmod command.

## How to create directories using mkdir?

Creating directories is pretty simple, all you need to do is to pass the name of the directory you want to create to the mkdir command.

mkdir [directory]

Following is an example:

mkdir test 

![mkdir](./images/test.png)


## cp

### In simple Terms:

The `cp` command is a command-line utility for copying files and directories. It supports moving one or more files or folders with options for taking backups and preserving attributes.

To copy a file with the `cp` command pass the name of the file to be copied and then the destination. In the following example the file `food.txt` is copied to a new file called `bar.txt`. The cp command will also create the new file as part of the operation.

ls 
food.txt 
cp food.txt bar.txt
ls 
food.txt bar.txt

![cp](./images/cp.png)

Copy 2 files main.c and def.h to destination absolute path directory /home/usr/rapid/ 

cp main.c def. h /home/usr/rapid/

## pwd

### In simple Terms:

**pwd** stands for **P**rint **W**orking **D**irectory. It prints the path of the working directory, starting from the root.

![pwd](./images/pwd.png)

pwd is shell built-in command(pwd)

This command has two flgas. 

**pwd - L**  Prints the symbolic path.
**pwd - P** Prints the actual path. 

# Changelog

- [x] cd ~ Steven 
- [x] mkdir ~ Steven 
- [x] cp~Steven 
- [x]pwd
- [ ] mv
- [ ] rm
- [ ] history
- [ ] Home directory and ~
- [ ] file paths in linux
- [ ] Using the tab key to complete file paths
- [ ] Using up and down arrow for history

