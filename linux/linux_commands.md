# Linux Commands

### Popular commands

- `ls` - Lists directories
- `ls -a` - Lists all directories (inc. hidden)
- `ls ..` - Lists files in directory above
- `cd` - Moves to home directory
- `cd <folder_name>` - Moves to folder within directory
- `cd ..` - Moves back one directory
- `clear` - Moves command line to top of screen to clear the page (but doesn't remove previous commands)

### Information

- `whoami` - Returns active username
- `uname` - Gets basic info about the OS
- `cat /etc/shells` - Shows available shells
- `history` - Shows command history
- `history -c` - Resets history
- `file <file_name>` - Shows info about the file


### File content

- `cat <file_name>` - Displays file content

### Making files

- `mkdir <directory_name>` - Makes directory
- `mv <file_name>` - Move or rename files
- `touch <file_name>` - Create blank/empty files
- `nano <file_name>` - Gives option to add text to file being created using text editor

### Removing items

- `rm <file_name>` - Removes chosen file
- `rm -i` - Interactive removal (you get asked to confirm)
- `rm -r` - Removes directory
- `rm -rf` - Forced removal of directory

### Interacting with files

- `mv <file_name_current> <file_name_new>` - Renames files and extensions but doesn't change content
- `curl <file_name>` - Used to transfer data
- `cp <file_name_to_be_copied> <file_name_copy>` - Copies chosen file and gives new name to new file
- `nl <filename>` - Numbers lines of text within file
- `grep`- Global Regular Expression Print - highlights a chosen word within the text

### Getting packages from linux

- `apt <package_name>` - Downloads chosen package (may require sudo command first)

### Superuser

- `sudo` - Gives superuser permissions for one command
- `sudo su` - Gives permanent superuser permissions
- `exit` - Exits superuser permissions

### Heads and Tails

- `head -<number>` e.g. `head -2` - Returns chosen number of lines from top of file
- `tails -<number>` e.g. `tails -2`- Returns chosen number of lines from bottom of file

