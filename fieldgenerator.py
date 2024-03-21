class FieldGenerator:
    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        with open(self.filepath, "r") as f:
            # Leggi la prima riga
            header = f.readline().split()

            # Assegna le variabili
            self.COL = int(header[0])
            self.ROW = int(header[1])
            self.NUM_G = int(header[2])
            self.NUM_S = int(header[3])
            self.NUM_T = int(header[4])

            self.golden_points = set()
            for _ in range(self.NUM_G):
                line = f.readline().split()
                x, y = int(line[0]), int(line[1])
                self.golden_points.add((x, y))
        '''
            # Leggi le informazioni sulle piastrelle
            self.tiles = {}
            for _ in range(self.NUM_T):
                line = f.readline().split()
                tile_id, cost, quantity = line[0], int(line[1]), int(line[2])
                self.tiles[tile_id] = Tile(tile_id, cost, quantity)
        '''
        return self