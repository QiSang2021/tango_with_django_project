import os
import re
import importlib
from rango.models import Page
from django.test import TestCase
from django.conf import settings
from django.urls import reverse
from populate_script import populate
from django.contrib.auth.models import User
from django.forms import fields as django_fields

HEADER = f"{os.linesep}{os.linesep}================{os.linesep}FAILURE =({os.linesep}================{os.linesep}"
FOOTER = f"{os.linesep}"


class BaseTemplateTests(TestCase):
    """
    check that the base template exists, and that each page in the templates/rango directory has a title block.
    """

    def test_base_title_block(self):
        """
        Checks if Rango's base template has the correct value for the base template.
        """
        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'rango', 'base.html')
        template_str = self.get_template(template_base_path)

        title_pattern = r'<title>(\s*|\n*)Wardrobe(\s*|\n*)-(\s*|\n*){% block title_block %}(\s*|\n*)(\s*|\n*){% (endblock|endblock title_block) %}(\s*|\n*)</title>'
        self.assertTrue(re.search(title_pattern, template_str),
                        f"{HEADER}When searching the contents of base.html, we couldn't find the expected title block.{FOOTER}")

    def test_view_template(self):
        """
        Check that view uses the correct template.
        """
        populate()

        urls = [reverse('rango:about'),
                reverse('rango:add_page', kwargs={'category_name_slug': 'dior'}),
                reverse('rango:index'), ]

        templates = ['rango/about.html',
                     'rango/add_page.html',
                     'rango/index.html', ]

        for url, template in zip(urls, templates):
            response = self.client.get(url)
            self.assertTemplateUsed(response, template)

    def get_template(self, path_to_template):
        """
        Help to return the string representation of a template file.
        """
        f = open(path_to_template, 'r')
        template_str = ""

        for line in f:
            template_str = f"{template_str}{line}"

        f.close()
        return template_str


class IndexTests(TestCase):
    """
    Test the URL mapping and index view and check the response from the server.
    """

    def setUp(self):
        self.project_urls_module = importlib.import_module('tango_with_django_project.urls')

    def test_mappings_correctness(self):
        """
        Have the two URL mappings been set up correctly?
        """
        index_mapping_exists = False

        for mapping in self.project_urls_module.urlpatterns:
            if hasattr(mapping, 'name'):
                if mapping.name == 'index':
                    index_mapping_exists = True

        self.assertTrue(index_mapping_exists,
                        f"{HEADER}The index URL mapping could not be found. Check your PROJECT'S urls.py module.{FOOTER}")
        self.assertEquals(reverse('rango:index'), '/rango/',
                          f"{HEADER}The index URL lookup failed. Check Rango's urls.py module. {FOOTER}")


class PageFormTests(TestCase):
    """
    Check whether the PageForm class has been implemented correctly.
    """

    def test_page_form_class(self):
        """
        Does the PageForm implementation exist, and does it contain the correct instance variables?
        """
        import rango.forms
        self.assertTrue('PageForm' in dir(rango.forms),
                        f"{HEADER}The class PageForm could not be found in Rango's forms.py module.{FOOTER}")

        from rango.forms import PageForm
        page_form = PageForm()

        self.assertEqual(type(page_form.__dict__['instance']), Page,
                         f"{HEADER}The PageForm does not link to the Page model.{FOOTER}")

        fields = page_form.fields

        expected_fields = {
            'clothname': django_fields.CharField,
            'description': django_fields.CharField,
            'url': django_fields.URLField,
            'views': django_fields.IntegerField,
            'price': django_fields.DecimalField,
        }

        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]

            self.assertTrue(expected_field_name in fields.keys(),
                            f"{HEADER}The field '{expected_field_name}' was not found in your PageForm implementation.{FOOTER}")
            self.assertEqual(expected_field, type(fields[expected_field_name]),
                             f"{HEADER}The field '{expected_field_name}' in PageForm was not of the expected type '{type(fields[expected_field_name])}'.{FOOTER}")


def create_user_object():
    """
    Helper function to create a User object.
    """
    user = User.objects.get_or_create(username='testuser',
                                      first_name='Test',
                                      last_name='User',
                                      email='test@test.com')[0]
    user.set_password('testabc123')
    user.save()

    return user


def get_template(path_to_template):
    """
    Helper function to return the string representation of a template file.
    """
    f = open(path_to_template, 'r')
    template_str = ""

    for line in f:
        template_str = f"{template_str}{line}"

    f.close()
    return template_str


class AddPageTests(TestCase):

    def test_add_page_url_mapping(self):
        """
        Test whether the URL mapping for adding clothes is resolvable.
        """
        try:
            resolved_url = reverse('rango:add_page', kwargs={'category_name_slug': 'python'})
        except:
            resolved_url = ''

        self.assertEqual(resolved_url, '/rango/category/python/add_page/',
                         f"{HEADER}The lookup of URL name 'rango:add_page' didn't return a URL matching '/rango/category/python/add_page/', when using category 'python'. {FOOTER}")

    def test_bad_add_page(self):
        """
        Test whether clothes can not be added when not logged in.
        """
        populate()
        response = self.client.get(reverse('rango:add_page', kwargs={'category_name_slug': 'python'}))

        self.assertEqual(response.status_code, 302,
                         f"{HEADER}When not logged in and attempting to add a page, we should be redirected.{FOOTER}")

    def test_good_add_page(self):
        """
        Test whether clothes can be added when logged in.
        """
        populate()
        user_object = create_user_object()
        self.client.login(username='testuser', password='testabc123')
        response = self.client.get(reverse('rango:add_page', kwargs={'category_name_slug': 'python'}))

        self.assertEqual(response.status_code, 302,
                         f"{HEADER}We weren't greeted with a HTTP status code when attempting to add a page when logged in.{FOOTER}")
