#!/usr/bin/python

class Block:
    def __init__(self,blocktype,blockname):
        self.lines = []
        self.type = blocktype
        self.name = blockname
        
def parse_file(path):
    f = open(path)
    blocks = {}
    curblock = []
    for line in f.readlines():
        if line.startswith('%'):
            tag = line[1:].strip()
            blocktype, blockname = tag.split(' ',1)
            curblock = Block(blocktype,blockname)
            blocks[tag] = curblock
        else:
            curblock.lines.append(line.strip())
    f.close()
    return blocks

if __name__ == '__main__':
    import sys
    for arg in sys.argv[1:]:
        print parse_file(open(arg))
