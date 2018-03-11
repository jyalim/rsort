rsort example
=============

The three txt files in this directory show the results of running a
vanilla `ls`, `ls --sort=version`, and `rsort`.

Note that `rsort` appropriately sorts the files based on the `F` token,
whereas the alternatives fail to (search the file for `e-11`).

That is, `7431764629e-11` is the smallest `F` token value, but only
rsort captures this.

version
-------

#### ls 

    ls (GNU coreutils) 8.25
    Copyright (C) 2016 Free Software Foundation, Inc.
    License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.

    Written by Richard M. Stallman and David MacKenzie.

#### rsort

    Version 0.0.0
