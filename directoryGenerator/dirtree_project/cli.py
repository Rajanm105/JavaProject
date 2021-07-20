import argparse
import pathlib
import sys

from . import __version__
from .dirtree import DirectoryTree


def main():
    args = parse_cmd_line_arguments()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print("The specified root directory doesn't exist")
        sys.exit()
    tree = DirectoryTree(root_dir,dir_only=args.dir_only)
    tree.generate()

def parse_cmd_line_arguments():
    parser = argparse.ArgumentParser(
        prog="tree",
        description="DIR Tree, a directory tree generator",
        epilog="Thanks for using DIR Tree",
    )
    parser.version = f"DIR Tree v{__version__}"
    parser.add_argument("-v", "--version", action="version")
    parser.add_argument(
        "-d",
        "--dir-only",
        action="store_true",
        help="Generate a  directory-only tree",
    )
    return parser.parse_args()
