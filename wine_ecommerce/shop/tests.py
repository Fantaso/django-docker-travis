from django.test import TestCase, Client

# Create your tests here.
class ClientTests(TestCase):
    def setUp(self):
        self.client = Client()


    def test_client_ok_response(self):
        # make the request
        response = self.client.get('/shop/')

        # assert that the web page loads correctly
        self.assertEqual(response.status_code, 200)

    def test_client_false_response(self):
        # make the request
        response = self.client.get('/shop/')

        # assert that the web page loads correctly
        self.assertNotEqual(response.status_code, 400)
