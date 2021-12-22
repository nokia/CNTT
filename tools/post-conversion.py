#!/bin/python3
####
# Copyright 2021 Nokia
# Licensed under the Apache License 2.0
# SPDX-License-Identifier: Apache-2.0
####
# A script to mass modify Anuket specification rst files after their conversoin from md. 

import argparse
import glob
import logging
import os
import re


def main():
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)
    idText = "A script to run after the conversion from md to rst."
    logger.info(idText)
    parser = argparse.ArgumentParser(description=idText)
    parser.add_argument('directory', default="",
                        help='The directory where all the .rst files should be processed.')
    parser.add_argument('--debug', action="store_true",
                        help='Print debug logs.')

    args = parser.parse_args()
    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Debug logging is ON")
    filePattern = "{}/*.rst".format(args.directory)
    logger.info("File pattern is {}".format(filePattern))
    fileList = glob.glob(filePattern)

    for filename in sorted(fileList):
        logger.info("Filename is {}".format(filename))
        images = {}
        fIn = open(filename, 'r')
        lineNumber = 0
        lines = fIn.readlines()
        fIn.close()
        for line in lines:
            #logger.debug("Line is {}".format(line))
            lineNumber = lineNumber + 1
            
            # .. |Figure 1-1: Scope of Reference Model| image:: ../figures/ch01_scope.png
            result = re.match('^\.\. \|(.*)\| image:: (.*)', line)
            if result:
                logger.debug("Match \'{}\' / \'{}\' / \'{}\'".format(line, result.group(2), result.group(1)))
                images[result.group(1)] = result.group(2)
        for key in images.keys():
            logger.debug("Key: {}".format(key))

        fOut = open(filename, 'w')
        for line in lines:
            # |Figure 1-1: Scope of Reference Model|
            result = re.match("^\|(.*)\|", line)
            if result:
                logger.debug("Image found: \'{}\'".format(result.group(1)))
                if result.group(1) in images.keys():
                    logger.debug("  Key found")
                    logger.debug("  Original line: {}".format(line))
                    line = ".. image:: {}\n   :alt: \"{}\"\n\n".format(images[result.group(1)], result.group(1))
                    logger.debug("  Modified line: {}".format(line))
                else:
                    logger.debug("  Key not found")
            result = re.match('^\.\. \|(.*)\| image:: (.*)', line)
            if result:
                logger.debug("Match \'{}\' / \'{}\' / \'{}\'".format(line, result.group(2), result.group(1)))
                line = ""
            fOut.writelines(line)
        fOut.close()


if __name__ == "__main__":
    main()
