class edge:

    def __init__(self, source, destination, cost):
        self.source = source
        self.destination = destination
        self.cost = cost
    
    def __str__(self):
        return f"{self.source} --- {self.cost} ---> {self.destination}"
