# Lab 1 Commit Process

## Command Line Approach

1. Open up a terminal window or command prompt.

2. Navigate to a location of choice, where you would like to clone your repository.

3. In a browser of choice, go to our GitHub Team 6 Project repository

    * https://github.com/BUMETCS673/seprojects-cs673olf24team6

    and click on the green “code” button, a drop down window will appear. Make sure you’re on the `local` tab.

4. There are 3 GitHub link options presented that can be used to clone the repository. The following instructions will be for the SSH method.

    * HTTPS
    * SSH
    * GitHub CLI

    NOTE: I prefer the SSH way, assuming your SSH keys are set up. If not, GitHub has documentation regarding how to setup SSH keys at this link: 

    https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

5. Once the SSH keys have been generated, please copy the link under SSH tab from the pop up window.

    * The link should look like this: `git@github.com:BUMETCS673/seprojects-cs673olf24team6.git`

6. After copying the link, enter the command below on the terminal that you opened previously:
    
    * `git clone git@github.com:BUMETCS673/seprojects-cs673olf24team6.git`

	Press enter and the repo should be cloned.

    To verify, enter the command:

    * `ls -l`

    The `seprojects-cs673olf24team6` directory should be there.

7. Once the project repo has been made, navigate into it by entering the command:

    * `cd seprojects-cs673olf24team6/`

8. Once in the repo, enter the following command to check the branch you're currently on:

    * `git branch`

    By default, it should be on the `main` branch.

9. Switch to the Lab1 branch by entering the following command:

    * `git checkout Lab1`
    
    To verify that the branch is now `Lab1`, enter the command:

    * `git branch`

    There should be a special character (ex: `*`) next to a highlighted branch name that indicates what branch is
    currently checked out.

10. Make sure the branch is up to date with the latest commits by entering the following command:

    * `git pull`

    This will grab/pull the latest changes on the branch to your cloned repo.

11. Open up the `team.md` file with a editor of your choice and make the changes.

    * To check all current changes made on the local repository, enter the command: 
        - `git diff`

12. Once the changes have been finalized, enter the command:

    * `git add team.md`

    This will add the file to the Git staging area.

13. To verify the correct file has been staged, enter the command:

    * `git status`

    This should show the current file(s) that are staged and the files that are ready to be committed.

14. To commit the file, enter the command:

    * `git commit -m "Enter a message reflecting the changes made"`

    In the quotations, enter a appropriate message regarding the file changes made.

15. Once again, to verify, enter the command: 

    * `git status`

16. Once the files are committed, push the committed files to GitHub by entering the command:

    * `git push`

    **NOTE:** 
    
    In the case that commits have been pushed from another colloborator, follow the instructions the command line states to resolve any merge conflicts. This can
    be done using merge tools or manually moving changes over.

    Please follow the instructions from the link below to resolve merge conflicts:

    https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts

17. There are multiple ways to verify that the changes have been pushed to GitHub. Below are
    two ways.

    * From the cloned local repository, enter the command: `git log`
        - A history/log of previous commits should be displayed in the terminal.

    * On a browser of choice, navigate to:
        - https://github.com/BUMETCS673/seprojects-cs673olf24team6/commits/Lab1/
