from django.shortcuts import render
from django.db.models import Count

from home.models import NYC311Record, CommunityBoard


def index(request):
    data = {
        'brooklyn_boards': range(1, 19),
        'bronx_boards': range(1, 13),
        'manhattan_boards': range(1, 13),
        'queens_boards': range(1, 15),
        'staten_island_boards': range(1, 4),
    }
    return render(request, 'index.html', data)

def board_detail(request, **kwargs):
    community_board = CommunityBoard.objects.get(slug=kwargs['board_slug'])
    category_dict = NYC311Record.objects.values('complaint_type').annotate(total=Count('complaint_type')).order_by('-total')
    data = {
            'community_board': community_board,
            'categories': list(category_dict)[:5],
    }
    return render(request, 'board_detail.html', data)
