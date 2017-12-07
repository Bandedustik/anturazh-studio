import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'anturazh_studio.settings')

import django
django.setup()

from landingPage.models import Client, ClientMessage
from faker import Faker

fakegen = Faker()

def add_client():
    fake_name = fakegen.first_name()
    fake_email = fakegen.email()

    client = Client.objects.get_or_create(name = fake_name, email = fake_email)[0]
    client.save()
    return client

def fill_with_fake_data(N = 5):
    for entry in range(N):
        fake_client = add_client()

        fake_message = fakegen.paragraphs(nb=3, ext_word_list=None)
        fake_date = fakegen.date()

        client_message = ClientMessage.objects.get_or_create(client = fake_client, message = fake_message, date = fake_date)[0]
        client_message.save()

if __name__ == '__main__':
    print("Заполняем данные...")
    fill_with_fake_data(50)
    print("Данные сгенерированы!")
