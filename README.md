# veno
```
                 ▓               
                 ▓▓              
 ▓▓▓  ▓▓ ▓▓▓▓▓▓▓ ▓▓▓  ▓▓  ▓▓▓▓▓ 
 ▓▓▓  ▓▓ ▓▓      ▓▓▓▓ ▓▓ ▓▓   ▓▓
  ▓▓  ▓▓ ▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓ ▓▓   ▓▓
  ▓▓ ▓▓  ▓▓      ▓▓▓ ▓▓▓ ▓▓   ▓▓
   ▓▓▓   ▓▓▓▓▓▓▓ ▓▓▓  ▓▓  ▓▓▓▓▓ 
                       ▓         
```
Multi-purpose text/code editor meant for easy and vast expandability.

## Install

Uses external libraries. Requires Python3.
Prerequisites: Pygments, Curses. Install these for Python3 if not currently on system.

Run `pip3 install -r requirements.txt` in `veno` directory to install prerequisites.

## Usage

To run, execute `python3 veno [filename]` Filename optional. 

Runs in a terminal window. GUI not yet implemented.

## Keybindings

 - **Ctrl-C** -- cancel/quit
 - **Arrow Keys** -- move cursor in file
 - **PageUp, PageDown** -- scroll screen up/down
 - **Ctrl-Arrow Keys** -- move viewport in file
 - **Ctrl-W** -- save file
 - **Home Key** -- go to start of line in file
 - **End Key** -- go to end of line in file
 - **F3** -- go to start of file
 - **F4** -- go to end of file
 - **Ctrl-F** -- find regex string in file
 - **Ctrl-G** -- find next match in file
 - **Ctrl-H** -- find and replace all
 - **Ctrl-B** -- select text
 - **Ctrl-K** -- copy selection
 - **Ctrl-X** -- cut selection
 - **Ctrl-V** -- paste selection
