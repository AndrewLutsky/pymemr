"""Main python file"""
import gzip
import argparse
from pathlib import Path
import psutil
import psutil
from rich.console import Console
from helper import SexpType, print_file_hex, print_file_raw, is_gzip

#
# Create a console object
console = Console()


def main():
    parser = argparse.ArgumentParser(description="Raw RData file reader")
    parser.add_argument("file", type=Path, help="Path to .RData file")
    parser.add_argument("debug", type=bool, help="Debugger mode")
    args = parser.parse_args()

    # Available memory in bytes
    available_bytes = psutil.virtual_memory().available
    print(f"{available_bytes / 1.e9:2f}")
    

    if not args.file.exists():
        console.print(f"[red]File not found:[/] {args.file}")
        return


    if args.debug:
        print(f"Printing raw file for {args.file}!")
        print_file_raw(args.file)
        print(f"Printing hex file for {args.file}!")
        print_file_hex(args.file)
if __name__ == "__main__":
    main()
