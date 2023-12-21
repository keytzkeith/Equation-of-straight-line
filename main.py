def calculate_y_difference(y_intercept, x_intercept):
    return y_intercept - x_intercept

def calculate_x_difference(x_intercept, y_intercept):
    return x_intercept - y_intercept

def evaluate_line_equation():
    y_x = float(input('Enter the x-value of the y-intercept: \n=> '))
    y_y = float(input('Enter the y-value of the y-intercept: \n=> '))
    x_x = float(input("Enter the x-value of the x-intercept: \n=> "))
    x_y = float(input('Enter the y-value of the x-intercept: \n=> '))

    y_val = calculate_y_difference(y_y, x_y)
    x_val = calculate_x_difference(y_x, x_x)

    m = y_val / x_val
    C = y_y - (m * y_x)

    if m == 1.0 and C == 0.0:
        print('y = x')
    elif m == 0:
        print(f'y = {C:.2f}')
    else:
        print(f'y = {m:.2f}x + {C:.2f}')
        print(f'Gradient = {m:.2f}')

print('Here you can generate an equation of a straight line')
evaluate_line_equation()
  
