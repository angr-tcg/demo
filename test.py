#!/usr/bin/env python
import os
import os.path
import angr

# Path to input binary
this_dir = os.path.dirname(os.path.abspath(__file__))
test_bin = os.path.join(this_dir, 'pytcg/test/simple_loop.bin')

# Options passed to cle loader
main_opts = {
    'backend': 'blob',
    'custom_arch': 'amd64',
    'custom_entry_point': 0xb0000000,
    'custom_base_addr': 0xb0000000,
}

# Create the Angr project and load the first basic block located at the entry
p = angr.Project(test_bin, auto_load_libs=False, main_opts=main_opts)
s = p.factory.entry_state()
b = s.block()

# Pretty-print target arch instructions
print('Input Block Instructions')
print('------------------------')
b.capstone.pp()

print('')

# Pretty-print IR
print('Intermediate Representation')
print('---------------------------')
b.vex.pp()
