import tkinter as tk

class Canvas(tk.Canvas):
    def __init__(self,master=None):
        self.master = master if master else tk.Tk()
        super().__init__(self.master,height=400,width=400,
                bg='white',scrollregion=(-200,-200,200,200))
        self.pack()
        self.centerx = 200
        self.centery = 200
        self.center = (self.centerx,self.centery)
        self.title = 'codestudio'

    def __setattr__(self,name,value):
        super().__setattr__(name,value)
        if name == 'title': self.master.title(value)

    def save(self,name):
        #TODO check for existing fname and if so just increment name by 1
        fname = name + '.eps'
        return self.postscript(file=fname)

if __name__ == '__main__':
    c = Canvas()
    c.title = 'Blah'
    c.create_line(0,0,400,400,fill='red',width=7,capstyle='round')
    tk.mainloop()
