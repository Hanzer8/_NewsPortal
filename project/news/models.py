from django.contrib.auth.models import User
from django.db import models
GRADE = [(1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7),(8, 8),(9, 9),(10, 10),]
# Create your models here.
class Author(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   reting = models.SmallIntegerField(default=0)

   def update_rating(self):
      post_ratings = Post.objects.filter(author=self).aggregate(total=models.Sum('rating'))['total'] or 0

      comment_ratings = Comment.objects.filter(user=self.user).aggregate(total=models.Sum('rating'))['total'] or 0

      self.rating = post_ratings * 3 + comment_ratings
      self.save()

class Category(models.Model):
   name = models.CharField(unique=True)


class Post(models.Model):
   author = models.ForeignKey(Author, on_delete=models.CASCADE)
   choose= {
      'Новость': 'News',
      'Статья': 'Article'
   }
   choise = models.CharField(choices=choose)
   datetime = models.DateTimeField(auto_now_add=True)
   post = models.ManyToManyField(Category, through='PostCategory')
   title = models.CharField(max_length=32)
   text = models.TextField()
   reting = models.SmallIntegerField(choices=GRADE, default=0, editable=True)


class PostCategory(models.Model):
   post = models.ForeignKey(Post, on_delete=models.CASCADE)
   category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
   post = models.ForeignKey(Post, on_delete=models.CASCADE)
   user = models.ManyToManyField(User, through=Author)
   text = models.TextField(max_length=256)
   datetime = models.DateTimeField(auto_now_add=True)
   reting = models.SmallIntegerField(choices=GRADE, default=0, editable=True)

   def like(self):
      self.reting += 1
      self.save()

   def dislike(self):
      self.reting -= 1
      self.save()


   # def update_reting(self):
   #    postRat = self.Post.reting
   #    pRet = 0
   #    pRet += Post.reting
   #
   #    commentRet = self.Comment.re


   # def preview(self):
   #    return f'{self.text_com[0:123]} ...'


# choose= {
#    'Новость': 'News',
#    'Статья': 'Article'
# }
# choise = models.CharField(choices=choose)

# class Order(models.Model):
#    time_in = models.DateTimeField(auto_now_add=True)
#    time_out = models.DateTimeField(null=True)
#    cost = models.FloatField(default=0.0)
#    pickup = models.BooleanField(default=False)
#    complete = models.BooleanField(default=False)
#    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)