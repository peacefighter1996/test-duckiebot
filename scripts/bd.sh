#!/bin/bash
############################################################
# Help                                                     #
############################################################
Help()
{
   # Display Help
   echo "quick build and deploy script for deploying package on a remote host"
   echo
   echo "Syntax: scriptTemplate [-h|r]"
   echo "options:"
   echo "r     remote host to deploy to"
   echo "h     Print this Help."
   echo
}

############################################################
# Build                                                    #
############################################################
Build()
{
   echo "Start build on ${host}"
   dts devel build -f -H ${host}
   echo "Finished build"
}

############################################################
# Deploy                                                   #
############################################################
Deploy()
{
   echo "Start deploy on ${host}"
   dts devel run -f -H ${host}
   echo "Finished deploy"
}

############################################################
############################################################
# Main program                                             #
############################################################
############################################################

# Set variables
host="none"
deploy="false"
build="false"
############################################################
# Process the input options. Add options as needed.        #
############################################################
# Get the options
while getopts ":hr:bd" option; do
   case $option in
      h) # display Help
         Help
         exit;;
      r) # remote
         host=$OPTARG;;
      d) # deploy
         echo "run with deploy"
         deploy="true";;
      b) # build
         echo "run with build"
         build="true";;
     \?) # Invalid option
         echo "Error: Invalid option"
         exit;;
   esac
done

if [ $host == "none" ]; then
   echo "No name specified"
   exit -1
fi

echo "host: ${host}"
echo "deploy: ${deploy}"
echo "build: ${build}"

if [ $build == "false" ] && [ $deploy == "false" ]; then
   echo "No build or deploy specified"
   Build
   Deploy
elif [ $build == "true" ]; then
   echo "run build"
   Build
elif [ $deploy == "true" ]; then
   echo "run"
   Deploy
fi
