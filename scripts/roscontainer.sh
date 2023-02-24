
# Set variables
host="none"
remote="none"
while getopts ":hr:" option; do
   case $option in
      h) # display Help
         Help
         exit;;
      r) # remote ip
         remote=$OPTARG;;
      i) # own ip
         host=$OPTARG;;
     \?) # Invalid option
         echo "Error: Invalid option"
         exit;;
   esac
done

if [ $host == "none" ]; then
   host=$(hostname -I | awk '{print $1}')
   echo "No host ip specified, using ${host}"
fi

if [ $remote == "none" ]; then
   echo "No remote ip specified"
   exit -1
fi

docker run -it --rm --net host -e ROS_MASTER_URI="http://${remote}:11311/" -e ROS_IP=$host duckietown/dt-ros-commons:daffy /bin/bash
