from .common import GetMonitorResolution, VERSION 

from pydraw import *


TITLE: str = F"010 painter {VERSION}"

X_PADDING: int = 10
Y_PADDING: int = 5

Y_DIST: int = 10
CYCLE_WIDTH: int = 54 # multiple of two

FONT_SIZE: int = 28
ENUM_FONT_SIZE: int = 12
FONT_RATIO: int = 1.7

Y_OFFSET: int = Y_DIST + FONT_SIZE
AMPLITUDE: float = 0.72
MAX_WIDTH, MAX_HEIGHT = GetMonitorResolution(0.85)
FPS: int = 5
PYDRAW_BORDER: int = 15


class Painter(object):
    def __init__(self, graphs, cycles: int):
        self.graphs = graphs
        self.cycles = cycles
        self.graph_x_offset = int(max(len(graph.name) for graph in self.graphs) * FONT_SIZE / FONT_RATIO) + X_PADDING

        width = self.graph_x_offset + cycles * CYCLE_WIDTH + X_PADDING*3
        height = Y_PADDING * 2 + Y_OFFSET * (len(self.graphs) + 1)
        
        width = min(MAX_WIDTH, width)
        height = min(MAX_HEIGHT, height)

        # TODO solve problem with big graphs
        self.screen = Screen(width, height, TITLE)
        self.screen._screen.screensize(1, 1)

        self.draw_markup()
        self.draw_graph()

    def draw_markup(self):
        # Draw cycle numbers
        x, y = X_PADDING + self.graph_x_offset + CYCLE_WIDTH//2, Y_PADDING

        for i in range(self.cycles):
            Text(self.screen, str(i), Location(x, y), size=ENUM_FONT_SIZE)
            x += CYCLE_WIDTH

        # Draw graphs titles
        x, y = X_PADDING, Y_PADDING + Y_DIST + ENUM_FONT_SIZE

        for graph in self.graphs:
            text = Text(self.screen, 
                        getattr(graph, 'name'), 
                        Location(x, y), 
                        size=FONT_SIZE, 
                        font='Roboto Mono')

            y += Y_OFFSET

        self.graph_x_offset += X_PADDING

        # Draw horizontal lines
        x, y = self.graph_x_offset, Y_PADDING + Y_OFFSET + ENUM_FONT_SIZE
        for graph in self.graphs:
            Line(self.screen, 
                 Location(x, y) ,
                 Location(x + self.cycles * CYCLE_WIDTH, y), 
                 thickness=1)
            
            y += FONT_SIZE + Y_DIST

        # Draw vertical dash lines for splitting the cycles
        x, y = self.graph_x_offset, Y_PADDING + ENUM_FONT_SIZE
        for i in range(1, self.cycles, 1):
            Line(self.screen, 
                 Location(x + CYCLE_WIDTH*i, y), 
                 Location(x + CYCLE_WIDTH*i, y + (len(self.graphs))*Y_OFFSET), 
                 dashes=1)

        self.width = x + CYCLE_WIDTH
        self.height = y + (len(self.graphs) + 1)*FONT_SIZE

    def draw_graph(self):
        prev_state = [graph.values[0] for graph in self.graphs]
        
        for c in range(self.cycles*2):
            for g in range(len(self.graphs)):
                graph_level = (1 - AMPLITUDE) if self.graphs[g].values[c] else 1

                if prev_state[g] != self.graphs[g].values[c]:                   
                    Line(self.screen, 
                         Location(self.graph_x_offset, Y_PADDING + Y_OFFSET*g + Y_OFFSET*(1-AMPLITUDE) + ENUM_FONT_SIZE), 
                         Location(self.graph_x_offset, Y_PADDING + Y_OFFSET*(g+1) + ENUM_FONT_SIZE), 
                         color=Color(getattr(self.graphs[g], 'color')), 
                         thickness=3)

                y = Y_PADDING + Y_OFFSET*g + Y_OFFSET*graph_level + ENUM_FONT_SIZE
                Line(self.screen, 
                     Location(self.graph_x_offset, y), 
                     Location(self.graph_x_offset + CYCLE_WIDTH//2, y), 
                     color=Color(getattr(self.graphs[g], 'color')), 
                     thickness=3)

                prev_state[g] = self.graphs[g].values[c]

            self.graph_x_offset += CYCLE_WIDTH//2

    def draw(self):
        while True:
            try:
                self.screen.update()
            except Exception:
                return
            
            self.screen.sleep(1 / FPS)