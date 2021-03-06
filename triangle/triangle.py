def is_triangle(sides):
    return sum(sides) > 2 * max(sides)

def equilateral(sides):
    return is_triangle(sides) and len(set(sides)) == 1
    
def isosceles(sides):
    return is_triangle(sides) and len(set(sides)) < 3

def scalene(sides):
    return is_triangle(sides) and len(set(sides)) == 3

