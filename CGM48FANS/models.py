from django.db import models

# class Member(models.Model):
#     # ชื่อเล่นหรือชื่อสั้น
#     name = models.CharField(max_length=100)
    
#     # ชื่อเต็ม
#     full_name = models.CharField(max_length=255)
    
#     # ตำแหน่งงาน
#     position = models.CharField(max_length=100)
    
#     # ทีมที่พนักงานสังกัด
#     team = models.CharField(max_length=100)
    
#     # วันเกิด
#     born = models.DateField()
    
#     # สถานที่เกิด
#     birthplace = models.CharField(max_length=255)
    
#     # หมู่เลือด (เลือกระหว่าง A, B, AB, O)
#     BLOOD_TYPE_CHOICES = [
#         ('A', 'A'),
#         ('B', 'B'),
#         ('AB', 'AB'),
#         ('O', 'O'),
#     ]
#     blood_type = models.CharField(max_length=2, choices=BLOOD_TYPE_CHOICES)
    
#     # อายุ
#     age = models.PositiveIntegerField()
    

#     gen = models.IntegerField()

    

#     def __str__(self):
#         return self.full_name


from django.db import models

class Member2(models.Model):
    # UniqueID will be the primary key
    unique_id = models.AutoField(primary_key=True)  # Assuming auto-increment
    team = models.CharField(max_length=100,null=True)
    age = models.IntegerField(null=True)
    nickname = models.CharField(max_length=100,null=True)
    full_name_thai = models.CharField(max_length=200,null=True)
    bd = models.DateField(null=True)  # Assuming 'bd' means birthday (date field)

    def __str__(self):
        return self.nickname


class SongInformation(models.Model):
    # UniqueID will be the primary key
    unique_id = models.AutoField(primary_key=True)
    name_song = models.CharField(max_length=200)
    center = models.ForeignKey(Member2, on_delete=models.CASCADE)  # ForeignKey to Member model
    sembatsu = models.ManyToManyField(Member2, related_name='sembatsu_songs')  # Many-to-many relationship

    def __str__(self):
        return self.name_song


class Album(models.Model):
    # UniqueID will be the primary key
    unique_id = models.AutoField(primary_key=True)
    name_album = models.CharField(max_length=200)
    copy = models.IntegerField()
    list_songs = models.ManyToManyField(SongInformation, related_name='albums')  # Many-to-many relationship


    def __str__(self):
        return self.name_album


class Single(models.Model):
    # UniqueID will be the primary key
    unique_id = models.AutoField(primary_key=True)
    name_single = models.CharField(max_length=200)
    copy = models.IntegerField()
    list_songs = models.ManyToManyField(SongInformation, related_name='singles')  # Many-to-many relationship

    def __str__(self):
        return self.name_single
    

