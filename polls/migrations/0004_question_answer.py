# Generated by Django 4.0.2 on 2022-02-19 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_question_option_four_question_option_one_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]