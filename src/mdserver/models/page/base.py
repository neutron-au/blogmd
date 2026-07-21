

class BasePage:
    def __init__(self, path:str):
        self.path = path

    def render():
        """
        Full render pipeline, returns string containing page HTML content. 
        """
        raise NotImplementedError('The render method must be implemented by subclass.')
        