JavaScript-to-Python Port Examples
==================================

Often coding is about creative expression, but not always. Sometimes the
working world demands coders &mdash; especially juniors &mdash; to create
something based on a given set of requirements.  Porting code created by
dragging and dropping Blockly on [studio.code.org](http://studio.code.org)
to typed Python based on the JavaScript revealed by the  *Show Code*
button builds on the fun and skills while learning to 'code to spec' in
a third programming language. 

This folder contains a few example ports to help students remember
the format and specification to receive full credit for their ports.

Files are named after their corresponding URLs from
[learn.code.org](http://learn.code.org).

Students save their work into a `code-org` repo so it can be checked
consistently, even automatically.

Detailed descriptions of the sections of each ported Python file are
embedded as comments in these examples.

As students progress in their porting to more complicated challenges that
require use and creation of functions they put them into their own verion
of the `mymod` module file. `random_color()` has been added by default.

Future
======

Eventually these ports will use the
[`codestudio`](http://github.com/skilstak/codestudio) module designed in
collaboration with the [code-dot-org](http://github.com/code-dot-org)
team to provide a cleaner API for JavaScript -> Python ports. Even
though the Python `turtle` module provides an almost direct correlation
to the Artist challenges `codestudio` will supplement it using the same
domain language as from the challenges as well create Maze and Farmer
equivalents where there is currently no direct port path for these.