# Code Listing #1

"""

Glossary models - Showing django admin view

"""

from django.db import models

class GlossaryTerm(models.Model):
    """ Model for describing a glossary word (term) """
    
    term = models.CharField(max_length=1024)
    meaning = models.CharField(max_length=1024)
    meaning_html = models.CharField('Meaning with HTML markup',
                    max_length=4096, null=True, blank=True)
    example = models.CharField(max_length=4096, null=True, blank=True)

    # can be a ManyToManyField?
    domains = models.CharField(max_length=128, null=True, blank=True)

    notes = models.CharField(max_length=2048, null=True, blank=True)
    url = models.CharField('URL', max_length=2048, null=True, blank=True)
    name = models.ForeignKey('GlossarySource', verbose_name='Source', blank=True)

    def __unicode__(self):
        return self.term

    class Meta:
        unique_together = ('term', 'meaning', 'url')

class GlossarySource(models.Model):
    """ Model for describing a glossary source """
    
    name = models.CharField(max_length=256, primary_key=True)
    url = models.CharField(max_length=2048, blank=True)
    description = models.CharField(max_length=512)

    # can be a ManyToManyField?
    tags  = models.CharField(max_length=1024, blank=True)

    mainlang = models.CharField(max_length=8, default='en_US')
    singlepage = models.BooleanField(default=True)
    translations = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


