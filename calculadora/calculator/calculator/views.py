from django.shortcuts import render

# This function renders the calculator form
def index(request):
    """ 
    Renders the calculator form.
    """
    context = {}
    return render(request, 'calculator/index.html', context)

def calculate(request):
    """ 
    Processes form submission and displays result.
    """
    if request.method == 'POST':
        # Get the operands and operator from the form submission
        first_operand = request.POST['first_operand']
        operator = request.POST['operator']
        second_operand = request.POST['second_operand']

        try:
            # Evaluate the expression and store the result
            result = eval(first_operand + operator + second_operand)
        except Exception as e:
            # If there's an error, store the error message
            result = "Error: " + str(e)
    else:
        # No result for GET requests
        result = ""

    # Store the result in the context dictionary
    context = {'result': result}
    return render(request, 'calculator/index.html', context)