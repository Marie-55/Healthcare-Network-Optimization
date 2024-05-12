import math
class CSP: 
    def __init__(self, variables, Domains,constraints): 
        self.variables = variables 
        self.domains = Domains 
        self.constraints = constraints 
        self.solution = None

    def solve(self):
        self.solution = self.best_hospital()
        return self.solution
    
    def constraint_propagation(self):
        service,distance,capacity = self.constraints
        hospitals = set()
        for hospital in self.domains:
            services = hospital["service"] 
            if service in services:
                hospitals.add(hospital)
        
        for hospital in hospitals:
            if hospitals["capacity"] == 0:
                hospitals.remove(hospital)

        for hospital in hospitals:
            if hospitals["distance"] > distance:
                hospitals.remove(hospital)
        return hospitals
    
    def best_hospital(self):
        hospitals = self.constraint_propagation()
        best_hospital = None
        best_distance = float('inf')
        for h in hospitals:
            if h["distance"] < best_distance:
                best_distance = h["distance"]
                best_hospital = h 

        return best_hospital