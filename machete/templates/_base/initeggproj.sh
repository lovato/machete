#!/bin/bash

if [ $# = 0 ]; then
	echo "Usage: initeggproj.sh <new_software_name>"
else
	project=$1
	project=`echo $project | sed 's/-/_/g'`
	target='/tmp/'$project

	echo
	echo "Doing it..."
	echo "Destination Path: "$target
	git checkout master >> /dev/null
	rm -rf $target
	mkdir $target
    git init $target
	cp -R . $target
	cd $target
	rm -rf *egg-info
	rm -rf dist
	rm initeggproj.sh
	mv packagesample $project
	echo "Replacing some default strings to "$project
	sed -i "s/packagesample/$project/g" setup.py
	sed -i "s/packagesample/$project/g" README.md
	sed -i "s/packagesample/$project/g" run.py
	sed -i "s/packagesample/$project/g" MANIFEST.in
	sed -i "s/packagesample/$project/g" docs/source/changelog.rst
	sed -i "s/packagesample/$project/g" $project/start.py
	sed -i "s/packagesample/$project/g" $project/__init__.py
	sed -i "s/packagesample/$project/g" $project/submodule/module.py
	sed -i "s/packagesample/$project/g" $project/submodule/__init__.py
	sed -i "s/packagesample/$project/g" tests/test_version.py
	sed -i "s/packagesample/$project/g" setup.cfg
	mv docs/example/packagesample.cfg docs/example/$project.cfg
	#ln -s pre-commit-source $project/.git/hooks/pre-commit
	echo "Creating virtualenv"
	deactivate 2>> /dev/null
	rm -rf $WORKON_HOME/$project
	virtualenv $WORKON_HOME/$project
	source $WORKON_HOME/$project/bin/activate
	echo $project > .venv
	if [ -f requirements.txt ]; then
		echo "Installing base requirements for $project (please hold...)"
		pip install -r requirements.txt
	fi
	if [ -f requirements-dev.txt ]; then
		echo "Installing development requirements for $project (please hold...)"
		pip install -r requirements-dev.txt
	fi
	echo
	echo "Done, my friend. Copy the whole folder from:"
	echo $target
	echo "And then add a remote to it, add and commit your changes."
	echo
fi
