# encoding=UTF-8

# Copyright © 2013-2017 Jakub Wilk <jwilk@jwilk.net>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

'''
*injunctive* provides Perl6 style junctions_ (``all``, ``any``, ``one``, ``none``).

.. _junctions: https://www.perl6.org/archive/doc/design/exe/E06.html#The%20Wonderful%20World%20of%20Junctions
'''

import distutils.core

try:
    import distutils644
except ImportError:
    pass
else:
    distutils644.install()

b''  # Python >= 2.6 is required

classifiers = '''
Development Status :: 3 - Alpha
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 3
'''.strip().splitlines()

distutils.core.setup(
    name='injunctive',
    version='0.1',
    license='MIT',
    description='Perl6 style junctions',
    long_description=__doc__.strip(),
    classifiers=classifiers,
    url='https://github.com/jwilk/python-injunctive',
    author='Jakub Wilk',
    author_email='jwilk@jwilk.net',
    py_modules=['injunctive']
)

# vim:ts=4 sts=4 sw=4 et
