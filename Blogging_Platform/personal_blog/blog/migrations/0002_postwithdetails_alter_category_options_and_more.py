# Generated by Django 5.0.6 on 2024-06-06 12:56

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostWithDetails',
            fields=[
                ('post_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField()),
                ('last_modified', models.DateTimeField()),
                ('category_names', models.TextField()),
                ('comment_details', models.TextField()),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z\\s]+$')]),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=60, validators=[django.core.validators.RegexValidator('^[a-zA-Z\\s]+$')]),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^[a-zA-Z\\s]+$')]),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['name'], name='blog_catego_name_cb8828_idx'),
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['author'], name='blog_commen_author_c4f747_idx'),
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['created_on'], name='blog_commen_created_871382_idx'),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['title'], name='blog_post_title_e1c6f7_idx'),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['created_on'], name='blog_post_created_7e46d3_idx'),
        ),
    ]
