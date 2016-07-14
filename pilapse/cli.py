"""Handles the Command Line Interface part of Pilapse."""

from . import __version__
from .exceptions import ParameterException, ParameterWarning
import argparse


DESCRIPTION = ("Takes stills using a connected Raspberry Pi Camera")
version = ".".join([str(x) for x in __version__])  # Create version str


def setup_parser():
    """Set up an argparse parser and return it."""
    parser = argparse.ArgumentParser(prog="pilapse",
                                     description=DESCRIPTION)

    parser.add_argument("-v", "--version",
                        action="version",
                        version="%(prog)s " + version)

    parser.add_argument("output_folder",
                        help="The folder in which stills are saved.")

    parser.add_argument("-n", "--name",
                        dest="name",
                        help=("Base name to use for stills."
                              " Datetime info is added automatically. "
                              "Default: 'pilapse'"),
                        default="pilapse")

    parser.add_argument("-i", "--iso",
                        dest="iso",
                        help=("Sets the ISO value of the camera. "
                              "Guide: 100-200 for daytime, "
                              "400-800 for nighttime"),
                        type=int,
                        default=100)

    # ** Crontab **
    parser.add_argument("--install",
                        dest="install",
                        help=("Whether to install the Pilapse program in a "
                              "crontab. Use with --interval."),
                        action="store_true")

    parser.add_argument("--interval",
                        dest="interval",
                        help=("The interval at which timelapse stills are "
                              "taken. Use with --install."),
                        type=int)

    parser.add_argument("--cronstring",
                        dest="cronstring",
                        help=("Alternative to --interval. This string will "
                              "be used as the cron entry if set."))

    return parser


def check_args(args):
    """
    Check that the combination of CLI-parameters is valid.

    Raises ParameterException or ParameterWarning if invalid
    parameters are found.
    """
    # ** Crontab **
    # --install must have a --interval or --cronstring
    if args.install and not (args.interval or args.cronstring):
        raise ParameterException("--install must be used with either "
                                 "--interval or --cronstring")

    if args.interval and not args.install:
        raise ParameterWarning("--interval must be used with --install "
                               "to have an effect. Parameter ignored.")

    if args.cronstring and not args.install:
        raise ParameterWarning("--cronstring must be used with --install "
                               "to have an effect. Parameter ignored.")
