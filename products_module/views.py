from django.views.generic import ListView, DetailView
from .models import Product, ProductCategory

class ProductListView(ListView):
    model = Product
    template_name = 'products_module/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.filter(is_active=True)
        return context

    def get_queryset(self):
        return Product.objects.filter(is_active=True)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products_module/product_detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'
