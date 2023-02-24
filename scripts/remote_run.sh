
while getopts ":hr:" option; do
   case $option in
      h) # display Help
         Help
         exit;;
      r) # remote
         host=$OPTARG;;
     \?) # Invalid option
         echo "Error: Invalid option"
         exit;;
   esac
done

dir=${PWD##*/}  
echo "dir: ${dir}"
docker -H ${host} run -e VEHICLE_NAME=${host} -v /var/run/avahi-deamon/socket:/var/run/avahi-deamon/socket -v /data:/data --network host -d duckietown/${dir}:v2-arm64v8 