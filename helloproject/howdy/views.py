from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
  template_name = "index.html"
  # def get(self, request, **kwargs):
    # return render(request, 'index.html', context=None)

class AboutPageView(TemplateView):
  template_name = "about.html"

class StartPageView(TemplateView):
  template_name = "startpage.html"

# Add this view
class DataPageView(TemplateView):
  def get(self, request, **kwargs):
    # pass this context object into the template
    # so that we can access the data list in the template
    context = {
      'data': [
        {
          'name': 'Celeb 1',
          'worth': '3454234'
        },
        {
          'name': 'Celeb 2',
          'worth': '2300000'
        },
        {
            'name': 'Celeb 3',
            'worth': '1000007'
        },
        {
            'name': 'Celeb 4',
            'worth': '456789'
        },
        {
            'name': 'Celeb 5',
            'worth': '7890000'
        },
        {
            'name': 'Celeb 6',
            'worth': '12000456'
        },
        {
            'name': 'Celeb 7',
            'worth': '896000'
        },
        {
            'name': 'Celeb 8',
            'worth': '670000'
        }
      ]
    }

    return render(request, 'data.html', context)