# from django.views.generic import ListView, DetailView
# from .models import Book, Author

# class BookListView(ListView):
#     model = Book
#     template_name = 'book_list.html'
#     context_object_name = 'books'

# class AuthorDetailView(DetailView):
#     model = Author
#     template_name = 'author_detail.html'
#     context_object_name = 'author'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['books'] = self.object.book_set.all()
#         return context

# from django.shortcuts import render
# from django.views import View
# from .models import Book, Author

# class MyListView(View):
#     model = None
#     template_name = None
#     context_object_name = None
    
#     def get_queryset(self):
#         return self.model.objects.all()
    
#     def get_template_name(self):
#         if self.template_name:
#             return self.template_name
#         return f'{self.model.__name__.lower()}_list.html'
    
#     def get_context_object_name(self):
#         if self.context_object_name:
#             return self.context_object_name
#         return f'{self.model.__name__.lower()}s'
    
#     def get_context_data(self, queryset):
#         context = {}
#         context[self.get_context_object_name()] = queryset
#         return context
    
#     def get(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         context = self.get_context_data(queryset)
#         return render(request, self.get_template_name(), context)


# class MyDetailView(View):
#     model = None
#     template_name = None
#     context_object_name = None
#     pk_url_kwarg = 'pk'
    
#     def get_queryset(self):
#         return self.model.objects.all()
    
#     def get_object(self):
#         pk = self.kwargs.get(self.pk_url_kwarg)
#         return self.get_queryset().get(pk=pk)
    
#     def get_template_name(self):
#         if self.template_name:
#             return self.template_name
#         return f'{self.model.__name__.lower()}_detail.html'
    
#     def get_context_object_name(self):
#         if self.context_object_name:
#             return self.context_object_name
#         return self.model.__name__.lower()
    
#     def get_context_data(self, obj):
#         context = {}
#         context[self.get_context_object_name()] = obj
#         return context
    
#     def get(self, request, *args, **kwargs):
#         obj = self.get_object()
#         context = self.get_context_data(obj)
#         return render(request, self.get_template_name(), context)


# class BookListMyView(MyListView):
#     model = Book
#     template_name = 'book_list.html'
#     context_object_name = 'books'


# class AuthorDetailMyView(MyDetailView):
#     model = Author
#     template_name = 'author_detail.html'
#     context_object_name = 'author'
    
#     def get_context_data(self, obj):
#         context = super().get_context_data(obj)
#         context['books'] = obj.book_set.all()
#         return context

from django.shortcuts import render
from .forms import CalculatorForm

def calculator(request):
    result = None
    error = None
    
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            operation = form.cleaned_data['operation']
            
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    error = 'Ошибка: Деление на ноль!'
    else:
        form = CalculatorForm()
    
    return render(request, 'calculator.html', {
        'form': form,
        'result': result,
        'error': error,
    })