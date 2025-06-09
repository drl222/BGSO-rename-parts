# BGSO-rename-parts

This is a script that takes the part files outputted by MuseScore and renames them in a way that's a little more convenient for the BGSO.

To run, download the Python file from this repository (and Python itself, if you don't already have it). In the command line, run:

```
python BGSO_rename_parts.py [name of the folder containing all the files you want renamed]
```

All files with a hyphen in their names will have what's before the hyphen swapped with what's after the hyphen (e.g. `SuperMario-Flute_1.pdf` becomes `Flute_1-SuperMario.pdf` - and running the script a second time will swap it back). All filenames without a hyphen in them will have an underscore prepended to them if there isn't an initial underscore already. This lets these files (which for our purposes are usually things like the conductor's score or the rendered midi audio track) be sorted at the top, above all the other files, when sorting alphabetically.
