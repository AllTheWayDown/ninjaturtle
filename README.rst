ninjaturtle
===========

WARNING: A work in progress currently.

A re-implementation of Python's turtle module, with some improvements.

Main improvements are:

 * timed-based animation model, turtles move same speed regardless of CPU speeds
 * animation in separate engine for easier use in game/simulation loops
 * faster maths, including C acceleration
 * unit tests and cleaner design for further extending
 * pluggable output rendering:

   * builtin Tk renderer reuses stdlib's turtle renderer
   * companion library Turgles provides fast OpenGL renderer
   * stdout renderer for debugging
   * can be headless for pure simulation


Other goals/ideas
-----------------

Other renderering backends: svg, gif, network


System Requirements
-------------------

python 2.6/2.7/3.2/3.3/PyPy

On linux systems, you may need to install python-tk as well.

If you want to use the Turgles OpenGL renderer (encouraged), then you'll need to
install that also. See http://github.com/AllTheWayDown/turgles for details

Running
-------

Currently there are two demo programs that create a single turtle. To run, use

.. code::

    python -i tk_demo.py

or

.. code::

    python -i gl_demo.py

You then have a python prompt with a turtle ``t`` that you can control as normal.
e.g. t.forward(100), t.left(90), etc
