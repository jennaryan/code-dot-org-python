import random as r

class Pen():
    """A pen can be given to any challenge Object to allow them to have
    turtle graphics like drawing capability. This has its own class
    to allow new challenges that could possibly combine elements of
    MazeChallenge with ArtistChallenge and such.
    """

    def __init__(self):
        self.on = True
        self.color = 'black'
        self.width = 7

    @staticmethod
    def random_color():
        return (r.random(),r.random(),r.random())

if __name__ == '__main__':
    print(Pen.random_color())
    print(Pen().random_color())
