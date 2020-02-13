	# Add your code here
    def __init__(self, elements):
        self.elements = elements
        
    def computeDifference(self):
        self.maximumDifference = max(self.elements) - min(self.elements)