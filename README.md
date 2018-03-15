rsort
=====

Simple utility that performs [real sorting][1].

Compat
------

Built for python 3 (py2 untested).

#### Python Dependencies

  * [natsort][2]

Installing
----------


#### Linux

    # Make sure $HOME/.local/bin is in your PATH
    #   or install rsort to a PATH directory
    chmod +x src/rsort.py
    ln -s $(readlink -f src/rsort.py) $HOME/.local/bin/rsort


Example
-------

    # See examples/README.md
    rsort "*.png"


[1]: http://natsort.readthedocs.io/en/master/realsorted.html
[2]: https://pypi.python.org/pypi/natsort
