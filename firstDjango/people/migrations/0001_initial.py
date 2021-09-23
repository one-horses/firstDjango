# Generated by Django 3.2.6 on 2021-09-18 10:14

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=128, verbose_name='出差编号')),
                ('wife', models.CharField(max_length=12, verbose_name='项目经理')),
                ('children', models.IntegerField(choices=[(1, '湖北省'), (2, '湖南省'), (3, '广东省'), (4, '安徽省'), (5, '四川省')], verbose_name='目的地')),
                ('parent', models.CharField(choices=[('军史馆', '军史馆'), ('博物馆', '博物馆'), ('展会', '展会')], max_length=12, verbose_name='项目类别')),
                ('c_date', models.DateField(default='', max_length=12, verbose_name='出差开始时间')),
                ('b_date', models.DateField(default='', max_length=12, verbose_name='出差结束时间')),
            ],
            options={
                'verbose_name': '出差管理',
                'verbose_name_plural': '出差管理',
                'db_table': 'table_family',
            },
            managers=[
                ('lq', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('age', models.CharField(max_length=128, verbose_name='项目编号')),
                ('name', models.CharField(max_length=128, verbose_name='项目名称')),
                ('xiangmjingl', models.CharField(max_length=128, verbose_name='项目经理')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_time', models.DateTimeField(auto_now=True, verbose_name='上次更新时间')),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '项目信息',
                'verbose_name_plural': '项目信息',
                'db_table': 'Person',
            },
        ),
        migrations.CreateModel(
            name='Wife',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_date', models.DateField(default='', max_length=12, verbose_name='项目开工时间')),
                ('b_date', models.DateField(default='', max_length=12, verbose_name='项目验收时间')),
                ('weight', models.FloatField(verbose_name='工期')),
                ('filename', models.FileField(null=True, upload_to='upload', verbose_name='项目文档')),
                ('name', models.OneToOneField(max_length=12, on_delete=django.db.models.deletion.CASCADE, to='people.person', verbose_name='项目名称')),
            ],
            options={
                'verbose_name': '项目文档',
                'verbose_name_plural': '项目文档',
                'db_table': 'Wife',
            },
        ),
        migrations.CreateModel(
            name='Husbands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField(choices=[(1, '采购经费'), (2, '活动经费'), (3, '差旅费'), (4, '邮寄费'), (5, '其他')], verbose_name='报销类别')),
                ('salary', models.FloatField(verbose_name='预支金额')),
                ('weight', models.FloatField(verbose_name='报销金额')),
                ('birthday', models.CharField(max_length=128, verbose_name='费用明细')),
                ('image1', models.ImageField(null=True, upload_to='baoxiaodan', verbose_name='报销单')),
                ('image2', models.ImageField(null=True, upload_to='baoxiaoxiangdan', verbose_name='报销详单')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_time', models.DateTimeField(auto_now=True, verbose_name='上次更新时间')),
                ('age', models.OneToOneField(max_length=12, on_delete=django.db.models.deletion.CASCADE, to='people.family', verbose_name='出差编号')),
                ('name', models.OneToOneField(max_length=12, on_delete=django.db.models.deletion.CASCADE, to='people.person', verbose_name='项目名称')),
            ],
            options={
                'verbose_name': '报销管理',
                'verbose_name_plural': '报销管理',
                'db_table': 'Husbands',
            },
        ),
        migrations.AddField(
            model_name='family',
            name='husband',
            field=models.OneToOneField(max_length=12, on_delete=django.db.models.deletion.CASCADE, to='people.person', verbose_name='项目名称'),
        ),
    ]