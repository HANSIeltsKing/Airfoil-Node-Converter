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

**Install mpi4py**
<br/>
pip3 install mpi4py
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
<br/>
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
<br/>
<br/>
export SU2_RUN=/usr/local/bin (you can see some files and python code here, in some cases it is in the /home/xxx/SU2-7.3.1/SU2/bin
<br/>
export su2_home=/home/xxx/SU2-7.3.1
<br/>
export PATH=$PATH:$SU2_RUN
<br/>
export PYTHONPATH=$PYTHONPATH:$SU2_RUN
<br/>
<br/>
source .bashrc
<br/>

**Install scipy and mpi4py again**
<br/>
pip3 install mpi4py --target=/...
<br/>
pip3 install scipy --target=/...
<br/>

## Possible errors
<br/>

**1. Lacking mpi.h**
<br/>
Upzipping again, do not reconfigure.
<br/>

**2. Linking target SU2_PY/pySU2/_pysu2.so Failed: SU2_PY/pySU2/_pysu2.so or lacking mpi4py/mpi4py.h**
<br/>
Editting code in the /home/xxx/SU2-7.3.1/externals/cgns/hdf5/meson.build is necessary
<br/>

**3. Error: Tried to form an absolute path to a source dir. You should not do that but use relative paths instead**
<br/>
That is why two mpi4pys are used.
<br/>
env should be outside the SU2-7.3.1
<br/>

**4. Linux command no permission**
<br/>
sudo su
<br/>
your password
<br/>

**5. WSL no permission**
<br/>
sudo chmod -R 777 /home/xxx/
<br/>







