from django.db import models

class DriveTestData(models.Model):
    filename = models.CharField(max_length = 255, blank = False)
    file = models.FileField(upload_to='data/')
    uploaded_at = models.DateTimeField(auto_now_add = True)

    def get_absolute_url(self):
        return reverse('table-view',kwargs={'pk':self.pk})
