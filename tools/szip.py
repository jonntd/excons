# Copyright (C) 2014  Gaetan Guidet
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

def Require(env):
  szip_inc, szip_lib = excons.GetDirs("szip")
  
  if szip_inc:
    env.Append(CPPPATH=[szip_inc])
  
  if szip_lib:
    env.Append(LIBPATH=[szip_lib])
  
  if excons.GetArgument("szip-static", 0, int) == 0:
    env.Append(CPPDEFINES=["SZ_BUILT_AS_DYNAMIC_LIB"])
  
  szip_libname = excons.GetArgument("szip-libname", None)
  if not szip_libname:
    szip_libsuffix = excons.GetArgument("szip_libsuffix", "")
    szip_libname = "%s%s" % (("sz" if sys.platform != "win32" else "libszip"), szip_libsuffix)
  
  env.Append(LIBS=[szip_libname])
