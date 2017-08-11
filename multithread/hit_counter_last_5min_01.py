class HitCounter:
    def __init__(self):
        self.times = [0] * 300
        self.hits = [0] * 300
        
    #Record hit
    def hit(self, timestamp):
        index = timestamp % 300
        if times[index] != timestamp:
            times[index] = timestamp
            hits[index] = 1
        else:
            hits[index] += 1
    
    
    #Return the number of hits in the past 5 minutes.
    def getHits(self, timestamp):
        total = 0
        for i in range(300):
            if timestamp - times[i] < 300:
                total += hits[i]
            
        return total
