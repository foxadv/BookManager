from django.db import models

class Book(models.Model):
    BOOK_STATUS = [
        ('dr','Draft'),
        ('se','Sent')
    ]
    name = models.CharField(max_length=200,verbose_name="Book Name",help_text="Your book's name")
    slug = models.SlugField(max_length=300,blank=True,verbose_name="Book Link",allow_unicode=True,unique=True,help_text="Your book's link(will auto generated)")
    cover = models.ImageField(upload_to="BookCovers",verbose_name="Book Cover",help_text="Your book's cover for showing")
    description = models.TextField(verbose_name="Book Details",help_text="Your book's details")
    book_status = models.CharField(max_length=2,blank=True,choices=BOOK_STATUS,verbose_name="Book Status",help_text="Your book's status") 
    publish_date = models.DateTimeField(blank=True,verbose_name="Book Publish Date",help_text="Your book's publish date")
    is_plus = models.BooleanField(default=False,verbose_name="Is plus",help_text="Is book for plus members?") 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)   

    def __str__(self):
        return f'{self.name} | {self.description[:20]}...'

    class Meta:
        verbose_name = "Offically Book"
        verbose_name_plural = "Offically Books"    