# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-10 18:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import ietf.snippets.models
import wagtail.core.fields
import wagtail.search.index


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0001_initial'),
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtaildocs', '0008_document_file_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallToAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_external', models.URLField(blank=True, verbose_name='External link')),
                ('title', models.CharField(help_text='Link title', max_length=255)),
                ('blurb', models.CharField(blank=True, help_text='An explanation of the call to action.', max_length=255)),
                ('button_text', models.CharField(help_text='Text that appears on the call to action link.', max_length=255)),
                ('link_document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtaildocs.Document')),
                ('link_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page')),
            ],
            options={
                'verbose_name_plural': 'Calls to action',
                'ordering': ['title'],
            },
            bases=(wagtail.search.index.Indexed, models.Model, ietf.snippets.models.RenderableSnippetMixin),
        ),
        migrations.CreateModel(
            name='Charter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=511, unique=True)),
                ('title', models.TextField(blank=True)),
                ('abstract', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Charter',
                'ordering': ['title'],
            },
            bases=(models.Model, wagtail.search.index.Indexed),
        ),
        migrations.CreateModel(
            name='GlossaryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The glossary term.', max_length=255)),
                ('body', wagtail.core.fields.RichTextField(help_text='Explanation of the glossary term.')),
                ('link', models.URLField(blank=True)),
            ],
            options={
                'verbose_name': 'Glossary item',
                'ordering': ['title'],
            },
            bases=(models.Model, wagtail.search.index.Indexed),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="This group's name.", max_length=255)),
                ('summary', models.CharField(blank=True, help_text='More information about this group.', max_length=511)),
                ('email', models.EmailField(blank=True, help_text="This group's email address.", max_length=254)),
                ('image', models.ForeignKey(blank=True, help_text='An image to represent this group.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='images.IETFImage')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model, wagtail.search.index.Indexed, ietf.snippets.models.RenderableSnippetMixin),
        ),
        migrations.CreateModel(
            name='MailingListSignup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The header text for this content.', max_length=255)),
                ('blurb', models.CharField(blank=True, help_text='An explanation and call to action for this content.', max_length=255)),
                ('button_text', models.CharField(help_text='Text that appears on the mailing list link.', max_length=255)),
                ('sign_up', models.CharField(blank=True, help_text='The URL or email address where the user should sign up. If the working group is set then this does not need to be set.', max_length=255)),
            ],
            options={
                'ordering': ['title'],
            },
            bases=(models.Model, wagtail.search.index.Indexed, ietf.snippets.models.RenderableSnippetMixin),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=511)),
                ('link', models.URLField()),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model, wagtail.search.index.Indexed),
        ),
        migrations.CreateModel(
            name='RFC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=511)),
                ('title', models.TextField(blank=True)),
                ('rfc', models.CharField(help_text="The RFC's number (without any letters)", max_length=511, unique=True)),
                ('abstract', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'RFC',
                'ordering': ['title'],
            },
            bases=(models.Model, wagtail.search.index.Indexed),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A role within the IETF.', max_length=255)),
            ],
            options={
                'verbose_name': 'Role Override',
                'ordering': ['name'],
            },
            bases=(models.Model, wagtail.search.index.Indexed),
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The name of the organisation.', max_length=255)),
                ('link', models.URLField(blank=True)),
                ('logo', models.ForeignKey(help_text="The organisation's logo.", on_delete=django.db.models.deletion.CASCADE, related_name='+', to='images.IETFImage')),
            ],
            options={
                'ordering': ['title'],
            },
            bases=(models.Model, wagtail.search.index.Indexed),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The name of this topic.', max_length=255)),
                ('slug', models.CharField(max_length=511, unique=True)),
            ],
            options={
                'ordering': ['title'],
            },
            bases=(models.Model, wagtail.search.index.Indexed),
        ),
        migrations.CreateModel(
            name='WorkingGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=511)),
                ('acronym', models.CharField(blank=True, max_length=511)),
                ('description', models.CharField(blank=True, max_length=4096)),
                ('list_email', models.EmailField(blank=True, max_length=254)),
                ('list_subscribe', models.EmailField(blank=True, max_length=254)),
            ],
            options={
                'verbose_name': 'Working Group',
                'ordering': ['name'],
            },
            bases=(models.Model, wagtail.search.index.Indexed),
        ),
        migrations.AddField(
            model_name='rfc',
            name='working_group',
            field=models.ForeignKey(blank=True, help_text='The working group that produced this RFC', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='snippets.WorkingGroup'),
        ),
        migrations.AddField(
            model_name='mailinglistsignup',
            name='working_group',
            field=models.ForeignKey(blank=True, help_text='The group whose mailing list sign up address should be used. If sign up is set then this does not need to be set.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='snippets.WorkingGroup'),
        ),
        migrations.AddField(
            model_name='group',
            name='role',
            field=models.ForeignKey(blank=True, help_text="This group's role within the IETF.", null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='snippets.Role'),
        ),
        migrations.AddField(
            model_name='charter',
            name='working_group',
            field=models.ForeignKey(blank=True, help_text="This charter's working group", null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='snippets.WorkingGroup'),
        ),
    ]
