from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from feedback.models import Feedback
from django.db.models import Count, Sum
from projects.models import Project



User = get_user_model()



# Create your views here
@login_required
def dashboard(request):
    total_budget = Project.objects.aggregate(total_budget=Sum('budget'))['total_budget']
    total_budget = float(total_budget) if total_budget else 0.0
    data={
        'total_users': User.objects.count(),
        'total_feedback': Feedback.objects.count(),
        'total_projects': Project.objects.count(),
        'total_budget': total_budget,
    }
    
    return render(request, 'dashboard/home.html', data )