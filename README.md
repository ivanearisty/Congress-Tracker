# Congress-Tracker

## Group Guidance

Please don't commit push things to main that are dependent on your machine.

Create virutal environments for python and ignore your specific installations for node.

### Github

Github is a version control manager.

There are remote and local branches.

THe remote branches are branches kept in github servers.

THe local branches are branches kept in our computers.

You perform work in a local branch and then add, commit, and push your changes to a remote branch.

There can be more than one branch, for example, you can have a main, remote branch and other remote branches for each project member.

When you are done finishing some stuff: 
- push your changes to your remote branch
- copy the changes from the latest changes in the maain remote branch to your own remote branch
- make sure things work
- merge back into the remote branch so that everyone has your new changes

Download the cli tool lazygit if you want to make things easier for your.

### Backend Installation

- Install virtualenv or make a new python virtual environment inside the Backend folder
```zsh
➜  Backend git:(main) ✗ virtualenv .venv    
created virtual environment CPython3.13.0.final.0-64 in 377ms
  creator CPython3macOsBrew(dest=/Users/suape/WorkDir/CongressTracker/Backend/.venv, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, via=copy, app_data_dir=/Users/suape/Library/Application Support/virtualenv)
    added seed packages: pip==24.2
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
➜  Backend git:(main) ✗ source .venv/bin/activate
(.venv) ➜  Backend git:(main) ✗ 
```
- Install requirements.txt
- Installing something new? add to requirements: `pip freeze > requirements.txt`

### Frontend Installation