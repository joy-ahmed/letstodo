# Generated by Django 4.2.6 on 2023-10-12 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskList_app', '0005_alter_tasklist_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasklist',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='profileimg',
            name='profileImg',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]
