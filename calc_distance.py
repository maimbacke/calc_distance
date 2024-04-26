def add(x,y)

    return x+y

def my_app(calc_distance, point1, point2);
res=[]
for i,j in zip(point1, point2):
    res.append(calc_distance(i, j))

    return res

    point1= [(1.0,1.0,1.0), (2.0,2.0,2.0), (3.0,3.0,3.0)]
    point2= [(4.0,4.0,4.0), (5.0,5.0,5.0), (6.0,6.0,6.0)]

    distance= my_app(calc_distance, point1, point2)
    print(distance)