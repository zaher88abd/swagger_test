from sklearn.ensemble import RandomForestClassifier


class classifier:
    def __init__(self):
        self.model = None;
    
    def getModel(self):
        if self.model is None:
            self.load_model()

    def load_model(self):
        
        
