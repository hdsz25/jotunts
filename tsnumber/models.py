# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Jotunts(models.Model):
    index = models.BigIntegerField(primary_key=True)
    engname = models.TextField(db_column='EngName', blank=True, null=True)  # Field name made lowercase.
    chinname = models.TextField(db_column='ChinName', blank=True, null=True)  # Field name made lowercase.
    tel = models.TextField(db_column='Tel', blank=True, null=True)  # Field name made lowercase.
    shipyard = models.TextField(db_column='Shipyard', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'jotunts'
    def __str__(self):
        return self.chinname

class Meituan(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    des = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    sold = models.IntegerField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'meituan'


class Tsms(models.Model):
    index = models.BigIntegerField(primary_key=True)
    tip = models.TextField(db_column='Tip', blank=True, null=True)  # Field name made lowercase.
    classification_society = models.TextField(db_column='Classification_Society', blank=True, null=True)  # Field name made lowercase.
    imo = models.TextField(db_column='IMO', blank=True, null=True)  # Field name made lowercase.
    contract_no_field = models.TextField(db_column='Contract_No.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase.
    ship_s_name = models.TextField(db_column="Ship's_Name", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hull_no_field = models.TextField(db_column='Hull_No.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    project_no_field = models.TextField(db_column='Project_No.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    type_of_ship = models.TextField(db_column='Type_of_Ship', blank=True, null=True)  # Field name made lowercase.
    unit = models.TextField(db_column='Unit', blank=True, null=True)  # Field name made lowercase.
    dwt = models.BigIntegerField(db_column='DWT', blank=True, null=True)  # Field name made lowercase.
    ship_s_owner = models.TextField(db_column="Ship's_Owner", blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    owner_country = models.TextField(db_column='Owner_Country', blank=True, null=True)  # Field name made lowercase.
    builder = models.TextField(db_column='Builder', blank=True, null=True)  # Field name made lowercase.
    sales_in_charge = models.TextField(db_column='Sales_in_charge', blank=True, null=True)  # Field name made lowercase.
    start_to_paint = models.DateTimeField(db_column='Start_to_Paint', blank=True, null=True)  # Field name made lowercase.
    stage_number_of_blocks = models.BigIntegerField(db_column='Stage_Number_of_Blocks', blank=True, null=True)  # Field name made lowercase.
    painted_blocks = models.BigIntegerField(db_column='Painted_Blocks', blank=True, null=True)  # Field name made lowercase.
    date_of_keel_laying = models.TextField(db_column='Date_of_Keel_laying', blank=True, null=True)  # Field name made lowercase.
    date_of_launching = models.TextField(db_column='Date_of_Launching', blank=True, null=True)  # Field name made lowercase.
    outside_shell = models.FloatField(db_column='Outside_Shell', blank=True, null=True)  # Field name made lowercase.
    wbt = models.FloatField(db_column='WBT', blank=True, null=True)  # Field name made lowercase.
    ct_ch = models.FloatField(db_column='CT_CH', blank=True, null=True)  # Field name made lowercase.
    outfitting_stage = models.FloatField(db_column='Outfitting_Stage', blank=True, null=True)  # Field name made lowercase.
    date_of_sea_trial = models.TextField(db_column='Date_of_Sea_Trial', blank=True, null=True)  # Field name made lowercase.
    pre_docking = models.TextField(db_column='Pre-Docking', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delivery_date = models.DateTimeField(db_column='Delivery_Date', blank=True, null=True)  # Field name made lowercase.
    start_to_tank_coating = models.TextField(db_column='Start_to_Tank_coating', blank=True, null=True)  # Field name made lowercase.
    tank_coating_leader = models.TextField(db_column='Tank_coating_Leader', blank=True, null=True)  # Field name made lowercase.
    coating_advisor_assigned_as_project_leader = models.TextField(db_column='Coating_advisor_assigned_as_Project_Leader', blank=True, null=True)  # Field name made lowercase.
    paints_used_for_w_b_t = models.TextField(db_column='Paints_used_for_W.B.T', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    paints_used_for_f_w_t = models.TextField(db_column='Paints_used_for_F.W.T', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    paints_used_for_cargo_hold = models.TextField(db_column='Paints_used_for_Cargo_Hold', blank=True, null=True)  # Field name made lowercase.
    af_vertical_side = models.TextField(db_column='AF_Vertical_Side', blank=True, null=True)  # Field name made lowercase.
    af_flat_side = models.TextField(db_column='AF_Flat_Side', blank=True, null=True)  # Field name made lowercase.
    notification_of_ts_assignment = models.TextField(db_column='Notification_of_TS_Assignment', blank=True, null=True)  # Field name made lowercase.
    technical_spec_field = models.TextField(db_column='Technical_Spec.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    tech_agreement = models.TextField(db_column='Tech._Agreement', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sent_date = models.DateTimeField(db_column='Sent_Date', blank=True, null=True)  # Field name made lowercase.
    id_report = models.DateTimeField(db_column='ID_report', blank=True, null=True)  # Field name made lowercase.
    specification_report = models.DateTimeField(db_column='Specification_report', blank=True, null=True)  # Field name made lowercase.
    check_list = models.DateTimeField(blank=True, null=True)
    tank_coating_report = models.DateTimeField(db_column='Tank_Coating_Report', blank=True, null=True)  # Field name made lowercase.
    final_report = models.DateTimeField(db_column='Final_report', blank=True, null=True)  # Field name made lowercase.
    line_manager = models.TextField(db_column='Line_Manager', blank=True, null=True)  # Field name made lowercase.
    score = models.TextField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
    guarantee = models.TextField(db_column='Guarantee', blank=True, null=True)  # Field name made lowercase.
    jan = models.FloatField(db_column='Jan', blank=True, null=True)  # Field name made lowercase.
    feb = models.FloatField(db_column='Feb', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tsms'


class Zhaopin(models.Model):
    company = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    jobname = models.CharField(db_column='jobName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    salary = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zhaopin'
