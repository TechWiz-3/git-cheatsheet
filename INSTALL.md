# Installation

## Binary Installation
For those without Python installed, you can use a binary from the [GitHub Actions](https://github.com/TechWiz-3/git-cheatsheet/actions) tab.
1. Click the latest workflow, then scroll to the bottom for the heading 'Artifacts'.
2. Download the right one for your platform.
3. Unzip/extract the file
4. Now clone the repo `git clone https://github.com/TechWiz-3/git-cheatsheet.git`
5. Move the extracted binary into the git repo (ensure it is named `gcheat_binary`)
6. Now run `cd git-cheasheet && sudo bash install-binary`
7. Cd out of the git repo and use the command `gcheat`
8. If an issue occurs, please report it :pray:
9. Enjoy!

### On Windows with no access to Bash
**Logic:**
Basically since you can't do step 6, you will need to ensure that whenever `gcheat_binary.exe` is invoked, the path to the repo's `README.md` is the last arguement.  
That might look something like this So `gcheat_binary.exe git-cheatsheet/README.md`  
Preferably, the `gcheat_binary` can be accessed from anywhere, and the `README.md` argument is passed in automatically.  

A smart way to do it would be, (after moving the binary to the git cloned repo), adding the repo to the command prompt/terminal's path and then aliasing gcheat to `\path\gcheat_binary.exe \path\README.md`.  

## Python Installation
```sh
git clone https://github.com/TechWiz-3/git-cheatsheet && cd git-cheatsheet
pip install -r requirements.txt
bash install
```

```
gcheat
```

