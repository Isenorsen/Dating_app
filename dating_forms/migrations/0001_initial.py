# Generated by Django 2.1.5 on 2019-02-06 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatingForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('image1', models.ImageField(blank=True, upload_to='media')),
                ('image2', models.ImageField(blank=True, upload_to='media')),
                ('image3', models.ImageField(blank=True, upload_to='media')),
                ('user', models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.UserAccounts')),
            ],
        ),
    ]