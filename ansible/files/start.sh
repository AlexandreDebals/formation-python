nohup node app.js > start.out 2>&1 &
echo $! > pid.txt # enregistrment du pid du dernier processus lancé