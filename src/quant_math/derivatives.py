def numerical_derivative(f,x,h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

def second_derivative(f,x,h=1e-5):
    return (f(x+h) - (2* (f(x))) + f(x-h))/(h**2)

def third_derivative(f, x, h=1e-5):
    return (f(x+(2*h)) - (2*(f(x+h))) + (2*(f(x-h))) - (f(x-2*h)))/(2*h**3)

def taylor_approx_2(f,x,x0):
    first_der = numerical_derivative(f,x0)
    second_der = second_derivative(f, x0)
    return f(x0) + (first_der * (x-x0)) + (0.5 * second_der * ((x-x0)**2))