from django.db import models
import datetime

class b2p_site(models.Model):
    site=models.CharField(max_length=255,null=False,blank=False,db_index=True)
    
    
    def __str__(self) :
        return self.site

class b2p_program(models.Model):
    program=models.CharField(max_length=300,null=False,blank=False,db_index=True)
    
    
    def __str__(self) :
        return self.program


class b2p_project_name(models.Model):

    project_1=models.CharField(max_length=255,null=False,blank=False)
    site=models.ForeignKey(b2p_site, on_delete=models.PROTECT,null=False,blank=False)
    true_program=models.ForeignKey(b2p_program, on_delete=models.PROTECT,null=True,blank=True)
    is_active=models.BooleanField(default=True)
    effective_date = models.DateField(default=datetime.date.today,null=False,blank=False)
    expiration_date = models.DateField(default='2699-12-31',null=False,blank=False)

    def __str__(self) :
        return ' - '.join([self.project_2,self.project_1,self.site.site])  



class b2p_reference(models.Model):

    BILLING_TYPE = [
        ("PPM","PPM"),
        ("Hourly","Hourly")
    ]

    FTE_CAPPING = [
        (1,"daily"),
        (2,"weekly"),
        (3,"monthly")
    ]
    
    project=models.ForeignKey(b2p_program, on_delete=models.PROTECT,null=False,blank=False)
    site=models.ForeignKey(b2p_site, on_delete=models.PROTECT,null=False,blank=False)
    billing_type=models.CharField(max_length=50,null=False,blank=False,choices=BILLING_TYPE)
    effective_date = models.DateField(default=datetime.date.today,null=False,blank=False)
    expiration_date = models.DateField(default='2699-12-31',null=False,blank=False)
    b2p_target = models.FloatField(null=True,blank=True)
    aht_cap= models.FloatField(null=True,blank=True)
    ob_cap= models.FloatField(null=True,blank=True)
    fte_cap= models.FloatField(null=True,blank=True)
    fte_capping= models.SmallIntegerField(null=True,blank=True,choices=FTE_CAPPING)
    shrink= models.FloatField(null=True,blank=True)
    sme_shrink= models.FloatField(null=True,blank=True)
    flex_sme_ratio= models.FloatField(null=True,blank=True)
    
    def __str__(self) :
        return ' - '.join([self.project.program,self.site.site,str(self.effectived_date)])

    
class b2p_flex_nesting_agents_program(models.Model):

    program=models.CharField(max_length=255,null=True,blank=True,db_index=True)
    lob=models.CharField(max_length=255,null=True,blank=True)
    site=models.CharField(max_length=255,null=True,blank=True)
    true_program=models.ForeignKey(b2p_program, on_delete=models.PROTECT,null=True,blank=True)
    true_site=models.ForeignKey(b2p_site, on_delete=models.PROTECT,null=True,blank=True)
    assignment=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self) :
        return ' - '.join([self.lob,self.site])

class b2p_flex_sme_ratio_program(models.Model):

    program=models.CharField(max_length=255,null=True,blank=True,db_index=True)
    lob=models.CharField(max_length=255,null=True,blank=True)
    site=models.CharField(max_length=255,null=True,blank=True)
    true_program=models.ForeignKey(b2p_program, on_delete=models.PROTECT,null=True,blank=True)
    true_site=models.ForeignKey(b2p_site, on_delete=models.PROTECT,null=True,blank=True)
    assignment=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self) :
        return ' - '.join([self.lob,self.site])

class b2p_rates_program(models.Model):

    program=models.CharField(max_length=255,null=True,blank=True,db_index=True)
    lob=models.CharField(max_length=255,null=True,blank=True)
    site=models.CharField(max_length=255,null=True,blank=True)
    true_program=models.ForeignKey(b2p_program, on_delete=models.PROTECT,null=True,blank=True)
    true_site=models.ForeignKey(b2p_site, on_delete=models.PROTECT,null=True,blank=True)
    assignment=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self) :
        return ' - '.join([self.lob,self.site])
