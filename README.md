*Introduction to Computer Science*<br>Code.org in Python
========================================================

This repo contains the puzzles from the [Introduction to Computer Science
on code.org](http://learn.code.org/s/1) written in Python3 suitable for
any learning environment requiring only vanilla Python3 to be installed.
This includes the default Raspberry Pi setup. It was created to supplement
or replace the Blockly activities for those ready to ***actually*** write 
 code. [Students 'create' code with Blockly but they certainly don't
'write' it.]

Students [fork this
repo](http://github.com/skilstak/code-dot-org-python/fork) or [download
the zip](http://github.com/skilstak/code-dot-org-python/archive/master.zip) and complete the puzzles with a vanilla
installation of Python on their local computer. The results of their
code solutions is checked in real-time against a saved solution (in JSON
format) in the `puzzles` directory. Detailed descriptions of the sections
of each ported Python file are embedded as comments in these examples.  If
students get stuck they can refer to the [solutions](/solutions). Teachers
can easily create additional puzzles for which the solutions are not
available for more formal assessments if needed.

As students progress in their porting to more complicated puzzles that
require use and creation of functions they put them into their own
version of the [mymod.py](mymod.py) module file.

Finally students can create their own puzzles for themselves
and others by contributing to the [extra collection](/extra), which may
eventually become its own site to students to puzzles each other.

The [codestudio](/codestudio) library module on which these puzzles
are based contains tools to help create new puzzles easily as well as
visualize puzzles and solutions. The steps to create your own puzzles
are outlined in [extras](/extra) with examples. The module itself
has been designed to serve as a basic for learning Python modules,
object-oriented-programming, packaging, geometry/trigonometry, domain
modeling, separation of concerns, exception handling, test-driven
development, basic GUI development, cross-platform audio programming,
JSON and more.
