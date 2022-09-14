# Git Cheatsheet

Just my own git commands reference for personal use.  


## Branch stuff

### Change file in multiple branches

```sh
$ git log  # get commit SHA
$ git checkout <branch>
$ git cherry-pick COMMIT_SHA
```
[Source](https://stackoverflow.com/questions/20555694/what-is-the-best-way-to-make-the-same-change-to-multiple-branches)

### Compare file in multiple branches

```sh
$ git diff <b1> <b2> -- myfile.pog
```
[Source](https://stackoverflow.com/questions/4099742/how-to-compare-files-from-two-different-branches)

### Delete local branch

```
git branch -D <branch>
```

### Update deletion of local branch on remote

```
git push <remote-name> :<branch>
```
