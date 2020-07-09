# this file is part of pyliblzfse.
#
# Copyright (c) 2017-2020  Yogesh Khatri
# Copyright (c) 2016, 2017 Dima Krasner
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
from setuptools import setup, Extension

lzfse_dir = os.path.join('lzfse', 'src')
lzfse_srcs = [os.path.join(lzfse_dir, x) for x in os.listdir(lzfse_dir) if (x.endswith('.c') or x.endswith('.h')) and x != 'lzfse_main.c']

lzfse = Extension('liblzfse',
                   sources=lzfse_srcs + ['pylzfse.c', 'LICENSE.lzfse', 'COPYING', 'AUTHORS'],
                   extra_compile_args=['-std=c99'],
                   include_dirs=[lzfse_dir],
                   language='c')
                   
f = open('README', 'r')
description_from_readme = '<pre>' + f.read() + '</pre>'
f.close()

setup(name='pyliblzfse',
      version='0.4.0',
      license='MIT',
      author='Yogesh Khatri',
      author_email='yogesh@swiftforensics.com',
      description='Python bindings for the LZFSE reference implementation',
      long_description=description_from_readme,
      long_description_content_type='text/markdown',
      url='https://github.com/ydkhatri/pyliblzfse',
      ext_modules=[lzfse])
