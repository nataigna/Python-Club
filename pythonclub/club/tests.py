from django.test import TestCase
from .models import Meeting,Resource, MeetingMinuted,Event
from django.urls import reverse
# Create your tests here.

class MeetingTest(TestCase):
    def test_stringOutput(self):
        meeting= Meeting (meetingtitle='Monthly meetup')
        self.assertEqual(str(meeting),meeting.meetingtitle)
    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table),'meeting')

class ResourceTest(TestCase):
    def test_stringOutput(self):
        resource=Resource(resourcename='Libraries')
        self.assertEqual(str(resource),resource.resourcename)
    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table),'resource')

class EventTest(TestCase):
    def test_stringOutput(self):
        event=Event(eventtitle='event')
        self.assertEqual(str(event),event.eventtitle)
    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table),'event')

#testing the view

class TestIndex(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code,200)
    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('index'))
        self.assertTemplateUsed(response,'club/index.html')


class TestMeetingView(TestCase):
    def test_view_uses_correct_template (self):
        response=self.client.get(reverse('meeting'))
        self.assertTemplateUsed(response,'club/meeting.html')
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse ('meeting'))
        self.assertEqual(response.status_code,200)
    def test_view_url_exists_at_desired_location(self):
        response=self.client.get('/club/meeting')
        self.assertEqual(response.status_code, 200)



