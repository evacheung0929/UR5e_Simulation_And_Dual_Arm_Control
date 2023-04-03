# Convert UI file into python 3 QT5 file

pyuic5 -x Robot_Control.ui -o Robot_UI.py

::Remove last line of python file
head -n -1 Robot_UI.py>temp.txt  

::Add back to original
sudo mv temp.txt Robot_UI.py


