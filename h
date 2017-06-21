[1mdiff --git a/students/views.py b/students/views.py[m
[1mindex 91ea44a..e1a282a 100644[m
[1m--- a/students/views.py[m
[1m+++ b/students/views.py[m
[36m@@ -1,3 +1,30 @@[m
 from django.shortcuts import render[m
[32m+[m[32mfrom django.http import HttpResponse[m
 [m
[32m+[m[32m#Views for Students[m
[32m+[m[32mdef students_list(request):[m
[32m+[m	[32mreturn render(request, 'students/students_list.html', {})[m
[32m+[m
[32m+[m[32mdef students_add(request):[m
[32m+[m	[32mreturn HttpResponse('<h1>Student Add Form</h1>')[m
[32m+[m
[32m+[m[32mdef students_edit(request, sid):[m
[32m+[m	[32mreturn HttpResponse('<h1>Edit Student %s</h1>' % sid)[m
[32m+[m
[32m+[m[32mdef students_delete(request, sid):[m
[32m+[m	[32mreturn HttpResponse('<h1>Delete Student %s</h1>' % sid)[m
[32m+[m
[32m+[m
[32m+[m[32m#Views for Groups[m
[32m+[m[32mdef groups_list(request):[m
[32m+[m	[32mreturn HttpResponse('<h1>Groups Listing</h1>')[m
[32m+[m
[32m+[m[32mdef groups_add(request):[m
[32m+[m	[32mreturn HttpResponse('<h1>Group Add Form</h1>')[m
[32m+[m
[32m+[m[32mdef groups_edit(request, gid):[m
[32m+[m	[32mreturn HttpResponse('<h1>Edit Group %s</h1>' %gid)[m
[32m+[m
[32m+[m[32mdef groups_delete(request, gid):[m
[32m+[m	[32mreturn HttpResponse('<h1>Delete Group%s</h1>' %gid)[m[41m				[m
 # Create your views here.[m
[1mdiff --git a/studentsdb/urls.py b/studentsdb/urls.py[m
[1mindex 623dc5d..599dd60 100644[m
[1m--- a/studentsdb/urls.py[m
[1m+++ b/studentsdb/urls.py[m
[36m@@ -13,9 +13,23 @@[m [mIncluding another URLconf[m
     1. Import the include() function: from django.conf.urls import url, include[m
     2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))[m
 """[m
[31m-from django.conf.urls import url[m
[32m+[m[32mfrom django.conf.urls import url, include[m
 from django.contrib import admin[m
[32m+[m[32mfrom students import views[m
 [m
 urlpatterns = [[m
[31m-    url(r'^admin/', admin.site.urls),[m
[32m+[m[32m#Students URL's[m
[32m+[m		[32m# url(r'^index/$', students.views.students_list, name='home'),[m
[32m+[m		[32murl(r'^$', views.students_list, name='home'),[m
[32m+[m		[32murl(r'^students/add/$', views.students_add, name='students_add'),[m
[32m+[m		[32murl(r'^students/(?P<sid>\d+)/edit/$', views.students_edit, name='students_edit'),[m
[32m+[m		[32murl(r'^students/(?P<sid>\d+)/delete/$', views.students_delete, name='students_delete'),[m
[32m+[m
[32m+[m[32m#Groups URL's[m[41m	[m
[32m+[m		[32murl(r'^groups/$', views.groups_list, name='groups'),[m
[32m+[m		[32murl(r'^groups/add/$', views.groups_add, name='groups_add'),[m
[32m+[m		[32murl(r'^groups/(?P<gid>\d+)/edit/$', views.groups_edit, name='groups_edit'),[m
[32m+[m		[32murl(r'^groups/(?P<gid>\d+)/delete/$', views.groups_delete, name='groups_delete'),[m
[32m+[m
[32m+[m		[32murl(r'^admin/', include(admin.site.urls)),[m
 ][m
