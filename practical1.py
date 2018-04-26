# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# practical1.py
# Created on: 2018-01-23 16:04:05.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: practical1 <Input_Features> <Distance__value_or_field_> <Layer> <Intersect__3_> <Output_Feature_Class> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments
Input_Features = arcpy.GetParameterAsText(0)

Distance__value_or_field_ = arcpy.GetParameterAsText(1)

Layer = arcpy.GetParameterAsText(2)

Intersect__3_ = arcpy.GetParameterAsText(3)
if Intersect__3_ == '#' or not Intersect__3_:
    Intersect__3_ = "\\\\ds.leeds.ac.uk\\student\\student13\\gy17cev\\ArcGIS\\Default.gdb\\Intersect" # provide a default value if unspecified

Output_Feature_Class = arcpy.GetParameterAsText(4)

# Local variables:

# Process: Buffer
arcpy.Buffer_analysis(Input_Features, Output_Feature_Class, Distance__value_or_field_, "FULL", "ROUND", "NONE", "", "PLANAR")

# Process: Intersect
arcpy.Intersect_analysis([Layer,Output_Feature_Class], Intersect__3_, "ALL", "", "INPUT")

