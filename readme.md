## Prerequisites

### Required

- [Vscode installation](https://code.visualstudio.com/)
- [Docker desktop installation](https://www.docker.com/products/docker-desktop/)

### Highly Recommended

- [Github account](https://github.com/)

## Code of Conduct

### Work in branches

To work on a branch, follow these steps:

Assuming you are on the main branch, use the following commands to create a new branch:

```bash
git pull
git checkout -b <branchname>
```

### Commit Well, Commit Often

Commits should be made frequently to make reviewing code history easier. Git commits allow for easier debugging and tracking of changes. To commit:
```bash
git add <change> # . for all changes
git commit -m <descriptive title for code change>
```
*descriptive title should be short and concise*

### Add Code via Pull Requests

When the code is ready for deployment, push the code to the origin with:
```bash
git push origin <branch name> # Specifying branch name is often not needed 
```
Go to the GitHub repository and create a pull request. This can be done by navigating to the repository on GitHub, clicking the "Pull Requests" tab, and clicking the "New pull request" button. After merging, switch to the main branch pull changes, delete the working branch, and create a new branch for further development.
```bash
git checkout main
git pull
git branch -d <branch> # branch to delete
git checkout -b <branch> # new branch to create
```

## Suggested workflow

1.  Start dockerdesktop
2.  Start workspace in vscode
    ```bash
    code <path> # path to workspace
    ```
3.  Reopen in container 
4.  Pull lastest changes and rebranch
    ```bash
    git checkout main
    git pull
    git checkout -b <branch> # new branch to create
    ```
5. Work on your branch
6. Document and exert version control
    ```bash
    git add <change> # . for all changes
    git commit -m <descriptive title for code change>
    ```
    *repeat until brach is solved, or you want to merge into main*
7. Push to main
    ```bash
    git push origin <branch> # Specifying branch is often not needed 
    ```
15. Go to https://github.com/[YOURPROJECT] and merge the pushed content.
16. Pull lastest changes and rebranch
    ```bash
    git checkout main
    git pull
    git branch -d <branch> # branch to delete
    git checkout -b <branch> # new branch to create
    ```
20. Go to step 6.

## Python

### Intendened usage
It is recommened to only use run (control + alt + n) for executeing code.
Interacting line by line should only be done in the debugger

### Packages
Packages are handled in requirements.txt. requirements.txt should include all packages in the project and their version. We can run
```bash
pip3 freeze > src/requirements.txt
```
to update the requirements.txt with the packages used in the project. 

On rebuild src/requirements.txt is downloaded to the pythons virtual enviourment
```bash
bash -c "python3 -m venv venv &&
     source venv/bin/activate &&
     pip install -r src/requirements.txt
```
*defined in docker-compose*

## Vscode settings
It is recommended that you syncronize your personal vscode settings. See how in the vscode [offical docs](https://code.visualstudio.com/docs/editor/settings-sync)

## Suggest notations
1. Use lowercase
2. Use _ as space
3. Use double quotes
4. Document used abbreviations

## Debugging
Debugging in VSCode (Python, TypeScript, and JavaScript)
### Python
1. Set breakpoints: Place breakpoints in your Python code by clicking in the left margin of the editor window next to the line of code where you want to pause the debugger.

2. Launch the debugger: Press F5 or go to the Run and Debug view by clicking the Run and Debug icon in the Activity Bar, select "Python" as the debugging environment in the dropdown menu, and click the green play button to launch the debugger.

3. Debug your Python code: Once the debugger is launched, VSCode will stop at the breakpoints you set. You can then use the debugging toolbar to step through your code, inspect variables, and watch expressions to identify and fix any issues in your Python code.

## Registered abbreviations

- [Approved abbreviations](https://github.com/abbrcode/abbreviations-in-code)
- ADD YOUR DOMAIN SPECIFIC ABBREVIATIONS

## Cool trics

open project from terminal
```bash
widows + r, cmd, enter
code c:/env
```

open commandline
```bash
control + p
```
acces commands
```bash
control + p INSERT >
```

navigate objects
```bash
control + shift + .
```
Multiple textline editingg
```bash
alt + click
```
Multiple word highligt and editing
```bash
control + d
```
highlight line
```bash
control + l
```
comment out highlighted section
```bash
control + /
```

[MIT-License](LICENSE)