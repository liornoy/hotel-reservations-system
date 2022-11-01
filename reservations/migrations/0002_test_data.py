from django.db import migrations, transaction
import datetime


class Migration(migrations.Migration):
    dependencies = [
        ('reservations', '0001_initial'),
    ]

    def generate_data(apps, schema_editor):
        from reservations.models import Guest, Room, Reservation, Review
        test_data_guests = [
            ('Test Guest1', 'Guest1@mail.com'),
            ('Test Guest2', 'Guest2@mail.com'),
        ]
        test_data_rooms = [
            (1, 1, 10, 'Room #1 on floor #1 cost 10 per night'),
            (2, 2, 20, 'Room #2 on floor #2 cost 20 per night'),
        ]
        with transaction.atomic():
            for name, email in test_data_guests:
                Guest(name=name, email=email).save()
            for number, floor, price_per_night, details in test_data_rooms:
                Room(number=number, floor=floor, price_per_night=price_per_night, details=details).save()

        test_data_reviews = [
            (10, 'Test Guest1', 'test content 1'),
            (9, 'Test Guest2', 'test content 2'),
        ]
        test_data_reservations = [
            ('Test Guest1', 1, datetime.datetime(2022, 11, 6)),
            ('Test Guest2', 1, datetime.datetime(2022, 11, 5)),
        ]
        with transaction.atomic():
            for rating, guest_name, content in test_data_reviews:
                guest = Guest.objects.get(name=guest_name)
                Review(rating=rating, guest=guest, content=content).save()

            for guest_name, room_number, date in test_data_reservations:
                guest = Guest.objects.get(name=guest_name)
                room = Room.objects.get(number=room_number)
                Reservation(guest=guest, room=room, date=date).save()

    operations = [
        migrations.RunPython(generate_data),
    ]
