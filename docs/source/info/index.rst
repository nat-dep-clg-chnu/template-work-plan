..
   Copyright (c) 2022, VVKo

===========
КОРОТКА ДОВІДКА ПРО ЦИКЛОВУ КОМІСІЮ
===========

Ласкаво просимо до раю

.. tikz:: [>=latex',dotted,thick] \draw[->] (0,0) -- (1,1) -- (1,0)
   -- (2,0);
   :libs: arrows

.. plot::
   :format: python
   :align: center
   :scale: 75

   import matplotlib.pyplot as plt
   from matplotlib import cm
   from mpl_toolkits.mplot3d import axes3d

   fig = plt.figure()
   ax = fig.gca(projection='3d')
   X, Y, Z = axes3d.get_test_data(0.005)
   ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
   cset = ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
   cset = ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
   cset = ax.contourf(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)

   ax.set_xlabel('X'); ax.set_xlim(-40, 40)
   ax.set_ylabel('Y'); ax.set_ylim(-40, 40)
   ax.set_zlabel('Z'); ax.set_zlim(-100, 100)

   plt.show()


Дуже страшна формула :math:`a^2 + b^2 = c^2`.

.. math::
   :nowrap:

   \begin{eqnarray}
      y    & = & ax^2 + bx + c \\
      f(x) & = & x^2 + 2xy + y^2
   \end{eqnarray}

Sphinx provides several different types of admonitions.

``topic``
=========

.. topic:: This is a topic.

   This is what admonitions are a special case of, according to the docutils
   documentation.

``admonition``
==============

.. admonition:: The one with the custom titles

   It's got a certain charm to it.

``attention``
=============

.. attention::

   Climate change is real.

``caution``
===========

.. caution::

   Cliff ahead: Don't drive off it.

``danger``
==========

.. danger::

   Mad scientist at work!

``error``
=========

.. error::

   Does not compute.

``hint``
========

.. hint::

   Insulators insulate, until they are subject to ______ voltage.

``important``
=============

.. important::

   Tech is not neutral, nor is it apolitical.

``note``
========

.. note::

   This is a note.

``seealso``
===========

.. seealso::

   Other relevant information.

``tip``
=======

.. tip::

   25% if the service is good.

``todo``
========

.. todo::

   This needs the ``sphinx.ext.todo`` extension.

``warning``
===========

.. warning::

   Reader discretion is strongly advised.
