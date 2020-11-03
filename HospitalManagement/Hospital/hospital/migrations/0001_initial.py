# Generated by Django 3.1.1 on 2020-11-03 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=20)),
                ('Name', models.CharField(max_length=20)),
                ('Sex', models.CharField(max_length=10)),
                ('Contact_no', models.CharField(max_length=10)),
                ('Password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=10)),
                ('Email', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.IntegerField()),
                ('Quantity', models.CharField(default='', max_length=3)),
                ('Price', models.IntegerField()),
                ('Name', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NID', models.CharField(max_length=5)),
                ('Name', models.CharField(max_length=20)),
                ('Sex', models.CharField(max_length=10)),
                ('Contact_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PID', models.CharField(max_length=5)),
                ('Name', models.CharField(max_length=25)),
                ('Sex', models.CharField(max_length=10)),
                ('Address', models.CharField(max_length=20)),
                ('Contact_no', models.IntegerField()),
                ('Record_no', models.CharField(max_length=5)),
                ('Description', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Room_ID', models.CharField(max_length=3)),
                ('Room_type', models.CharField(max_length=1)),
                ('Room_period', models.CharField(default='', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Treatment', models.CharField(max_length=20)),
                ('Amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Visiting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Record_no', models.IntegerField()),
                ('Appointment', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=30)),
                ('PID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Receptionist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('R_ID', models.CharField(max_length=5)),
                ('NID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.nurse')),
                ('Record_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.record')),
            ],
        ),
        migrations.CreateModel(
            name='Permanent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Pdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Admit_date', models.CharField(default='', max_length=20)),
                ('Discharge_date', models.CharField(default='', max_length=20)),
                ('PID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Maintains',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('R_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.receptionist')),
                ('Record_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.record')),
            ],
        ),
        migrations.CreateModel(
            name='Governs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.nurse')),
                ('Room_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.rooms')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EID', models.CharField(max_length=5)),
                ('Email', models.CharField(max_length=20)),
                ('Salary', models.IntegerField()),
                ('NID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.nurse')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='Doc_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.nurse'),
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Treatment', models.CharField(max_length=20)),
                ('Amount', models.IntegerField()),
                ('Medicine', models.CharField(max_length=20)),
                ('PID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Attends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Doc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor')),
                ('PID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Assigned',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
                ('Room_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.rooms')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Description', models.CharField(max_length=30)),
                ('Doc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor')),
                ('PID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
            ],
        ),
    ]
