class Challenge():

    def __setattr__(self,name,value):
        if name == 'title':
            self.canvas.title = value
        if name == 'speed':
            self.canvas.speed = value
        super().__setattr__(name,value)
