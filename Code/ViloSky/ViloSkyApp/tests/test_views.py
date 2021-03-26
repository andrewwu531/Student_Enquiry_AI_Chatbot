from django.test import TestCase

class test_create_para_view(TestCase):
    @classmethod
    def setUp(self):
         newParaForm = NewParaForm({"static_text":"test adding paragraph"})
    def correct_response(self):
        response = self.client.get(reverse('paragraphs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'paragraphs.html')