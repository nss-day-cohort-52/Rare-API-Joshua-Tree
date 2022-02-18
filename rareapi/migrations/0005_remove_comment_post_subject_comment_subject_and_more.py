# Generated by Django 4.0.2 on 2022-02-18 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0004_comment_post_subject_alter_comment_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post_subject',
        ),
        migrations.AddField(
            model_name='comment',
            name='subject',
            field=models.CharField(default='subject', max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=1000),
        ),
    ]
