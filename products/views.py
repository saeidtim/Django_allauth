from django.shortcuts import render, reverse, redirect, resolve_url
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from .forms import PorductFormComment
from cart.forms import AddToCartProductForm


class ProductListView(generic.ListView):
    # model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(active=True)


class ProductDetailView(generic.DetailView, generic.FormView):
    model = Product
    template_name = 'products/product_detail.html'
    form_class = PorductFormComment

    def re
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data()
        context['CommentForm'] = PorductFormComment
        context['AddForm'] = AddToCartProductForm
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.product = self.get_object()
        obj.save()
        return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse_lazy('detail_view', kwargs={'pk': self.object.pk})
    def get_success_url(self):
        # return reverse_lazy('detail_view', self.kwargs.get('pk'))
        return reverse_lazy('detail_view', kwargs={'pk': self.kwargs.get('pk') })
