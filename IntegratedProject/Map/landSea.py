from IntegratedProject.Map.GeoObject import Terrain

def classifyTerrain(terrain: Terrain):
    sea = 0
    hasSea = False
    for i in terrain.de:
        if i==0:
            sea += 1
    sea *= .0035
    if sea>=100.00:
        hasSea = True
    dim = terrain.shape
    for i in range(dim):
        for j in range(dim):
            if terrain.de[i][j] == 0:
                terrain.type = "sea"
            else:
                terrain.type = "coastal"

