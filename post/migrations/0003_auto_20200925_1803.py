# Generated by Django 3.1 on 2020-09-25 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200925_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='club_post',
            name='allin',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='club_post',
            name='cera',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='club_post',
            name='civil',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='club_post',
            name='cse',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='club_post',
            name='meta',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='club_post',
            name='mining',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='club_post',
            name='mnc',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='club_post',
            name='mst',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='club_post',
            name='trical',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='club_post',
            name='tronix',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_post',
            name='allin',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_post',
            name='cera',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_post',
            name='civil',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_post',
            name='cse',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_post',
            name='meta',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_post',
            name='mining',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_post',
            name='mnc',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_post',
            name='mst',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_post',
            name='trical',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_post',
            name='tronix',
            field=models.IntegerField(default=0),
        ),
    ]
