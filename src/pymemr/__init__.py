"""Main python file"""
import gzip
import argparse
from enum import IntEnum
from pathlib import Path
from rich.console import Console


# Hard Coded SEXP types
class SexpType(IntEnum):
    """ Class that inherits from IntEnum that lets you treet NILSXP as 0
    itself or SYMSXP as 1
    """

    NILSXP      = 0   # nil = NULL
    SYMSXP      = 1   # symbols
    LISTSXP     = 2   # lists of dotted pairs
    CLOSXP      = 3   # closures
    ENVSXP      = 4   # environments
    PROMSXP     = 5   # promises: [un]evaluated closure arguments
    LANGSXP     = 6   # language constructs (special lists)
    SPECIALSXP  = 7   # special forms
    BUILTINSXP  = 8   # builtin non-special forms
    CHARSXP     = 9   # "scalar" string type (internal only)
    LGLSXP      = 10  # logical vectors
    # 11 and 12 were factors and ordered factors in the 1990s
    INTSXP      = 13  # integer vectors
    REALSXP     = 14  # real variables
    CPLXSXP     = 15  # complex variables
    STRSXP      = 16  # string vectors
    DOTSXP      = 17  # dot-dot-dot object
    ANYSXP      = 18  # "any" args for symbol registration
    VECSXP      = 19  # generic vectors
    EXPRSXP     = 20  # expressions vectors
    BCODESXP    = 21  # byte code
    EXTPTRSXP   = 22  # external pointer
    WEAKREFSXP  = 23  # weak reference
    RAWSXP      = 24  # raw bytes
    OBJSXP      = 25  # object, non-vector
    S4SXP       = 25  # same as OBJSXP, retained for back compatibility

    # For internal memory management / debugging
    NEWSXP      = 30  # fresh node created in new page
    FREESXP     = 31  # node released by GC

    # Function type catch-all
    FUNSXP      = 99  # Closure or Builtin or Special



# Create a console object
console = Console()

GZIP_MAGIC = b"\x1f\x8b"

def is_gzip(filepath: Path):
    """Function that tells you if file is gzipped or not"""
    with open(filepath, 'rb') as f:
        head = f.read(2)
        if head == GZIP_MAGIC:
            return True
        f.close()

    return False




def main():
    parser = argparse.ArgumentParser(description="Raw RData file reader")
    parser.add_argument("file", type=Path, help="Path to .RData file")
    args = parser.parse_args()

    if not args.file.exists():
        console.print(f"[red]File not found:[/] {args.file}")
        return

if __name__ == "__main__":
    main()
