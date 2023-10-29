# surface area of 2 cubes using nested functions

def add_cubes(a,b):
    def surface_area(x):
        return 6 * pow(x,2)
    return surface_area(a) + surface_area(b)

result = add_cubes(2,3)
print(f'the surface area after adding 2 cubes is {result}')