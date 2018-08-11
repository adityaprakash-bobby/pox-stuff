Setup for running w/ PyPy Interpreter:
----------------------------------------------------------------------------------
#copy the pypy folder into the pox folder.
#pypy already has pandas, scipy and numpy installed with it.

mininet@mininet-vm$sudo cp -rf ./pypy ~/pox
mininet@mininet-vm$sudo cp ./l3_new.py ./detect_new.py ~/pox/pox/forwarding	


Setup for running w/o PyPy interpreter:
-----------------------------------------------------------------------------------
mininet@mininet-vm$sudo apt-get install python-pandas python-numpy python-scipy
mininet@mininet-vm$sudo cp ./l3_new.py ./detect_new.py ~/pox/pox/forwarding


In TTY1:
-----------------------------------------------------------------------------------
mininet@mininet-vm$cd pox/

mininet@mininet-vm:~/pox$sudo ./pox.py forwaring.l3_new 


In TTY 2:
-----------------------------------------------------------------------------------
mininet@mininet-vm$sudo mn --controller remote --switch ovsk --topo tree,2,4
 ...

mininet>xterm h1


In XTerm H1:
-----------------------------------------------------------------------------------
root@mininet-vm$python <path-to-codes>/traffic.py -s 2 -e <#-of-last-host + 1>
 ...
 ...
 ...

root@mininet-vm$python <path-to-codes>/attack.py 10.0.0.x 
 ...
 ...
 ...

-----------------------------------------------------------------------------------


