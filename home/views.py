from django.shortcuts import render
from django.db.models import Count

from home.models import NYC311Record, CommunityBoard, BudgetRequest


def index(request):
    data = {
        'boards': [
            {
                'title': 'Brooklyn',
                'slug': 'brooklyn',
                'boards': range(1, 19),
            },
            {
                'title': 'Bronx',
                'slug': 'bronx',
                'boards': range(1, 13),
            },
            {
                'title': 'Manhattan',
                'slug': 'manhattan',
                'boards': range(1, 13),
            },
            {
                'title': 'Queens',
                'slug': 'queens',
                'boards': range(1, 15),
            },
            {
                'title': 'Staten Island',
                'slug': 'staten_island',
                'boards': range(1, 4),
            },
        ],
    }
    return render(request, 'index.html', data)

def board_detail(request, **kwargs):
    community_board = CommunityBoard.objects.get(slug=kwargs['board_slug'])
    category_dict = NYC311Record.objects.filter(community_board_relation=community_board).values('complaint_type').annotate(total=Count('complaint_type')).order_by('-total')
    capital_requests = BudgetRequest.objects.filter(community_board_relation=community_board, priority='CS')
    operational_requests = BudgetRequest.objects.filter(community_board_relation=community_board).exclude(priority='CS')
    data = {
            'community_board': community_board,
            'categories': list(category_dict)[:5],
            'budget_requests_capital': capital_requests[:5],
            'budget_requests_operational': operational_requests[:5],
    }
    return render(request, 'board_detail.html', data)
