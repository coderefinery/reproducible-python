(branching-and-committing)=

# Creating branches and commits

The first and most basic task to do in Git is **record changes** using
commits. In this part, we will record changes in two
ways: on a **new branch** (which supports multiple lines of work at once), and directly
on the "main" branch (which happens to be the default branch here).

:::{objectives}
- Record new changes to our own copy of the project.
- Understand adding changes in two separate branches.
- See how to compare different versions.
:::


## Background

- In the previous episode we have browsed an existing **repository** and saw **commits**
  and **branches**.
- Each **commit** is a snapshot of the entire project at a certain
  point in time and has a unique identifier (**hash**) .
- A **branch** is a line of development, and the `main` branch or `master` branch
  are often the default branch in Git.
- A branch in Git is like a **sticky note that is attached to a commit**. When we add
  new commits to a branch, the sticky note moves to the new commit.
- **Tags** are a way to mark a specific commit as important, for example a release
  version. They are also like a sticky note, but they don't move when new
  commits are added.

:::{figure} img/gophers.png
:alt: Branching explained with a gopher
:width: 100%

What if two people, at the same time, make two different changes?  Git
can merge them together easily.  Image created using <https://gopherize.me/>
([inspiration](https://twitter.com/jay_gee/status/703360688618536960)).
:::


## Exercise: Creating branches and commits

:::{figure} img/illustrations/branches.png
:alt: Illustration of what we want to achieve in this exercise
:width: 60%

Illustration of what we want to achieve in this exercise.
:::

:::{exercise} Exercise: Practice creating commits and branches (20 min)
1. First create a new branch and then either add a new file or modify an
   existing file and commit the change.  Make sure that you now work **on your
   copy** of the example repository. In your commit you can share a Git or
   programming trick you like.
1. In a new commit, modify the file again.
1. Switch to the `main` branch and create a commit there.
1. Browse the network and locate the commits that you just created ("Insights" -> "Network").
1. Compare the branch that you created with the `main` branch. Can you find an easy way to see the differences?
1. Can you find a way to compare versions between two arbitrary commits in the repository?
1. Try to rename the branch that you created and then browse the network again.
1. Try to create a tag for one of the commits that you created (on GitHub,
   create a "release").
:::

The solution below goes over most of the answers, and you are
encouraged to use it when the hints aren't enough - this is by
design.


## Solution and walk-through


### (1) Create a new branch and a new commit

:::::{tabs}
::::{group-tab} GitHub
1. Where it says "main" at the top left, click, enter a new branch
   name `new-tutorial`, click on the offer to create the new branch
   ("Create branch new-tutorial from main").
1. Make sure you are still on the `new-tutorial` branch (it should say
   it at the top), and click "Add file" → "Create new file" from the
   upper right.
1. Enter a filename where it says "Name your file...".
1. Share some Git or programming trick you like.
1. Click "Commit changes"
1. Enter a commit message. Then click "Commit
   changes".

You should appear back at the file browser view, and see your
modification there.
::::

::::{group-tab} VS Code
1. Make sure that you are on the main branch.
1. Version control button on left sidebar → Three dots in upper right of source control → Branch → Create branch.
1. VS Code automatically switches to the new branch.
4. Create a new file.
4. In the version control sidebar, click the `+` sign to add the file for the next commit.
4. Enter a brief message and click "Commit".
::::

::::{group-tab} Command line
Create a new branch called `new-tutorial` from `main` and switch to it:
```console
$ git switch --create new-tutorial main
```

Then create the new file. Finally add and commit the file:
```console
$ git add tutorial.md  # or a different file name
$ git commit -m "sharing a programming trick"
```
::::
:::::


### (2) Modify the file again with a new commit

:::::{tabs}
::::{group-tab} GitHub
This is similar to before, but we click on the existing file to
modify.

1. Click on the file you added or modified previously.
2. Click the edit button, the pencil icon at top-right.
3. Follow the "Commit changes" instructions as in the previous step.
::::

::::{group-tab} VS Code
Repeat as in the previous step.
::::

::::{group-tab} Command line
Modify the file. Then commit the new change:
```console
$ git add tutorial.md
$ git commit -m "short summary of the change"
```

Make sure to replace "short summary of the change" with a meaningful commit
message.
::::
:::::


### (3) Switch to the main branch and create a commit there

:::::{tabs}
::::{group-tab} GitHub
1. Go back to the main repository page (your user's page).
1. In the branch switch view (top left above the file view), switch to
   `main`.
1. Modify another file that already exists, following the pattern
   from above.
::::

::::{group-tab} VS Code
Use the branch selector at the bottom to switch back to the main branch.  Repeat the same steps as above,
but this time modify a different file.
::::

::::{group-tab} Command line
First switch to the `main` branch:
```console
$ git switch main
```

Then modify a file. Finally `git add` and then commit the change:
```console
$ git commit -m "short summary of the change"
```
::::
:::::


### (4) Browse the commits you just made

Let's look at what we did.  Now, the `main` and `new-tutorial` branches
have diverged: both have some modifications. Try to find the commits
you created.

:::::{tabs}
::::{group-tab} GitHub
Insights tab → Network view (just like we have done before).
::::

::::{group-tab} VS Code
This requires an extension.  Opening the VS Code terminal lets you use the
command line method (View → Terminal will open a terminal at bottom).  This is
a normal command line interface and very useful for work.
::::

::::{group-tab} Command line
```console
$ git graph
$ git log --graph --oneline --decorate --all  # if you didn't define git graph yet.
```
::::
:::::


### (5) Compare the branches

Comparing changes is an important thing we need to do.  When using the
GitHub view only, this may not be so common, but we'll show it so that
it makes sense later on.

:::::{tabs}

::::{group-tab} GitHub
A nice way to compare branches is to add `/compare` to the URL of the repository,
for example (replace USER):
`https://github.com/USER/planets/compare`
::::

::::{group-tab} VS Code
This seems to require an extension.  We recommend you use the command line method.
::::

::::{group-tab} Command line
```console
$ git diff main new-tutorial
```

Try also the other way around:
```console
$ git diff new-tutorial main
```

Try also this if you only want to see the file names that are different:
```console
$ git diff --name-only main new-tutorial
```
::::
:::::


### (6) Compare two arbitrary commits

This is similar to above, but not only between branches.

:::::{tabs}
::::{group-tab} GitHub
Following the `/compare`-trick above, one can compare commits on GitHub by
adjusting the following URL:
`https://github.com/USER/planets/compare/VERSION1..VERSION2`

Replace `USER` with your username and `VERSION1` and `VERSION2` with a commit hash or branch name.
Please try it out.
::::

::::{group-tab} VS Code
Again, we recommend using the Command Line method.
::::

::::{group-tab} Command line
First try this to get a short overview of the commits:
```console
$ git log --oneline
```

Then try to compare any two commit identifiers with `git diff`.
::::
:::::


### (7) Renaming a branch

:::::{tabs}
::::{group-tab} GitHub

Branch button → View all branches → three dots at right side → Rename branch.

::::
::::{group-tab} VS Code
Version control sidebar → Three dots (same as in step 2) → Branch → Rename branch.  Make sure you are on the right branch before you start.
::::

::::{group-tab} Command line
Renaming the current branch:
```console
$ git branch -m new-branch-name
```

Renaming a different branch:
```console
$ git branch -m different-branch new-branch-name
```
::::
:::::


### (8) Creating a tag

Tags are a way to mark a specific commit as important, for example a release
version. They are also like a sticky note, but they don't move when new
commits are added.

:::::{tabs}
::::{group-tab} GitHub
On the right side, below "Releases", click on "Create a new release".

What GitHub calls releases are actually tags in Git with additional metadata.
For the purpose of this exercise we can use them interchangeably.
::::

::::{group-tab} VS Code
Version control sidebar → Three dots (same as in step 2) → Tags → Create tag.  Make sure you are on the expected commit before you do this.
::::

::::{group-tab} Command line
Creating a tag:
```console
$ git tag -a v1.0 -m "New manuscript version for the pre-print"
```
::::
:::::


## Summary

In this part, we saw how we can make changes to our files.  With branches, we
can track several lines of work at once, and can compare their differences.

- You could commit directly to `main` if there is only one single line
  of work and it's only you.
- You could commit to branches if there are multiple lines of work at
  once, and you don't want them to interfere with each other.
- Tags are useful to mark a specific commit as important, for example a
  release version.
- In Git, commits form a so-called "graph". Branches are tags in Git function
  like sticky notes that stick to specific commits. What this means for us is
  that it does not cost any significant disk space to create new branches.
- Not all files should be added to Git. For example, temporary files or
  files with sensitive information or files which are generated as part of
  the build process should not be added to Git. For this we use
  `.gitignore` (more about this later: {ref}`practical-advice`).
- Unsure on which branch you are or what state the repository is in?
  On the command line, use `git status` frequently to get a quick overview.
