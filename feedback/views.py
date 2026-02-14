from django.shortcuts import render, get_object_or_404
from .models import Feedback
from django.core.paginator import Paginator


# Create your views here.
def feedback_list(request):
    all_feedback = Feedback.objects.all()
    paginator = Paginator(all_feedback, 10)
    
    page_number = request.GET.get('page', 1)
    page_number = int(page_number)
    
    if page_number < 1:
        page_number = 1
    
    elif page_number > paginator.num_pages:
        page_number = paginator.num_pages
        
    page = paginator.page(page_number)
    
    data = {
        'feedback_list': page.object_list,
        'page': page,
    }
    return render(request, 'feedback/feedback_list.html', data)

def feedback_detail(request,pk):
    feedback = get_object_or_404(Feedback, pk = pk)
    data = {'feedback_detail' : feedback}
    return render (request, "feedback/feedback_detail.html", data)