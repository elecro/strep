#!/usr/bin/python
import string
import os


if __name__ == "__main__":
    import sys
    from optparse import OptionParser

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

    with open(options.template_file) as f:
        data = f.read()

    template = string.Template(data)
    template_mapping = {}

    for item in args:
        # item is in the following form:  KEY=VALUE
        print("-> Current replacer %s" % item)
        key, value = item.split("=", 1)
        template_mapping[key] = value

    print("-> Using mapping: %s" % str(template_mapping))
    result = template.substitute(template_mapping)
    print("-----\n")

    if options.output:
        with open(options.output, "w") as f:
            f.write(result)
    else:
        print(result)
