#!/usr/bin/python
import string

if __name__ == "__main__":
    import sys

    template_file = sys.argv[1]

    with open(template_file) as f:
        data = f.read()

    template = string.Template(data)
    template_mapping = {}

    for item in sys.argv[2:]:
        # item is in the following form:  KEY=VALUE
        print("-> Current replacer %s" % item)
        key, value = item.split("=", 1)
        template_mapping[key] = value

    print("-> Using mapping: %s" % str(template_mapping))
    result = template.substitute(template_mapping)
    print("-----\n")
    print(result)
