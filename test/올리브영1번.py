def solution(x, y, r, v):
    
    
    left = min([x[i] - r[i] for i in range(len(x))])
    right = max([x[i] + r[i] for i in range(len(x))])
    bottom = min([y[i] - r[i] for i in range(len(x))])
    top = max([y[i] + r[i] for i in range(len(x))])
    
    points = []
    for i in range(0, len(v) - 1, 2):
        points.append([left + v[i] % (right - left), bottom + v[i+1] % (top - bottom)])
    
    in_point = 0
    for point in points :
        is_in = False
        for i in range(len(x)):
            if (point[0] - x[i])**2 + (point[1] - y[i])**2 <= r[i]**2 :
                is_in = True
        
        if is_in : in_point+=1
            
    f = in_point / len(points)
     
    return f * (right - left) * (top - bottom)