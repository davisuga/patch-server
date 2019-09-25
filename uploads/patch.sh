wget 10.2.135.26:5000/static/img/back.jpg
xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/workspace0/last-image -s $PWD"/back.jpg"
