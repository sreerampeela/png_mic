# The script for fully automated comparative modeling with Loop refinement
# Adapted from MODELLER manual

from modeller import *
from modeller.automodel import * # Load the AutoModel class
import argparse
# Creating arguments
parser = argparse.ArgumentParser()
parser.add_argument("--query", help="The name of query sequence in the alignment file")
parser.add_argument("--template", help="The name of template(s) in the alignment file. Separate multiple template names with commas(,)")
parser.add_argument("--pirfile", help="The name of the alignment file")
parser.add_argument("--nmodels", help="Number of models to generate")
args = parser.parse_args() # to parse the arguments
log.verbose()
env = Environ()

# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']
a = LoopModel(env,
# file with template codes and target sequence
alnfile = args.pirfile,
# PDB codes of the templates
knowns = (args.template.split(",")),
# code of the target
sequence = args.query)
a.auto_align() # get an automatic alignment
a.md_level = None # No refinement of model
a.loop.starting_model = 1 # First loop model
a.loop.ending_model = int(args.nmodels) # Last loop model
a.loop.md_level = refine.fast # Loop model refinement level
a.make() # do comparative modeling
