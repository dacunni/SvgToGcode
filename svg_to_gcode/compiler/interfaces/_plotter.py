from svg_to_gcode.compiler.interfaces import Gcode
from svg_to_gcode import formulas


class Plotter(Gcode):
    """
        Plotter Gcode generator. Maps laser on/off interface to pen down/up.
    """

    def __init__(self):
        super().__init__()
        self._pen_down = False
        self._depth = 5

    def laser_off(self):
        # Plunge tool
        if self._pen_down:
            self._pen_down = False
            return f"G1 Z{self._depth};"

        return ''

    def set_laser_power(self, power):
        # Lift tool
        if not self._pen_down:
            self._pen_down = True
            return f"G1 Z{-self._depth};"
