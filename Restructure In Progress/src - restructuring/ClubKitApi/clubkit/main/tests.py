from django.test import TestCase
# Create your tests here.


class MainPageTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_our_packages_page_status_code(self):
        response = self.client.get('/our-packages/')
        self.assertEquals(response.status_code, 200)

    def test_about_us_page_status_code(self):
        response = self.client.get('/about-us/')
        self.assertEquals(response.status_code, 200)

    def test_contact_us_page_status_code(self):
        response = self.client.get('/contact-us/')
        self.assertEquals(response.status_code, 200)

    def test_register_page_status_code(self):
        response = self.client.get('/register/')
        self.assertEquals(response.status_code, 200)

    def test_logout_status_code(self):
            response = self.client.get('/login/')
            self.assertEquals(response.status_code, 200)

    def test_reset_password_status_code(self):
            response = self.client.get('/password_reset/')
            self.assertEquals(response.status_code, 200)

    def test_buy_packages_status_code(self):
            response = self.client.get('/buy-packages/')
            self.assertEquals(response.status_code, 200)






