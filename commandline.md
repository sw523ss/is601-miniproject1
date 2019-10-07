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

