#!/usr/bin/python
import string
import os

from optparse import OptionParser


def build_template_mapping(arguments):
    """ Create a mapping from the input arguments which are in KEY=VALUE form. """
    return dict([item.split("=", 1) for item in arguments])


def template_from_file(filename):
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

    return (options, args)


def write_result(result):
    if options.output:
        with open(options.output, "w") as f:
            f.write(result)
    else:
        print(result)


if __name__ == "__main__":
    options, args = process_options()

    template_mapping = build_template_mapping(args)
    template = template_from_file(options.template_file)
    result = template.substitute(template_mapping)

    write_result(result)
