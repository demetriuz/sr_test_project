from django.db import models


class DefinitionLevelType(models.Model):
    name = models.CharField(max_length=512, unique=True)
    is_internal = models.BooleanField(default=False)


class DefinitionLevel(models.Model):
    type = models.ForeignKey(DefinitionLevelType, on_delete=models.CASCADE)
    value = models.CharField(max_length=512)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('value', 'parent')


class Tag(models.Model):
    parent_level = models.ForeignKey(DefinitionLevel, on_delete=models.CASCADE)
    code = models.CharField(unique=True, max_length=255)
    description = models.TextField(blank=True, null=True)
