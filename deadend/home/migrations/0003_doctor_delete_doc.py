# Generated by Django 4.2.7 on 2023-12-15 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_doc_delete_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=255)),
                ('doc_spec', models.CharField(max_length=255)),
                ('doc_department', models.CharField(max_length=255)),
                ('doc_image', models.ImageField(upload_to='doctors')),
            ],
        ),
        migrations.DeleteModel(
            name='doc',
        ),
    ]
