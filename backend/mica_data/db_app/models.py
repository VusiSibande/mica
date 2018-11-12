from django.db import models


class Unit(models.Model):
    unitID = models.IntegerField(primary_key=True)
    square_meters = models.FloatField(blank=True, null=True)
    title_deed = models.CharField(max_length=12, blank=True, null=True)
    registation_date = models.DateField(blank=True, null=True)
    purchase_price = models.FloatField(blank=True, null=True)


class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    cell_number = models.CharField(max_length=15)
    email = models.CharField(max_length=40, null=True, blank=True)
    id_number_one = models.CharField(max_length=14, blank=True, null=True)
    id_number_two = models.CharField(max_length=14, blank=True, null=True)
    unit = models.OneToOneField(Unit, on_delete=models.CASCADE)
    

class MonthlyWater(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    date = models.DateField()
    water_reading = models.IntegerField()


class FinancialYear(models.Model):
    start = models.DateField()
    end = models.DateField()

    class Meta:
        unique_together = ('start', 'end')


class LevyComponets(models.Model):
    fy = models.ForeignKey(FinancialYear, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    complex_water = models.FloatField()
    complex_power = models.FloatField()
    reserve_fund = models.FloatField()
    csos_levy = models.FloatField()
    regular_insurance = models.FloatField()
    fidelity_insurance = models.FloatField()
    admin_salary = models.FloatField()
    admin_stationary = models.FloatField()
    bank_charges = models.FloatField()
    audit = models.FloatField()
    landscaping = models.FloatField()
    water_reader = models.FloatField()
    firequip = models.FloatField()



