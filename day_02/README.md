### Day 2: Advanced Git Workflow, and Distiributed Version Control
Today, on my day 2 of the sprint, i continued to dive deeper into git and github, checking edge cases of everything along the way, learning every command needed.  
Learnt deeply about Merging of Branches, Merge conflicts, their resolution, merge commit and other intricate concepts.  
Learnt how to switch between commits, comapre comitts.  
Got to know what are the differences between Pushing and Fetching, their uses, and the command of Push, Push and Fetch, with checking edge cases manually
Understood git restore vs git reset deeply.  
Got practical experience with stashing in git, also understanding the differnce between git pop and git apply.  
Understood the command git revert.  
Internalized the Working of git rebase deeply.  
Finally completed the Git and Github Fundamentals by learning about Pull Request (PR)  

### Terminal Practice & CLI Execution  

<details>
  <summary><b> Click here to view my raw, unedited terminal history grind</b></summary>  
  
 I practiced navigating the system architecture and initializing the Git pipeline directly from the command line, i got hands on practice with every command i learnt and executed hundreds of command to build muscle memory for directory navigation and repository initialization.
```bash
satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop
$ cd git journey
bash: cd: too many arguments

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop
$ cd my-first-repo

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ ls
README.md  one.txt  two.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ ls -a
./  ../  .git/  README.md  one.txt  two.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   one.txt

no changes added to commit (use "git add" and/or "git commit -a")

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   one.txt
        modified:   two.txt

no changes added to commit (use "git add" and/or "git commit -a")

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$  mkdir myFolder

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ cd myFolder

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo/myFolder (main)
$ touch 3.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo/myFolder (main)
$ explore .
bash: explore: command not found

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo/myFolder (main)
$ explorer .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo/myFolder (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   ../one.txt
        modified:   ../two.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        ./

no changes added to commit (use "git add" and/or "git commit -a")

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo/myFolder (main)
$ cd ..

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   one.txt
        modified:   two.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        myFolder/

no changes added to commit (use "git add" and/or "git commit -a")

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git add --all

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   myFolder/3.txt
        modified:   one.txt
        modified:   two.txt


satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git reset
Unstaged changes after reset:
M       one.txt
M       two.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git states
git: 'states' is not a git command. See 'git --help'.

The most similar command is
        status

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   one.txt
        modified:   two.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        myFolder/

no changes added to commit (use "git add" and/or "git commit -a")

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git add -A

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   myFolder/3.txt
        modified:   one.txt
        modified:   two.txt


satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git reset
Unstaged changes after reset:
M       one.txt
M       two.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   one.txt
        modified:   two.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        myFolder/

no changes added to commit (use "git add" and/or "git commit -a")

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git add .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git reset
Unstaged changes after reset:
M       one.txt
M       two.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ cd myFolder

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo/myFolder (main)
$ git add .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo/myFolder (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   3.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   ../one.txt
        modified:   ../two.txt


satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo/myFolder (main)
$ git reset
Unstaged changes after reset:
M       one.txt
M       two.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo/myFolder (main)
$ cd ..

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git add --all

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   myFolder/3.txt
        modified:   one.txt
        modified:   two.txt

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    two.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        four.txt


satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git add *

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   four.txt
        new file:   myFolder/3.txt
        modified:   one.txt
        modified:   two.txt

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    two.txt


satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git reset
Unstaged changes after reset:
M       one.txt
D       two.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   one.txt
        deleted:    two.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        four.txt
        myFolder/

no changes added to commit (use "git add" and/or "git commit -a")

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git add 1.txt
fatal: pathspec '1.txt' did not match any files

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git add one.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   one.txt

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    two.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        four.txt
        myFolder/


satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git add myFolder/three.txt
fatal: pathspec 'myFolder/three.txt' did not match any files

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ explorer .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git add myFolder/3.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   myFolder/3.txt
        modified:   one.txt

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    two.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        four.txt


satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git add *.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   four.txt
        new file:   myFolder/3.txt
        modified:   one.txt

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    two.txt


satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$  git add .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   four.txt
        new file:   myFolder/3.txt
        modified:   one.txt
        deleted:    two.txt


satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git commit -m "i have made changes"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'satti@DESKTOP-JHB7J8S.(none)')

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git config --local user.email "sattire729@gmail.com"

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git config --local user.name "Sattire"

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git commit -m "i have made some changes to the file"
[main 1d41e47] i have made some changes to the file
 4 files changed, 3 insertions(+), 1 deletion(-)
 create mode 100644 four.txt
 create mode 100644 myFolder/3.txt
 delete mode 100644 two.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git reset HEAD~
Unstaged changes after reset:
M       one.txt
D       two.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   one.txt
        deleted:    two.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        four.txt
        myFolder/

no changes added to commit (use "git add" and/or "git commit -a")

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git add .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git commit -m "i have made some changes to the File"
[main afbaccb] i have made some changes to the File
 4 files changed, 3 insertions(+), 1 deletion(-)
 create mode 100644 four.txt
 create mode 100644 myFolder/3.txt
 delete mode 100644 two.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    one.txt

no changes added to commit (use "git add" and/or "git commit -a")

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git add .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git rm four.txt
rm 'four.txt'

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    four.txt
        deleted:    one.txt


satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ get reset
bash: get: command not found

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git reset
Unstaged changes after reset:
D       four.txt
D       one.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    four.txt
        deleted:    one.txt

no changes added to commit (use "git add" and/or "git commit -a")

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git reset --HARD
error: unknown option `HARD'
usage: git reset [--mixed | --soft | --hard | --merge | --keep] [-q] [<commit>]
   or: git reset [-q] [<tree-ish>] [--] <pathspec>...
   or: git reset [-q] [--pathspec-from-file [--pathspec-file-nul]] [<tree-ish>]
   or: git reset --patch [<tree-ish>] [--] [<pathspec>...]
   or: DEPRECATED: git reset [-q] [--stdin [-z]] [<tree-ish>]

    -q, --[no-]quiet      be quiet, only report errors
    --no-refresh          skip refreshing the index after reset
    --refresh             opposite of --no-refresh
    --mixed               reset HEAD and index
    --soft                reset only HEAD
    --hard                reset HEAD, index and working tree
    --merge               reset HEAD, index and working tree
    --keep                reset HEAD but keep local changes
    --[no-]recurse-submodules[=<reset>]
                          control recursive updating of submodules
    -p, --[no-]patch      select hunks interactively
    --[no-]auto-advance   auto advance to the next file when selecting hunks int
eractively
    -U, --unified <n>     generate diffs with <n> lines context
    --inter-hunk-context <n>
                          show context between diff hunks up to the specified nu
mber of lines
    -N, --[no-]intent-to-add
                          record only the fact that removed paths will be added
later
    --[no-]pathspec-from-file <file>
                          read pathspec from file
    --[no-]pathspec-file-nul
                          with --pathspec-from-file, pathspec elements are separ
ated with NUL character
    -z                    DEPRECATED (use --pathspec-file-nul instead): paths ar
e separated with NUL character
    --[no-]stdin          DEPRECATED (use --pathspec-from-file=- instead): read
paths from <stdin>


satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git reset --hard
HEAD is now at afbaccb i have made some changes to the File

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ /git status
bash: /git: No such file or directory

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git rm four.txt
error: the following file has local modifications:
    four.txt
(use --cached to keep the file, or -f to force removal)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git rm -f four.txt
rm 'four.txt'

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git reset --hard
HEAD is now at afbaccb i have made some changes to the File

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git rm --cached four.txt
rm 'four.txt'

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    four.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        four.txt


satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git add .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   four.txt


satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git reset --hard
HEAD is now at afbaccb i have made some changes to the File

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git rm -r myFolder
rm 'myFolder/3.txt'
Deletion of directory 'myFolder' failed. Should I try again? (y/n) y
Deletion of directory 'myFolder' failed. Should I try again? (y/n) y
Deletion of directory 'myFolder' failed. Should I try again? (y/n) y
Deletion of directory 'myFolder' failed. Should I try again? (y/n) y
Deletion of directory 'myFolder' failed. Should I try again? (y/n) n

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git rm -r myfolder
fatal: pathspec 'myfolder' did not match any files

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git rm -r myFolder
fatal: pathspec 'myFolder' did not match any files

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ explorer .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git rm -r myFolder
fatal: pathspec 'myFolder' did not match any files

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git reset -hard
error: did you mean `--hard` (with two dashes)?

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git reset --hard
HEAD is now at afbaccb i have made some changes to the File

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git rm -r myFolder
rm 'myFolder/3.txt'
Deletion of directory 'myFolder' failed. Should I try again? (y/n) y
Deletion of directory 'myFolder' failed. Should I try again? (y/n)
Sorry, I did not understand your answer. Please type 'y' or 'n'
Deletion of directory 'myFolder' failed. Should I try again? (y/n) y
Deletion of directory 'myFolder' failed. Should I try again? (y/n) n

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git rm -r myFolder
fatal: pathspec 'myFolder' did not match any files

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git rm -r myFolder
fatal: pathspec 'myFolder' did not match any files

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ explorer .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git add .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    myFolder/3.txt
        new file:   myFolder/three.txt


satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ ls
README.md  four.txt  myFolder/  one.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git rm -r myFolder
error: the following file has changes staged in the index:
    myFolder/three.txt
(use --cached to keep the file, or -f to force removal)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git reset -hard
error: did you mean `--hard` (with two dashes)?

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git reset --hard
Deletion of directory 'myFolder' failed. Should I try again? (y/n) y
Deletion of directory 'myFolder' failed. Should I try again? (y/n) y
Deletion of directory 'myFolder' failed. Should I try again? (y/n) y
Deletion of directory 'myFolder' failed. Should I try again? (y/n) y
Deletion of directory 'myFolder' failed. Should I try again? (y/n) n
Updating files: 100% (2/2), done.
HEAD is now at afbaccb i have made some changes to the File

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git reset --hard
HEAD is now at afbaccb i have made some changes to the File

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git rm -r myFolder
rm 'myFolder/3.txt'
Deletion of directory 'myFolder' failed. Should I try again? (y/n) n

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git reset --hard
HEAD is now at afbaccb i have made some changes to the File

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git log
commit afbaccb47a296fee20a591d603e0735686b75084 (HEAD -> main)
Author: Sattire <sattire729@gmail.com>
Date:   Mon May 18 16:01:53 2026 +0530

    i have made some changes to the File

commit 5658100c437381fc2eab27423a2d5399b282bd1e (origin/main, origin/HEAD)
Author: Pradyumna-Singh729 <sattire729@gmail.com>
Date:   Mon May 18 13:18:49 2026 +0530

    Add new file two.txt with a single line

commit f9530ebbed7540ee46a24ba94c56a9cc3e1246b0
Author: Pradyumna-Singh729 <sattire729@gmail.com>
Date:   Mon May 18 13:18:06 2026 +0530

    Add one.txt with initial content '1'

commit 7f36d91fe22ddd9c2e21d42a76e95fea637af52d
Author: Pradyumna-Singh729 <sattire729@gmail.com>
Date:   Mon May 18 13:16:05 2026 +0530

    Initial commit
...skipping...

                   SUMMARY OF LESS COMMANDS

      Commands marked with * may be preceded by a number, N.
      Notes in parentheses indicate the behavior if N is given.
      A key preceded by a caret indicates the Ctrl key; thus ^K is ctrl-K.

  h  H                 Display this help.
  q  :q  Q  :Q  ZZ     Exit.
 ---------------------------------------------------------------------------

                           MOVING

  e  ^E  j  ^N  CR  *  Forward  one line   (or N lines).
  y  ^Y  k  ^K  ^P  *  Backward one line   (or N lines).
  ESC-j             *  Forward  one file line (or N file lines).
  ESC-k             *  Backward one file line (or N file lines).
  f  ^F  ^V  SPACE  *  Forward  one window (or N lines).
  b  ^B  ESC-v      *  Backward one window (or N lines).
  z                 *  Forward  one window (and set window to N).
  w                 *  Backward one window (and set window to N).
  ESC-SPACE         *  Forward  one window, but don't stop at end-of-file.
  ESC-b             *  Backward one window, but don't stop at beginning-of-file.
 ESCESCESCq...skipping...
commit afbaccb47a296fee20a591d603e0735686b75084 (HEAD -> main)
Author: Sattire <sattire729@gmail.com>
Date:   Mon May 18 16:01:53 2026 +0530

    i have made some changes to the File

commit 5658100c437381fc2eab27423a2d5399b282bd1e (origin/main, origin/HEAD)
Author: Pradyumna-Singh729 <sattire729@gmail.com>
Date:   Mon May 18 13:18:49 2026 +0530

    Add new file two.txt with a single line

commit f9530ebbed7540ee46a24ba94c56a9cc3e1246b0
Author: Pradyumna-Singh729 <sattire729@gmail.com>
Date:   Mon May 18 13:18:06 2026 +0530

    Add one.txt with initial content '1'

commit 7f36d91fe22ddd9c2e21d42a76e95fea637af52d
Author: Pradyumna-Singh729 <sattire729@gmail.com>
Date:   Mon May 18 13:16:05 2026 +0530

    Initial commit

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git log --oneline
afbaccb (HEAD -> main) i have made some changes to the File
5658100 (origin/main, origin/HEAD) Add new file two.txt with a single line
f9530eb Add one.txt with initial content '1'
7f36d91 Initial commit

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git branch
* main

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git branch delelopment

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git branch
  delelopment
* main

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git checkout delelopment
Switched to branch 'delelopment'

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git status
On branch delelopment
nothing to commit, working tree clean

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git log
commit afbaccb47a296fee20a591d603e0735686b75084 (HEAD -> delelopment, main)
Author: Sattire <sattire729@gmail.com>
Date:   Mon May 18 16:01:53 2026 +0530

    i have made some changes to the File

commit 5658100c437381fc2eab27423a2d5399b282bd1e (origin/main, origin/HEAD)
Author: Pradyumna-Singh729 <sattire729@gmail.com>
Date:   Mon May 18 13:18:49 2026 +0530

    Add new file two.txt with a single line

commit f9530ebbed7540ee46a24ba94c56a9cc3e1246b0
Author: Pradyumna-Singh729 <sattire729@gmail.com>
Date:   Mon May 18 13:18:06 2026 +0530

    Add one.txt with initial content '1'

commit 7f36d91fe22ddd9c2e21d42a76e95fea637af52d
Author: Pradyumna-Singh729 <sattire729@gmail.com>
Date:   Mon May 18 13:16:05 2026 +0530

    Initial commit

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git branch
* delelopment
  main

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ ls
README.md  four.txt  myFolder/  one.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git status
On branch delelopment
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        three.txt

nothing added to commit but untracked files present (use "git add" to track)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git add .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git commit -m "I created three.txt and entered 3 there"
[delelopment 6f0ca92] I created three.txt and entered 3 there
 1 file changed, 1 insertion(+)
 create mode 100644 three.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git checkout main
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git checkout delelopment
Switched to branch 'delelopment'

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git status
On branch delelopment
nothing to commit, working tree clean

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ explorer .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git ls
git: 'ls' is not a git command. See 'git --help'.

The most similar command is
        lfs

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git ls
git: 'ls' is not a git command. See 'git --help'.

The most similar command is
        lfs

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ ls
README.md  four.txt  myFolder/  one.txt  three.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git checkout main
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   four.txt

no changes added to commit (use "git add" and/or "git commit -a")

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git add .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git commit -m "I changed four.txt and added additional four"
[main ead4020] I changed four.txt and added additional four
 1 file changed, 2 insertions(+), 1 deletion(-)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git checkout development
error: pathspec 'development' did not match any file(s) known to git

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git merge main -m "Merging main into the development"
Already up to date.

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git reset --hard
HEAD is now at ead4020 I changed four.txt and added additional four

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git checkout delelopment
Switched to branch 'delelopment'

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git merge main -m "Merging main into delelopment"
Merge made by the 'ort' strategy.
 four.txt | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git checkout main
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git merge delelopment -m "Merging on main with development"
Updating ead4020..6331023
Fast-forward (no commit created; -m option ignored)
 three.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 three.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git branch staging

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git checkout staging
Switched to branch 'staging'

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (staging)
$ gitstatus
bash: gitstatus: command not found

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (staging)
$ git status
On branch staging
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   four.txt

no changes added to commit (use "git add" and/or "git commit -a")

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (staging)
$ git add .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (staging)
$ git commit -m "changed fourfour"
[staging c6de330] changed fourfour
 1 file changed, 1 insertion(+), 1 deletion(-)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (staging)
$ git check delelopment
git: 'check' is not a git command. See 'git --help'.

The most similar command is
        checkout

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (staging)
$ git checkout delelopment
Switched to branch 'delelopment'

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git add .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git commit -m "add fourfourfour"
[delelopment 60bda98] add fourfourfour
 1 file changed, 1 insertion(+), 1 deletion(-)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git merge staging
Auto-merging four.txt
CONFLICT (content): Merge conflict in four.txt
Automatic merge failed; fix conflicts and then commit the result.

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment|MERGING)
$ git add .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment|MERGING)
$ git commit -m "merge conflict solved"
[delelopment 38d3c93] merge conflict solved

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git checkout staging
Switched to branch 'staging'

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (staging)
$ git merge delelopment
Updating c6de330..38d3c93
Fast-forward
 four.txt | 4 +++-
 1 file changed, 3 insertions(+), 1 deletion(-)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (staging)
$ git add .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (staging)
$ git commit "correction"
error: pathspec 'correction' did not match any file(s) known to git

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (staging)
$ git commit -m "correction"
[staging 90ac56e] correction
 1 file changed, 1 insertion(+), 3 deletions(-)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (staging)
$ git checkout delelopment
Switched to branch 'delelopment'

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git add .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git commit -m "correction"
[delelopment 755a088] correction
 1 file changed, 1 deletion(-)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git merge staging
Auto-merging four.txt
CONFLICT (content): Merge conflict in four.txt
Automatic merge failed; fix conflicts and then commit the result.

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment|MERGING)
$ git merge staging -m "resolved conflict"
error: Merging is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
























[delelopment c0cf674] Merge branch 'staging' into delelopment

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git commit -m "corrwctions on merging"
On branch delelopment
nothing to commit, working tree clean

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git checkout staging
Switched to branch 'staging'

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (staging)
$ git merge delelopment
Updating 90ac56e..c0cf674
Fast-forward
 four.txt | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (staging)
$ git checkout main
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 4 commits.
  (use "git push" to publish your local commits)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git merge staging
Updating 6331023..c0cf674
Fast-forward
 four.txt | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git log --oneline
c0cf674 (HEAD -> main, staging, delelopment) Merge branch 'staging' into delelopment
755a088 correction
90ac56e correction
38d3c93 merge conflict solved
60bda98 add fourfourfour
c6de330 changed fourfour
6331023 Merging main into delelopment
ead4020 I changed four.txt and added additional four
6f0ca92 I created three.txt and entered 3 there
afbaccb i have made some changes to the File
5658100 (origin/main, origin/HEAD) Add new file two.txt with a single line
f9530eb Add one.txt with initial content '1'
7f36d91 Initial commit

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git add .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git commit -m "update one.txt file"
[main 3016ffc] update one.txt file
 1 file changed, 2 insertions(+), 1 deletion(-)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git log --online
fatal: unrecognized argument: --online

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git log --oneline
3016ffc (HEAD -> main) update one.txt file
c0cf674 (staging, delelopment) Merge branch 'staging' into delelopment
755a088 correction
90ac56e correction
38d3c93 merge conflict solved
60bda98 add fourfourfour
c6de330 changed fourfour
6331023 Merging main into delelopment
ead4020 I changed four.txt and added additional four
6f0ca92 I created three.txt and entered 3 there
afbaccb i have made some changes to the File
5658100 (origin/main, origin/HEAD) Add new file two.txt with a single line
f9530eb Add one.txt with initial content '1'
7f36d91 Initial commit

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ ^C

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git checkout 331023
error: pathspec '331023' did not match any file(s) known to git

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git checkout 6331023
Note: switching to '6331023'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 6331023 Merging main into delelopment

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo ((6331023...))
$ git status
HEAD detached at 6331023
nothing to commit, working tree clean

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo ((6331023...))
$ git checkout main
Previous HEAD position was 6331023 Merging main into delelopment
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 11 commits.
  (use "git push" to publish your local commits)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git push origin main
info: please complete authentication in your browser...
Enumerating objects: 32, done.
Counting objects: 100% (32/32), done.
Delta compression using up to 2 threads
Compressing objects: 100% (20/20), done.
Writing objects: 100% (30/30), 2.30 KiB | 294.00 KiB/s, done.
Total 30 (delta 11), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (11/11), done.
remote: This repository moved. Please use the new location:
remote:   https://github.com/sattire729/my-first-repo.git
To https://github.com/Pradyumna-Singh729/my-first-repo.git
   5658100..3016ffc  main -> main

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git checkout staging
Switched to branch 'staging'

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (staging)
$ git push origin staging
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: This repository moved. Please use the new location:
remote:   https://github.com/sattire729/my-first-repo.git
remote:
remote: Create a pull request for 'staging' on GitHub by visiting:
remote:      https://github.com/sattire729/my-first-repo/pull/new/staging
remote:
To https://github.com/Pradyumna-Singh729/my-first-repo.git
 * [new branch]      staging -> staging

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (staging)
$ git checkout development
error: pathspec 'development' did not match any file(s) known to git

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (staging)
$ git checkout delelopment
Switched to branch 'delelopment'

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git push origin development
error: src refspec development does not match any
error: failed to push some refs to 'https://github.com/Pradyumna-Singh729/my-first-rep
o.git'

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git push origin delelopment
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: This repository moved. Please use the new location:
remote:   https://github.com/sattire729/my-first-repo.git
remote:
remote: Create a pull request for 'delelopment' on GitHub by visiting:
remote:      https://github.com/sattire729/my-first-repo/pull/new/delelopment
remote:
To https://github.com/Pradyumna-Singh729/my-first-repo.git
 * [new branch]      delelopment -> delelopment

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git fetch origin --prune
From https://github.com/Pradyumna-Singh729/my-first-repo
 - [deleted]         (none)      -> origin/delelopment
 * [new branch]      development -> origin/development

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git log --oneline
c0cf674 (HEAD -> delelopment, origin/staging, origin/development, staging) Merge branc
h 'staging' into delelopment
755a088 correction
90ac56e correction
38d3c93 merge conflict solved
60bda98 add fourfourfour
c6de330 changed fourfour
6331023 Merging main into delelopment
ead4020 I changed four.txt and added additional four
6f0ca92 I created three.txt and entered 3 there
afbaccb i have made some changes to the File
5658100 Add new file two.txt with a single line
f9530eb Add one.txt with initial content '1'
7f36d91 Initial commit

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (delelopment)
$ git branch -m development

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (development)
$ git branch --set-upstream-to=origin/development development
branch 'development' set up to track 'origin/development'.

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (development)
$ git pull
Already up to date.

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (development)
$ git add .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (development)
$ git commit -m "renamed branch development"
On branch development
Your branch is up to date with 'origin/development'.

nothing to commit, working tree clean

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (development)
$ git push origin development
Everything up-to-date

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (development)
$ git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git fetch
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 911 bytes | 41.00 KiB/s, done.
From https://github.com/Pradyumna-Singh729/my-first-repo
   3016ffc..d67a4a5  main       -> origin/main

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git merge
Updating 3016ffc..d67a4a5
Fast-forward
 three.txt | 3 ++-
 1 file changed, 2 insertions(+), 1 deletion(-)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git pull
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 915 bytes | 35.00 KiB/s, done.
From https://github.com/Pradyumna-Singh729/my-first-repo
   d67a4a5..6cbba86  main       -> origin/main
Updating d67a4a5..6cbba86
Fast-forward
 three.txt | 1 +
 1 file changed, 1 insertion(+)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git restore
fatal: you must specify path(s) to restore

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git restore one.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git checkout development
error: Your local changes to the following files would be overwritten by checkout:
        one.txt
Please commit your changes or stash them before you switch branches.
Aborting

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git stash
Saved working directory and index state WIP on main: 6cbba86 Add 'threethree' to three
.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git checkout devlopment
error: pathspec 'devlopment' did not match any file(s) known to git

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git checkout development
Switched to branch 'development'
Your branch is up to date with 'origin/development'.

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (development)
$ git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git stash pop
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   one.txt

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (bd6a4652e18c878870f2edbdbd17ce82f304785f)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git stash
Saved working directory and index state WIP on main: 6cbba86 Add 'threethree' to three
.txt
git
satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git stash apply
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   one.txt

no changes added to commit (use "git add" and/or "git commit -a")

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git stash list
stash@{0}: WIP on main: 6cbba86 Add 'threethree' to three.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git stash drop
Dropped refs/stash@{0} (f92ec37c02a1fbf931f9aca262218130e3744701)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git stash list

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   one.txt

no changes added to commit (use "git add" and/or "git commit -a")

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git stash
Saved working directory and index state WIP on main: 6cbba86 Add 'threethree' to three
.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git stash list
stash@{0}: WIP on main: 6cbba86 Add 'threethree' to three.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git stash pop
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   one.txt

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (1965038daa70410e7859dfc7152db64d6df8c91b)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git stash list

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git stash
Saved working directory and index state WIP on main: 6cbba86 Add 'threethree' to three
.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git stash list
stash@{0}: WIP on main: 6cbba86 Add 'threethree' to three.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git stash apply
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   one.txt

no changes added to commit (use "git add" and/or "git commit -a")

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git stash list
stash@{0}: WIP on main: 6cbba86 Add 'threethree' to three.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git stash
Saved working directory and index state WIP on main: 6cbba86 Add 'threethree' to three
.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git stash list
stash@{0}: WIP on main: 6cbba86 Add 'threethree' to three.txt
stash@{1}: WIP on main: 6cbba86 Add 'threethree' to three.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git add .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git commit -m "hello 3"
[main e453ed3] hello 3
 1 file changed, 1 insertion(+)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git log oneline
fatal: ambiguous argument 'oneline': unknown revision or path not in the working tree.
Use '--' to separate paths from revisions, like this:
'git <command> [<revision>...] -- [<file>...]'

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git long --oneline
git: 'long' is not a git command. See 'git --help'.

The most similar commands are
        clone
        log


Revert "hello 3"























[main 6af6b36] Revert "hello 3"
 1 file changed, 1 deletion(-)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git log --onelime
fatal: unrecognized argument: --onelime

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git lof --oneline
git: 'lof' is not a git command. See 'git --help'.

The most similar command is
        log

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git log --oneline
6af6b36 (HEAD -> main) Revert "hello 3"
e453ed3 hello 3
6cbba86 (origin/main, origin/HEAD) Add 'threethree' to three.txt
d67a4a5 Add 'three' to three.txt
3016ffc update one.txt file
c0cf674 (origin/staging, origin/development, staging, development) Merge branch 'stagi
ng' into delelopment
755a088 correction
90ac56e correction
38d3c93 merge conflict solved
60bda98 add fourfourfour
c6de330 changed fourfour
6331023 Merging main into delelopment
ead4020 I changed four.txt and added additional four
6f0ca92 I created three.txt and entered 3 there
afbaccb i have made some changes to the File
5658100 Add new file two.txt with a single line
f9530eb Add one.txt with initial content '1'
7f36d91 Initial commit

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git push
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 2 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 437 bytes | 218.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote: This repository moved. Please use the new location:
remote:   https://github.com/sattire729/my-first-repo.git
To https://github.com/Pradyumna-Singh729/my-first-repo.git
   6cbba86..6af6b36  main -> main

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git log --oneline
6af6b36 (HEAD -> main, origin/main, origin/HEAD) Revert "hello 3"
e453ed3 hello 3
6cbba86 Add 'threethree' to three.txt
d67a4a5 Add 'three' to three.txt
3016ffc update one.txt file
c0cf674 (origin/staging, origin/development, staging, development) Merge branch 'stagi
ng' into delelopment
755a088 correction
90ac56e correction
38d3c93 merge conflict solved
60bda98 add fourfourfour
c6de330 changed fourfour
6331023 Merging main into delelopment
ead4020 I changed four.txt and added additional four
6f0ca92 I created three.txt and entered 3 there
afbaccb i have made some changes to the File
5658100 Add new file two.txt with a single line
f9530eb Add one.txt with initial content '1'
7f36d91 Initial commit

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git branch feature

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git checkout feature
Switched to branch 'feature'

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (feature)
$ explorer .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (feature)
$ git add ,
fatal: pathspec ',' did not match any files

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (feature)
$ git add .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (feature)
$ git commit -m "Adding dark mode functionality"
[feature 2619f5a] Adding dark mode functionality
 1 file changed, 2 insertions(+), 1 deletion(-)

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (feature)
$ git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git add .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git commit -m "Adding dark mode UI"
[main ea3437f] Adding dark mode UI
 1 file changed, 1 insertion(+)
 create mode 100644 two.txt

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (main)
$ git checkout feature
Switched to branch 'feature'

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (feature)
$ git rebase main
Successfully rebased and updated refs/heads/feature.

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (feature)
$ git push
fatal: The current branch feature has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin feature

To have this happen automatically for branches without a tracking
upstream, see 'push.autoSetupRemote' in 'git help config'.


satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (feature)
$ git push --set-upstream origin feature
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 2 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 612 bytes | 204.00 KiB/s, done.
Total 6 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 1 local object.
remote: This repository moved. Please use the new location:
remote:   https://github.com/sattire729/my-first-repo.git
remote:
remote: Create a pull request for 'feature' on GitHub by visiting:
remote:      https://github.com/sattire729/my-first-repo/pull/new/feature
remote:
To https://github.com/Pradyumna-Singh729/my-first-repo.git
 * [new branch]      feature -> feature
branch 'feature' set up to track 'origin/feature'.

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (feature)
$ git add .

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (feature)
$ git commit . -m "Final changes to feature"
On branch feature
Your branch is up to date with 'origin/feature'.

nothing to commit, working tree clean

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (feature)
$ git push
Everything up-to-date

satti@DESKTOP-JHB7J8S MINGW64 ~/OneDrive/Desktop/my-first-repo (feature)
$ 
```
</details>  
 
### Git and GitHub Learning Notes, Handwritten
Page 1:
![Git and GitHub Basics Page 5](git_basics_5.jpg)
Page 2:
![Git and GitHub Basics Page 6](git_basics_6.jpg)
Page 3:
![Git and GitHub Basics Page 7](git_basics_7.jpg)
Page 4:
![Git and GitHub Basics Page 8](git_basics_8.jpg)
Page 5:
![Git and GitHub Basics Page 9](git_basics_9.jpg)
