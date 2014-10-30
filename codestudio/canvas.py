import tkinter as tk

class Canvas(tk.Canvas):
    N = 0
    S = 180
    E = 90
    W = 270

    def __init__(self,master=None):
        self.master = master if master else tk.Tk()
        super().__init__(self.master,height=400,width=400,
                bg='white',scrollregion=(-200,-200,200,200))
        self.pack()
        self.centerx = 0
        self.centery = 0
        self.center = (self.centerx,self.centery)
        self.title = 'codestudio'

    def __setattr__(self,name,value):
        super().__setattr__(name,value)
        if name == 'title': self.master.title(value)

    def save_eps(self,name):
        #TODO check for existing fname and if so just increment name by 1
        fname = name + '.eps'
        return self.postscript(file=fname)

    def draw_line(self,line,color='black',width=7):
        n = len(line)
        coords = (line[0],-line[1],line[2],-line[3])
        if n >= 5: color = line[4]
        if n >= 6: width = line[5]
        self.create_line(coords, fill=color,
            width=width,capstyle='round',arrow=None)

    def draw_lines(self,lines,*args,**kwargs):
        [self.draw_line(line,*args,**kwargs) for line in lines]

    def draw_image(self,obj):
        pass
