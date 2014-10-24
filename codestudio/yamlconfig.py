import yaml
from os import path
here = path.abspath(path.dirname(__file__))
default_fname = path.join(here,'config.yaml')

class YamlConfig():
    '''
    Memory safe way of loading yaml, doing something with it, then freeing all
    the resources used to load the file. Basically you can't use this class
    without using `with` syntax ensuring users of the class don't mistakenly
    leave the data it loads around in memory.

    with YamlConfig('basename') as config:
        print(config)

    Looks for a file named 'config.yaml' in the same directory as this file
    by default.
    '''
    def __init__(self,fname=None):
        if not fname: fname = default_fname
        self.fname = fname

    def __enter__(self):
        class _YamlConfig():

            def __str__(self): return str(self.__dict__)

            def __init__(self,fname=None):
                self.load(fname)

            def load(self,fname=None):
                with open(fname) as f:
                    self.data = yaml.load(f)

            def cleanup(self):
                pass

        self.yamlconfig = _YamlConfig(self.fname)
        return self.yamlconfig

    def __exit__(self, t, v, trace):
        self.yamlconfig.cleanup()

if __name__ == '__main__':
    
    # TODO put into proper unittests

    '''
    with YamlConfig() as config:
        print(config)
    '''

    with YamlConfig('./challenges/s1level24.yaml') as config:
        print(config)
