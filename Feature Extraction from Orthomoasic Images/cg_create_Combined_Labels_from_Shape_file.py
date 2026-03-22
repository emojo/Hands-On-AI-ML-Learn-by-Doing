import geopandas as gpd
import pandas as pd

#shape_file_path = "D:\/ML_Hackathon\/villages_training_dataset\/shp-file\/"
#shape_file_path = "D:\/ML_Hackathon\/data\/PB_training_dataSet_shp_file\/shp-file\/"
shape_file_path  = "D:\/ML_Hackathon\/data\/CG_Training_dataSet\/shp-file\/"
# input shapefiles
bridge_file            = "Bridge.shp"
Built_Up_Area_type_file = "Built_Up_Area_type.shp"
railway_file           = "Railway.shp"
road_file              = "Road.shp"
road_centre_line_file  = "Road_Centre_Line.shp"
utlity_file            = "Utility.shp"
utlity_poly_file      = "Utility_Poly.shp"
water_body_file        = "Water_Body.shp"
water_body_line        = "Water_Body_line.shp"
waterbody_point_file   = "Waterbody_Point.shp"

bridge              = gpd.read_file(shape_file_path+bridge_file)
#bridge.to_crs("EPSG:3857")
#bridge              = gpd.GeoDataFrame(bridge, geometry=bridge.geometry, crs=bridge.to_crs("EPSG:3857"))

built_up_area_type  = gpd.read_file(shape_file_path+Built_Up_Area_type_file)
#built_up_area_type.to_crs("EPSG:3857")
#built_up_area_type.
#built_up_area_type  = gpd.GeoDataFrame(built_up_area_type, geometry=built_up_area_type.geometry, crs=built_up_area_type.to_crs("EPSG:3857"))

railway             = gpd.read_file(shape_file_path+railway_file) 
#railway.to_crs("EPSG:3857")         
#railway             = gpd.GeoDataFrame(railway, geometry=railway.geometry, crs=railway.to_crs("EPSG:3857"))

road                = gpd.read_file(shape_file_path+road_file) 
#road.to_crs("EPSG:3857") 
#road                = gpd.GeoDataFrame(road, geometry=road.geometry, crs=road.to_crs("EPSG:3857"))
#print("Road:CRS:",road.crs)           

#road_center_line    = gpd.read_file(shape_file_path+road_centre_line_file) 
#road_center_line.to_crs("EPSG:3857")
#road_center_line    = gpd.GeoDataFrame(road_center_line, geometry=road_center_line.geometry, crs=road_center_line.to_crs("EPSG:3857"))

#utility              = gpd.read_file(shape_file_path+utlity_file) 
#utility.to_crs("EPSG:3857")
#utility              = gpd.GeoDataFrame(utility, geometry=utility.geometry, crs=utility.to_crs("EPSG:3857"))   

utility_poly         = gpd.read_file(shape_file_path+utlity_poly_file)      
#utility_poly_.to_crs("EPSG:3857")
#utility_poly_        = gpd.GeoDataFrame(utility_poly_, geometry=utility_poly_.geometry, crs=utility_poly_.to_crs("EPSG:3857"))

water_body          = gpd.read_file(shape_file_path+water_body_file)  
#water_body.to_crs("EPSG:3857")     
#water_body        = gpd.GeoDataFrame(water_body, geometry=water_body.geometry, crs=water_body.to_crs("EPSG:3857"))
                    
#water_body_line     = gpd.read_file(shape_file_path+water_body_line)       
#water_body_line.to_crs("EPSG:3857")
#water_body_line     = gpd.GeoDataFrame(water_body_line, geometry=water_body_line.geometry, crs=water_body_line.to_crs("EPSG:3857"))

#waterbody_point     = gpd.read_file(shape_file_path+waterbody_point_file)
#waterbody_point.to_crs("EPSG:3857")
#waterbody_point     = gpd.GeoDataFrame(waterbody_point, geometry=waterbody_point.geometry, crs=waterbody_point.to_crs("EPSG:3857"))


bridge["class_id"]                  = 1
bridge["class_name"]                = "Bridge"      

built_up_area_type["class_id"]      = 2
built_up_area_type["class_name"]    = "Built_Up_Area_type"

railway["class_id"]                 = 3   
railway["class_name"]               = "Railway"
 
road["class_id"]                    = 4
road["class_name"]                  = "Road"   

#road_center_line ["class_id"]       = 5 
#road_center_line ["class_name"]     = "Road_Centre_Line" 

#utility["class_id"]                 = 6
#utility["class_name"]               = "Utility"

utility_poly["class_id"]             = 7
utility_poly["class_name"]           = "Utility_Poly" 

water_body["class_id"]              = 8
water_body["class_name"]            = "Water_Body"

#water_body_line["class_id"]         = 9
#water_body_line["class_name"]       = "Water_Body_line"

#waterbody_point["class_id"]         = 10
#waterbody_point["class_name"]       = "Waterbody_Point"




print("Bridge CRS:",bridge.crs,"CRS Name:", bridge.crs.name)
print("built_up_area_type CRS:",built_up_area_type.crs,"CRS Name:", built_up_area_type.crs.name)

print("railway CRS:",railway.crs,"CRS Name:",railway.crs.name)
print("Road:CRS:  ",road.crs, "CRS Name:",road.crs.name)  

#print("road_center_line CRS:",road_center_line.crs)
#print("utility CRS:",utility.crs)

print("utility_poly CRS:",utility_poly.crs,"CRS Name:",utility_poly.crs.name)
print("water_body CRS:",water_body.crs, "CRS Name:",water_body.crs.name)

#print("water_body_line CRS:",water_body_line.crs)
#print("waterbody_point CRS:",waterbody_point.crs)

built_up_area_type = built_up_area_type.to_crs("EPSG:3857")
print("built_up_area_type CRS:",built_up_area_type.crs,"CRS Name:", built_up_area_type.crs.name)

# combine all layers
labels = pd.concat(
                    [
                    bridge,
                    built_up_area_type,
                    railway,
                    road,
                    #road_center_line,
                    #utility,
                    utility_poly,
                    water_body,
                    #water_body_line,
                    #waterbody_point
                    ], 
                    ignore_index=True)

# convert back to GeoDataFrame
labels = gpd.GeoDataFrame(labels, geometry="geometry")

# ensure CRS is same
#labels = labels.set_crs(shape_file_path+Road.crs)
labels = labels.set_crs("EPSG:3857")


# save output
labels.to_file("labels.shp")

print("labels.shp created successfully")