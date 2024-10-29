"""
This is the one place where you set the path structure of the LO code.
The info is stored in the dict Ldir.

All paths are pathlib.Path objects.

This program is meant to be loaded as a module by Lfun which then adds more
entries to the Ldir dict based on which model run you are working on.

Users should copy this to LO_user/get_lo_info.py, edit as needed, and make it into
their own GitHub repo.

"""
import os
from pathlib import Path

# defaults that should work on all machines
#parent = Path(__file__).absolute().parent.parent
parent = Path('/agdat1')
LO = Path('/data1/jvance/LO')
LOo = Path('/data1/jvance/LO_output')
LOu = Path('/data1/jvance/LO_user')
data = Path('/agdat1/parker/LO_data')

# This is where the ROMS source code, makefiles, and executables are
roms_code = parent / 'parker/LO_roms_source_git'
# NOTE 2023.11.03 This is obsolete. It was only used with an old model version
# and is not used in any current ones.

# This is a new piece of information, to help with integration of
# Aurora Leeson's new LO_traps repo, 2023.11.03.
traps_name = 'traps00'
# In order for this to be more useful it would have to be integrated
# into Aurora's code.
# I'm not sure this is the best way to solve this problem.

# These are places where the ROMS history files are kept
roms_out = parent / 'parker/LO_roms'
roms_out1 = Path('/agdat1/parker/LO_roms') # placeholder
roms_out2 = Path('/agdat1/parker/LO_roms')
roms_out3 = Path('/agdat2/parker/LO_roms')
roms_out4 = Path('/data2/parker/LiveOcean_roms/output')

# these are for mox and klone, other hyak mackines
remote_user = 'BLANK'
remote_machine = 'BLANK'
remote_dir0 = 'BLANK'
local_user = 'BLANK'

# default for linux machines
which_matlab = '/usr/local/bin/matlab'

lo_env = 'jv_mac'

Ldir0 = dict()
Ldir0['lo_env'] = lo_env
Ldir0['parent'] = parent
Ldir0['LO'] = LO
Ldir0['LOo'] = LOo
Ldir0['LOu'] = LOu
Ldir0['data'] = data
Ldir0['roms_code'] = roms_code
Ldir0['roms_out'] = roms_out
Ldir0['roms_out1'] = roms_out1
Ldir0['roms_out2'] = roms_out2
Ldir0['roms_out3'] = roms_out3
Ldir0['roms_out4'] = roms_out4
Ldir0['which_matlab'] = which_matlab
#
Ldir0['remote_user'] = remote_user
Ldir0['remote_machine'] = remote_machine
Ldir0['remote_dir0'] = remote_dir0
Ldir0['local_user'] = local_user
#
Ldir0['traps_name'] = traps_name


