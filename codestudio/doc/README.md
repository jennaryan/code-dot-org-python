codestudio
==========

A Python module to supplement and expand studio.code.org learning
activities and [code-dot-org](http://github.com/code-dot-org) with a focus
on initially typing out code 'ports' of the JavaScript from 'Show Code'
in each activity.

If you are a student you probably want to just fork
[code-org-example](http://github.com/skilstak/code-org-example), (which
includes this `codestudio` module as a submodule), instead of forking
this one.

This is a Python module so it can simply be forked and/or included in
other projects simply as a submodule. Either of these should work in
your own repos:

```
git submodule add git@github.com:skilstak/codestudio.git`
git submodule add http://github.com/skilstak/codestudio.git`
```

For testing and other distribution forms see the
[codestudio-project](http://github.com/skilstak/codestudio-project) repo.

FAQ
===

**Why not round off the large floating point numbers written to the json
files when saving a challenge?**

Not only does this precision allow for implementation on other visualization
systems later, it makes it more difficult for students and others to 'hack'
solutions of their own rather than just writing the Python to create them.
Any language that handles floating point math the same way should be able to
use these challenge solutions.

**Why all the `to_json` and `from_json` instead of `jsonpickle` and the
like?**

Mostly because even though we could bundle those dependencies in this module
we wanted to keep it mostly vanilla Python, which makes for a good example
itself of what those learning Python can do without the extra steps of
getting external libraries.

In other words, we wanted `codestudio` itself to serve as class material
that can be reconstructed entirely step-by-step to introduce more complex
module/package development to those new to it.
