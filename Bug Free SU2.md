# Bug Free SU2
## Build an advanced MPI version from source in Lunux/Ubuntu
<br/>
<br/>

**Browse the latest version SU2 from Github**
<br/>
SU2-7.3.1.tar.gz
<br/>

**Unzip it by typing:**
<br/>
tar -xvzf SU2-7.3.1.tar.gz
<br/>

**Create a virtualenv outside the SU2-7.3.1**
<br/>
sudo apt-get install virtualenv
<br/>
virtualenv --python=python3.env
<br/>
source env/bin/activate
<br/>

**Download openmpi**
<br/>
sudo apt-get install openmpi-bin
<br/>

**Check whether your /usr/bin/ has mpicc and mpicxx**
<br/>

**Change gcc by mpicc**
<br/>
export CC=/usr/bin/mpicc
<br/>
export CXX=/usr/bin/mpicxx
<br/>
export PYTHONPATH=/home/xxx/env/bin
<br/>

**Go to the /home/xxx/SU2-7.3.1/externals/cgns/hdf5/meson.build and modify code in line 28&29**
<br/>
opt_zlib = dependency('zlib', required: false, static: false)
opt_szip = dependency('szip', required: false, static: false)

**Build by meson (Do not reconfigure)**
<br/>
./meson.py build -Dcustom-mpi=true -Denable-autodiff=true -Denable-pywrapper=true
<br/>

**Install by ninja**
<br/>
./ninja -C build install
<br/>

**Change environment variables**
<br/>
nano .bashrc
>>export SU2_RUN=/usr/local/bin (you can see some files and python code here, in some cases it is in the /home/xxx/SU2-7.3.1/SU2/bin
>>export su2_home=/home/xxx/SU2-7.3.1
>>export PATH=$PATH:$SU2_RUN
>>export PYTHONPATH=$PYTHONPATH:$SU2_RUN
source .bashrc
<br/>









