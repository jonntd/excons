# Copyright (C) 2015~  Gaetan Guidet
#
# This file is part of excons.
#
# excons is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 2.1 of the License, or (at
# your option) any later version.
#
# excons is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301,
# USA.

from SCons.Script import *
import excons
import os

def Require(ilmthread=None, iexmath=None, python=None):
   
   if ilmthread is None:
      ilmthread = (excons.GetArgument("ilmbase-thread", 1, int) != 0)

   if iexmath is None:
      iexmath = (excons.GetArgument("ilmbase-iexmath", 1, int) != 0)

   if python is None:
      python = (excons.GetArgument("ilmbase-python", 0, int) != 0)

   def _RealRequire(env):
      ilmbase_libsuffix = excons.GetArgument("ilmbase-libsuffix", "")
      
      # Add python bindings first
      if python:
         pyilmbase_inc, pyilmbase_lib = excons.GetDirs("ilmbase-python")
         
         pyilmbase_libsuffix = excons.GetArgument("ilmbase-python-libsuffix", ilmbase_libsuffix)
         
         if pyilmbase_inc:
            if not pyilmbase_inc.endswith("OpenEXR"):
               pyilmbase_inc += "/OpenEXR"
            env.Append(CPPPATH=[pyilmbase_inc, os.path.dirname(pyilmbase_inc)])
         
         if pyilmbase_lib:
            env.Append(LIBPATH=[pyilmbase_lib])
         
         env.Append(LIBS=["PyImath" + pyilmbase_libsuffix])
      
      
      ilmbase_inc, ilmbase_lib = excons.GetDirs("ilmbase")
      
      static = (excons.GetArgument("ilmbase-static", 0, int) != 0)

      if ilmbase_inc and not ilmbase_inc.endswith("OpenEXR"):
         ilmbase_inc += "/OpenEXR"
      
      libs = []
      if ilmthread:
         libs.append("IlmThread")
      libs.append("Imath")
      if iexmath:
         libs.append("IexMath")
      libs.append("Iex")
      libs.append("Half")
      
      if ilmbase_libsuffix:
         libs = map(lambda x: x+ilmbase_libsuffix, libs)
      
      if sys.platform == "win32":
         if not static:
            env.Append(CPPDEFINES=["OPENEXR_DLL"])
      
      if ilmbase_inc:
         env.Append(CPPPATH=[ilmbase_inc, os.path.dirname(ilmbase_inc)])
      
      if ilmbase_lib:
         env.Append(LIBPATH=[ilmbase_lib])
      
      env.Append(LIBS=libs)
   
   return _RealRequire
