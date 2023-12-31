# Generated by Django 4.2.5 on 2023-09-07 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False)),
                ('title', models.TextField(max_length=256)),
                ('content', models.TextField(max_length=256)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.usermodel')),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]
