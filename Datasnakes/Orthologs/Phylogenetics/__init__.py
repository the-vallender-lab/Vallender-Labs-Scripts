"""Phylogenetic tools part of the Orthologs Package"""

import warnings

from Bio import AlignIO
from Datasnakes.Orthologs import OrthologsWarning

# Ignore the warning in this init script.
warnings.simplefilter('ignore', OrthologsWarning)

# Initialize the modules
from Datasnakes.Orthologs.Phylogenetics.PAML import ETE3PAML, PamlTest
from Datasnakes.Orthologs.Phylogenetics.PhyloTree import TreeViz
from Datasnakes.Orthologs.Phylogenetics import PhyML
# Add a new module


class RelaxPhylip(object):
    """Convert the a multiple sequence alignment file to
    relaxed-phylip format.
    """
    def __init__(inputfile, outputfile):
        """Fasta to Relaxed Phylip format."""
        AlignIO.convert(inputfile, "fasta",
                        outputfile, "phylip-relaxed")


# Make this explicit, then they show up in the API docs
__all__ = ("ETE3PAML",
           "PamlTest",
           "PhyML",
           "TreeViz",
           #"Phylip",
           "RelaxPhylip",
           )
