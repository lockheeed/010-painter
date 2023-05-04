from .exceptions import *

import os
import re


class GraphData(object):
    def __init__(self, data: str):
        self.data = data
        
        self.values = []
        self.cycles = 0
        self.name = None
        self.color = 'black'
        self.name = '?'

        self.parse()

    def parse(self):
        if not re.fullmatch(r'([01]{2}\ )*(\w*=[^\ ]*\ ?)*', self.data):
            raise InvalidDataFormatError(self.data)
        
        match = re.search('(([01][01]\ )*)', self.data)
        self.values = [int(v) for v in match.group()[:-1].replace(' ', '')]
        self.cycles = len(self.values)//2

        for attr, val in map(lambda x: x.split('='), self.data[match.span()[1]:].split()):
            setattr(self, attr, val)


class Parser(object):
    def __init__(self):
        pass

    def load(self, path: str):
        graphs = []

        if not os.path.exists(path):
            raise FileDoentExist(path)
        
        for line in open(path, 'r').readlines():
            line = line.strip()
            if line:
                graphs.append(GraphData(line))
            
        if any(graphs[i].cycles != graphs[i+1].cycles for i in range(len(graphs) - 1)):
            raise VariableGrapthLenError
    
        return graphs, graphs[0].cycles