# PyhtonCrashCourse_2ndEd
Notes and Tutorials of walking through the book
using git

#There are three states we need to know about
	# working directory
		# untracked and modified files
		# listed when use git status
	# staging area
		# organize what we want to be committed
		# allows for detailed commits
			# very detailed commits
		# add files to the staging area
	# .git directory (repo)


##### two common scenerios: #####

##### initialize a repository from existing code: #####

		##### working directory: #####

# from within directory in the terminal
$ git init

cloned-repo
local-repo

$ ls 
	# to list the directories

$ git init 
	# will start tracking the directory on your computer

$ rm -rf .git
	#removes the tracking of the folder

$ git status
	# show untracked files

$ touch .gitignore ("touch" Unix or Mac only)
$ echo "first line" >> .gitignore
	# creates the git ignore file
	# open in editor to add the files
	# save it
$ git status
	# now it will now show the files you listed

		##### staging area: #####

$ git add -A
	# adds all the files that are untracked or modified

##### OR #####

$ git add <file name>
	# to add individually

$ git status

$ git reset or with <file name>
	# removes file(s) from add so not to be committed

##### our first commit #####

$ git commit -m "Initial Commit"
	# initial commit is typically the shell of the code
	# we are now successfully tracking those changes and new files

$ git log
	# shows the commits that we made

##### cloning a remote repo #####

$ git clone <url> <where to clone>
	# <url> is the repo you want to clone down to your local
	# using a period (.) means (in the current directory)
	# be in the directory you want to clone to

$ git remote -v
	# view information about the remote repo

$ git branch -a
	# lists all the branches of the repo 

##### Changes made to files #####

$ git diff
	# shows the changes made to the code
	# maybe not necessary with VS CODE

$ git status
	# show modified files

$ git add -A
	# to add all the changed files to the staging area

$ git commit -m "Changes to blah, made because blah"
	# now we have commited the files LOCALLY
	# we still NEED to push to the remote repo (online)

##### VERY IMPORTANT #####

$ git pull origin master
	# pulls any changes to that were made since the last time we pulled from the repo

$ git push origin master
	# origin is the name of the repo
	# master is the branch we're going to

##### common workflow ##### ##### Branches #####

$ git branch calc-divide
	# create branch <calc-divide> as common practice

$ git checkout calc-divide
	# lets you work out on that branch

$ git status

$ git add -A

$ git commit -m "Divide Function"

$ git push -u origin calc-divide
	# pushed to the remote repo
	# otherwise its origin <branch>

$ git branch -a
	# view branches remote and local

##### merge a branch to master #####

$ git checkout master
	# on local repo

$ git pull origin master
	# incase changes were made
	# on local repo

$ git branch --merged
	# shows branches merged
	# on local repo

$ git merge calc-divide
	# be in the master branch
	# on local repo

$ git push origin master
	# pushing to remote

##### delete the branch #####

$ git branch -d calc-divide (BIG D?)
	# delete when done merging

$ git push origin --delete <branch name>



#### Nick's Presentation

git add . (period) is also a way to get all!

jira always use that to create branches

tableau link for tableau files

$ git fetch origin
	# updates the local repo

$ git merge origin/master
	# updates the local master from the repo master
