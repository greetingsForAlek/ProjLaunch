# ProjLaunch for Mac/VSCode

ProjLaunch is a terminal tool for mac and vscode that saves and opens projects when you run a command.

## How it works

This is a guide for how to install and use the software.

### Installment

To install, run the provided install script, (in the scripts folder) and then you need to add a line at the bottom of your .zshrc file (usually located in your home directory.)

This is the line you need to add: ```export PATH="$HOME/scripts:$PATH"```. this allows the terminal to get our command from the scripts folder. Don't worry if you do not have a scripts folder, the install script creates one.

*Important:* to run the install script, I recommend: In your terminal move to the directory where the scripts folder is. Then, run ```bash scripts/install.sh```.

### How to add your project

To add a project, once you've installed the software, run ```proj add```.
This will bring up a pop-up that lets you add a project. You can put a name, a path to a directory, any commands you want to run upon opening and also any websites you want opened upon opening.

### How to open the project

Now, This project works with VSCode, so it will open vscode if you have that installed. If there is a command to open your editor of choice, I recommend that you edit the code, there you will find a ```subprocess.Popen``` that has ```"code"``` inside it. If there is a command to open your editor of choice, replace the string ```"code"``` with a string with the command for your editor of choice.

With that out of the way, run ```proj launch your_project_name``` to launch the project. Make sure to replace ```your_project_name``` with the actual name of your project.