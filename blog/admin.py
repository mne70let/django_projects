from django.contrib import admin
from .models import Post

#import (include) the Post model defined in the previous chapter:
admin.site.register(Post)