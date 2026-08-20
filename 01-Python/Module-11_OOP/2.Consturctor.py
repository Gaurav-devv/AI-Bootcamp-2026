class Factory:
    def _init_(self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

reebok = Factory("Leather,3,2")
