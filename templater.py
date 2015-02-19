#!/usr/bin/python
import string
import os
import sys

from optparse import OptionParser

class Templater(object):

    def __init__(self, filename, arguments=None):
        self._filename = filename
        self._template = self._template_from_file(filename)
        self._arguments = arguments

    def set_arguments(self, arguments):
        self._arguments = arguments

    def get_result(self):
        template_mapping = self._get_template_mapping()
        return self._template.substitute(template_mapping)

    def _get_template_mapping(self):
        """ Create a mapping from the input arguments which are in KEY=VALUE form. """
        if hasattr(self._arguments, "keys"):
            return self._arguments
        else:
            return dict([item.split("=", 1) for item in self._arguments])

    def _template_from_file(self, filename):
        """ Create a Template from a given file. """
        with open(options.template_file) as f:
            return string.Template(f.read())


def process_options():
    parser = OptionParser()
    parser.add_option("-t", "--template", dest="template_file",
                      help="Input template file")
    parser.add_option("-o", "--output", dest="output",
                      help="Output file (if not specified then the stdout will be used")

    (options, args) = parser.parse_args()

    if not options.template_file:
        parser.print_help()
        exit(1)

    if not os.path.isfile(options.template_file):
        sys.stderr.write("Invalid input template file: %s" % options.template_file)
        exit(1)

    # filter out arguments without '='
    filtered_args = []
    for item in args:
        if "=" not in item:
            sys.stderr.write("Skipping invalid argument '%s'\n" % (item))
            continue

        filtered_args.append(item)

    return (options, filtered_args)


def write_result(result, output=None):
    if output:
        with open(output, "w") as f:
            f.write(result)
    else:
        print(result)


if __name__ == "__main__":
    options, args = process_options()
    result = Templater(options.template_file, args).get_result()
    write_result(result, options.output)
