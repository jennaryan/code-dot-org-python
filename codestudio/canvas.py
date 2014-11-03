import tkinter as tk

class Canvas(tk.Canvas):
    N = 0
    S = 180
    E = 90
    W = 270
    delay = 1
    speed_scale = 1000
    speed_slowest = 0.5
    speed_slower = 5 
    speed_slow = 10 
    speed_normal = 40
    speed_fast = 50
    speed_faster = 80
    speed_fastest = 0 
    count = 0

    def __init__(self,startx=0,starty=0,master=None,speed='normal'):
        self.master = master if master else tk.Tk()
        self.master.geometry('400x400+0+0')
        self.speed = speed
        super().__init__(self.master,height=400,width=400,
                bg='white',scrollregion=(-200-startx, -200+starty,
                                          200-startx, 200+starty))
        self.pack()
        self.title = 'codestudio'
        self._delay = 0
        self.speed = speed 

    def exit_on_click(self):
        self.bind('<Button>',lambda e: e.widget.quit())
        self.mainloop()

    def __setattr__(self,name,value):
        if name == 'title':
            self.master.title(value)
        if name == 'speed':
            if isinstance(value,str):
                if   value == 'fastest': value = self.speed_fastest
                elif value == 'faster' : value = self.speed_faster
                elif value == 'fast'   : value = self.speed_fast
                elif value == 'normal' : value = self.speed_normal
                elif value == 'slow'   : value = self.speed_slow
                elif value == 'slower' : value = self.speed_slower
                elif value == 'slowest': value = self.speed_slowest
            if value == 0: 
                self._delay = 0
            else:
                self._delay = round((1/value) * self.speed_scale)
        super().__setattr__(name,value)

    def save_eps(self,name):
        #TODO check for existing fname and if so just increment name by 1
        fname = name + '.eps'
        return self.postscript(file=fname)

    def draw_line(self,line,color=None,width=7):
        n = len(line)
        master_color = color
        if color: master_color = color
        coords = (line[0],-line[1],line[2],-line[3])
        if n >= 5: color = master_color if master_color else line[4]
        if n >= 6: width = line[5]
        self.create_line(coords, fill=color,
            width=width,capstyle='round',arrow=None)
        self.delay()
        self.update()

    def delay(self,amount=None):
        amount = amount if amount else self._delay
        if amount != 0: self.after(amount)

    def draw_lines(self,lines,*args,**kwargs):
        [self.draw_line(line,*args,**kwargs) for line in lines]

    def draw_image(self,obj):
        pass
