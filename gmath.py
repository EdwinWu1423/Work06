import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    n = math.sqrt(vector[0]*vector[0]+vector[1]*vector[1]+vector[2]*vector[2])
    vector[0]=vector[0]/n
    vector[1]=vector[1]/n
    vector[2]=vector[2]/n
def cross_product(a,b):
  return [a[1]*b[2]-a[2]*b[1],
          a[2]*b[0]-a[0]*b[2],
          a[0]*b[1]-a[1]*b[0]]


#Return the dot porduct of a . b
def dot_product(a, b):
    return (a[0]*b[0] + a[1]*b[1] + a[2]*b[2])

#Calculate the surface normal for the triangle whose first
#point is located at i i in polygons
def calculate_normal(polygons, i):
    v1 = [polygons[i+1][0]-polygons[i][0],polygons[i+1][1]-polygons[i][1],polygons[i+1][2]-polygons[i][2]]
    v2 = [polygons[i+2][0]-polygons[i][0],polygons[i+2][1]-polygons[i][1],polygons[i+2][2]-polygons[i][2]]
    return cross_product(v1, v2)
