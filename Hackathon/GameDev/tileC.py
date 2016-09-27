import pygame, Funk

class Tile(pygame.Rect):

    List = []
    width, height = 32, 32
    total_tiles = 1
    H, V = 1, 22

    invalids = [1,22,23,25,26,28,29,32,33,34,35,36,37,38,39,40,41,42,45,47,47,48,50,51,66,67,69,70,72,73,75,76,77,78
                ,79,80,81,82,83,84,85,86,88,89,91,92,94,95,97,98,100,101,103,105,106,107,110,111,119,120,121,132,133,135,136
                ,137,138,139,140,142,147,149,151,152,154,155,157,176,177,179,180,182,183,186,187,199,201,202,204
                ,205,206,207,208,209,210,211,212,213,214,215,217,218,221,223,224,226,227,228,229,231,232
                ,233,234,237,239,243,246,250,251,261,262,265,267,292,293,294,295,296,297,298,299,301,303,304,99
               ,102,104,108,141,143,145,146,150,158,145,150,167,168,169,170,171,172,172,174,245,246,240,268,300,306,302,305
               ,308,22,287,44,198,220,242,264,286]


    def __init__(self, x, y, Type):

        self.parent = None
        self.H, self.G, self.F = 0,0,0

        self.type = Type
        self.number = Tile.total_tiles
        Tile.total_tiles += 1

        if Type == 'empty':
            self.walkable = True
        else:
            self.walkable = False

        pygame.Rect.__init__(self, (x, y) , (Tile.width, Tile.height) )

        Tile.List.append(self)

    @staticmethod
    def get_tile(number):
        for tile in Tile.List:
            if tile.number == number:
                return tile

    @staticmethod
    def draw_tiles(screen):
        half = Tile.width / 2

        for tile in Tile.List:

            pass

            #if not(tile.type == 'empty'):
                #pygame.draw.rect(screen, [40, 40, 40], tile )

            #Funk.text_to_screen(screen, tile.number, tile.x, tile.y)