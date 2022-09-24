rm -rf rawrz
tar -xf volx.tar.gz
rm -rf rawr1
rm -rf rawr2
cp -r rawrz rawr1
cp -r rawrz rawr2
python3 main1.py &
sleep 8
python3 main2.py
