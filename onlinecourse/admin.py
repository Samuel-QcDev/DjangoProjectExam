from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Choice, Question

# <HINT> Register QuestionInline and ChoiceInline classes here

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 4

class QuestionInLine(admin.StackedInline):
    model = Question
    
class ChoiceInLine(admin.StackedInline):
    model = Choice

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]
    list_display = ('id', 'question_text')

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_answer']

# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
