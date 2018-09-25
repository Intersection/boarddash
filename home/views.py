from django.shortcuts import render

def index(request):
    data = {
        'brooklyn_boards': range(1, 19),
        'bronx_boards': range(1, 13),
        'manhattan_boards': range(1, 13),
        'queens_boards': range(1, 15),
        'staten_island_boards': range(1, 4),
    }
    return render(request, 'index.html', data)
