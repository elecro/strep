Simple Template REPlace (STREP)
========

This nifty little tool accepts a template file and
replaces the variables in it with the given values
returning the result on the stdout (by default).


In the template file one can use variables in the
form `$var` or `${var}`.


The values for the variables are given to the tool
as command line arguments in the `KEY=VALUE` form.

So the basic usage is something like this:
```bash
$ python strep.py -t <template file> KEY=VALUE ...
```


Reading the template file from stdin is also supported
just use the `-t -` argument. Example:
```bash
$ echo 'Hello $thing' | python strep.py -t - thing=World
Hello world
```

(Note that the string was given between `'` characters to
avoid echo's (or bash's?) variable replacment.



To specify the output file (instead of the stdout), use
the `-o <output file>` option. Example:
```bash
$ python strep.py -t file.template KEY=VALUE -o file.result
```
