from modules import exceptions
from modules import parser
from modules import painter

import sys


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise exceptions.NoParamsError

    graph_data, cycles = parser.Parser().load(sys.argv[1])
    painter = painter.Painter(graph_data, cycles)
    painter.draw()