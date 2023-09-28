# Linux Commands, Processes and Permissions


## Commands

- `mv` can rename but it can also move
- `mv <file_name> <folder_name>` - To move a file into a folder
- `mv <file_name> ..` - Moves the file back up to the previous folder
- `mv <file_name_original> <file_name_new>` - Moves contents of file 1 to file 2

## Making a script

- `nano <shell_name.sh>`
- `#!/bin/bash` - Called a shabang. Tells the system that this is a script
- Add comments with # for each element of the script
- Put the script command below the comment
- Make sure the commands are in the correct sequence

## Processes

- `ps` - shows processes
- PID means process ID
- CMD is the command used to run the process
- `ps --help simple` - shows options for showing processes
- `ps aux` - shows all info about processes
- `top` - live readout of the processes going on
- shift + m - sorts by memory
- `sleep 5` - runs processes in the foreground
- `sleep 5000 &` - runs process in the background
- ctrl + c - ends process
- `kill -1 <PID>` - kills chosen process (hangup - less forceful)
- `kill -15 <PID>` - kills chosen process (terminated - forceful)
- `kill -9 <PID>` - kills chosen process (killed - super forceful) - Not recommended on databases or anything continually writing data
- `kill -KILL <PID>` - same as kill -9

## Permissions

### longhand

- `ls -l` - longhand list info - the first part of the line is the permissions
- e.g. drwxrwxr
- d - 
- rwx - owner can read, write and execute
- rwx - user can read, write and execute
- r-x - (group) anyone else can read and execute but not write
- `chmod u+x <file_name>` - changes file permission for user (if this doesn't work add sudo)
- Removing the letter executes this for everyone
- Change + to - so no one can execute

### shorthand

- `chmod 777 <file_name>` - gives all permissions for all users
- Use chmod calculator to work out shorthand numbers
- https://chmod-calculator.com/
- Read (+4), Write (+2), Execute (+1)

## Environment variables

- `printenv` - prints all environment variables
- Variables are shown in all caps with no spaces between variable, =, and content
- The OS is case sensitive
- Environment variables are available across the whole system as opposed to normal variables
- `export <variable>` - makes the variable environment variable

## Notes

- Within a folder, `.` and `..` show that the folder is a child folder when you do `ls -a`
- `system ctl enable` - configures the system to start the service at next reboot
- `sudo chmod +x <file_name>` - makes file executable
- `ls -l` - longhand list data