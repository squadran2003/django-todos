from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from todos.models import Todo
from django.utils import timezone

# Create your tests here.

# model tests
class TodoModeTest(TestCase):
    def setUp(self):
        self.client = Client()
        # create a user
        self.user = User.objects.create_user(
            username='test',
            password='innocent23',
        )
        self.todo = Todo.objects.create(
            user=self.user,
            name='my todo',
            description='my description'
        )
    
    def test_todo_created(self):
        # check a record was created
        self.assertLess(self.todo.created_at,timezone.now())
        # try to find that todo
        todo = Todo.objects.get(user=self.user,name='my todo')
        self.assertTrue(todo.name,'my todo')
    
    def test_todo_deleted(self):
        todo = Todo.objects.get(user=self.user, name='my todo')
        todo.delete()
        result= None
        try:
            todo = Todo.objects.get(user=self.user, name='my todo')
            result = todo
        except Todo.DoesNotExist:
            result = 'user was deleted'
        self.assertTrue(result,'user was deleted')

class TodoViewTests(TestCase):
        def setUp(self):
            self.client = Client()
            # create a user
            self.user = User.objects.create_user(
                username='test',
                password='innocent23',
            )
            self.todo = Todo.objects.create(
                user=self.user,
                name='my todo',
                description='my description'
            )
            # log the user in
            self.client.force_login(self.user)
        
        def test_todo_list_view(self):
            response = self.client.get(reverse('home'))
            self.assertEqual(response.status_code,200)
            # check that the created todo was in the returned list
            self.assertContains(response,'my todo')
        
        def test_todo_create_view(self):
            data={
                'user':self.user,
                'name':'my todo2',
                'description':'my todo2 descriotion'
            }
            response = self.client.post(reverse('todos:add'),data)
            self.assertRedirects(response,reverse('home'))
        
        def test_todo_detail_view(self):
            response = self.client.get(reverse('todos:detail',kwargs={
                'pk':self.todo.id
            }))
            self.assertTrue(response.status_code,200)
            self.assertContains(response,'my todo')
            self.assertTemplateUsed(response, 'todos/todo_detail.html')
        
        def test_todo_update_view(self):
            data={
                'user':self.user,
                'name':'new todo',
                'description':'new description'
            }
            response = self.client.post(reverse('todos:edit',kwargs={
                'pk':self.todo.id
            }),data)
            self.assertTrue(response.status_code,200)
            self.assertRedirects(response,reverse('home'))
            







