# Git Cheatsheet

Just my own git commands reference for personal use.  

Install the CLI tool (with or without Python) [here](./INSTALL.md). Seriously, do it! It's super useful.

## Branch stuff

### Change file in multiple branches

```sh
git log  # get commit SHA
git checkout <branch>
git cherry-pick COMMIT_SHA
```
[Source](https://stackoverflow.com/questions/20555694/what-is-the-best-way-to-make-the-same-change-to-multiple-branches)

### Compare file in multiple branches

```sh
git diff <b> <b> -- myfile.pog
```
[Source](https://stackoverflow.com/questions/4099742/how-to-compare-files-from-two-different-branches)

### Delete local branch

```sh
git branch -D <branch>
```

### Update deletion of local branch on remote

```sh
git push <remote-name> :<branch>
```

### Rename branch

```sh
# local branch
git branch -m <new-name>
# other branch
git branch -m <old-nane> <new-name>

# to update/delete on remote
git push <remote-name> :<old-name>
# delete the old upstream as it hasn't been updated with new name
git branch --unset-upstream <new-name>
# push renamed branch to remote
git push <remote-name> <new-name>
# set the correct upstream for the newly pushed local branch
git push <remote-name> -u <new_name>
# response will look something like this
# "Branch 'new_branch_name' set up to track remote branch 'new_branch_name' from 'origin'."
```
[Source](https://stackoverflow.com/questions/30590083/how-do-i-rename-both-a-git-local-and-remote-branch-name)

### Checkout branch on remote locally

```sh
git pull
# you should see something like this:
" * [test branch]      test_branch -> origin/test_branch"
git checkout <branch-name>
```

## Terminology

### Origin/`<remote-name>`

```
In Git, "origin" is a shorthand name for the remote repository that a project was originally cloned from.
More precisely, it is used instead of that original repository's URL - and thereby makes referencing much easier.
Note that origin is by no means a "magical" name, but just a standard convention.
```
[Source](https://www.git-tower.com/learn/git/glossary/origin)
