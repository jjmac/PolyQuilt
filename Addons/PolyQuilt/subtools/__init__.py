
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from .maintool_default import MainToolDefault
from .maintool_hold import MainToolHold
from .maintool_brush import MainToolBrush
from .maintool_lowpoly import MainToolLowPoly
from .maintool_knife import MainToolKnife
from .maintool_delete import MainToolDelete
from .maintool_extrude import MainToolExtrude
from .maintool_loopcut import MainToolLoopCut

maintools = {
    'MASTER'    : MainToolDefault ,
    'HOLD'      : MainToolHold ,
    'LOWPOLY'   : MainToolLowPoly ,
    'BRUSH'     : MainToolBrush ,
    'EXTRUDE'   : MainToolExtrude ,
    'KNIFE'     : MainToolKnife ,
    'DELETE'    : MainToolDelete ,
    'LOOPCUT'   : MainToolLoopCut ,
}
