from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner
from .models import Question, Choice, Submission, Enrollment

# <HINT> Register QuestionInline and ChoiceInline classes here
class  QuestionInLine(admin.StackedInline):
    model = Question
    extra = 1

class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 4


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ['title', 'content']

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'date_enrolled', 'mode', 'rating']

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text']
    inlines = [ChoiceInLine]


# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Submission)
