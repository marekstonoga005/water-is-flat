rm -rf rawrz
tar -xf volx.tar.gz
rm -rf rawr1
rm -rf rawr2
rm -rf rawr3
rm -rf rawr4
rm -rf rawr5
cp -r rawrz rawr1
cp -r rawrz rawr2
cp -r rawrz rawr3
cp -r rawrz rawr4
cp -r rawrz rawr5
python3 main1.py &
sleep 8
python3 main2.py &
sleep 8
python3 main3.py &
sleep 8
python3 main4.py &
sleep 8
python3 main5.py
