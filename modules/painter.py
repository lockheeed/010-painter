from .common import VERSION

from pydraw import *


class DrawConst:
    title: str = F"010 painter {VERSION}"
    x_padding: int = 15
    y_padding: int = 1

    y_dist: int = 15
    cycle_width: int = 80
    font_size: int = 34
    enum_fonst_size: int = 14
    font_ratio: int = 1.7
    amplitude: float = 0.72
    
    fps: int = 5
    y_offset = y_dist + font_size


class Painter(object):
    def __init__(self, graphs, cycles: int):
        self.graphs = graphs
        self.cycles = cycles
        self.graph_x_offset = int(max(len(graph.name) for graph in self.graphs) * DrawConst.font_size / DrawConst.font_ratio)

        width = DrawConst.x_padding * 2 + cycles * DrawConst.cycle_width + self.graph_x_offset
        height = DrawConst.y_padding * 2 + DrawConst.y_offset * (len(self.graphs) + 1)

        self.screen = Screen(width, height, DrawConst.title)
        self.draw_markup()
        self.draw_graph()

    def draw_markup(self):
        # Draw cycle numbers
        x, y = DrawConst.x_padding + self.graph_x_offset + DrawConst.cycle_width//2, DrawConst.y_padding

        for i in range(self.cycles):
            Text(self.screen, str(i), Location(x, y), size=DrawConst.enum_fonst_size)
            x += DrawConst.cycle_width

        # Draw graphs titles
        x, y = DrawConst.x_padding, DrawConst.y_padding + DrawConst.y_dist + DrawConst.enum_fonst_size

        for graph in self.graphs:
            text = Text(self.screen, 
                        getattr(graph, 'name'), 
                        Location(x, y), 
                        size=DrawConst.font_size, 
                        font='Roboto Mono')

            y += DrawConst.y_offset

        self.graph_x_offset += DrawConst.x_padding

        # Draw horizontal lines
        x, y = self.graph_x_offset, DrawConst.y_padding + DrawConst.y_offset + DrawConst.enum_fonst_size
        for graph in self.graphs:
            Line(self.screen, 
                 Location(x, y) ,
                 Location(x + self.cycles * DrawConst.cycle_width, y), 
                 thickness=1)
            
            y += DrawConst.font_size + DrawConst.y_dist

        # Draw vertical dash lines for splitting the cycles
        x, y = self.graph_x_offset, DrawConst.y_padding + DrawConst.enum_fonst_size
        for i in range(1, self.cycles, 1):
            Line(self.screen, 
                 Location(x + DrawConst.cycle_width*i, y), 
                 Location(x + DrawConst.cycle_width*i, y + (len(self.graphs))*DrawConst.y_offset), 
                 dashes=1)

        self.width = x + DrawConst.cycle_width
        self.height = y + (len(self.graphs) + 1)*DrawConst.font_size

    def draw_graph(self):
        prev_state = [graph.values[0] for graph in self.graphs]
        
        for c in range(self.cycles*2):
            for g in range(len(self.graphs)):
                graph_level = (1 - DrawConst.amplitude) if self.graphs[g].values[c] else 1

                if prev_state[g] != self.graphs[g].values[c]:                   
                    Line(self.screen, 
                         Location(self.graph_x_offset, DrawConst.y_padding + DrawConst.y_offset*g + DrawConst.y_offset*(1-DrawConst.amplitude) + DrawConst.enum_fonst_size), 
                         Location(self.graph_x_offset, DrawConst.y_padding + DrawConst.y_offset*(g+1) + DrawConst.enum_fonst_size), 
                         color=Color(getattr(self.graphs[g], 'color')), 
                         thickness=3)

                y = DrawConst.y_padding + DrawConst.y_offset*g + DrawConst.y_offset*graph_level + DrawConst.enum_fonst_size
                Line(self.screen, 
                     Location(self.graph_x_offset, y), 
                     Location(self.graph_x_offset + DrawConst.cycle_width//2, y), 
                     color=Color(getattr(self.graphs[g], 'color')), 
                     thickness=3)

                prev_state[g] = self.graphs[g].values[c]

            self.graph_x_offset += DrawConst.cycle_width//2

    def draw(self):
        while True:
            try:
                self.screen.update()
            except Exception:
                return
            
            self.screen.sleep(1 / DrawConst.fps)