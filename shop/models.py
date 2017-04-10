from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=55, db_index=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    name = models.CharField(max_length=300, db_index=True)
    slug = models.SlugField(max_length=320, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    period = models.CharField(max_length=25)                                        # 旅行時間
    main_image = models.ImageField(upload_to='products/main')                   # 顯示產品主要圖片（只顯示1張）
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name='products')
    description = models.TextField()
    itinerary = models.TextField()                                                  # 旅行路線
    q_and_a = models.TextField(blank=True)                                          # 常見問題Q&A

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'), )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images')                     # 每一個產品可以有多張其他的圖片
    image = models.ImageField(upload_to='products/detail', blank=True)     # 可以用於顯示產品的詳細圖片
