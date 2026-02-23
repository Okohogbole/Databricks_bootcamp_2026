BASE_PATH = "/Volumes/workspace/bronze/source_systems"

INGERSTION_CONFIG = [
    #crm
    {"source":"crm",
     "path":f"{BASE_PATH}/source_systems/cust_info.csv",
     "table":"crm_cust_info"},
    
    {"source":"crm",
     "path":f"{BASE_PATH}/source_systems/prd_info.csv",
     "table":"crm_prd_info"},


    {"source":"crm",
     "path":f"{BASE_PATH}/source_systems/sales_details.csv",
     "table":"crm_sales_info"},
    
    #erp
    {"source":"erp",
     "path":f"{BASE_PATH}/source_systems/CUST_AZ12.csv",
     "table":"erp_cust_az12"},

     {"source":"erp",
     "path":f"{BASE_PATH}/source_systems/LOC_A101.csv",
     "table":"erp_loc_a101"},
    
    {"source":"erp",
     "path":f"{BASE_PATH}/source_systems/PX_CAT_G1V2.csv",
     "table":"erp_px_cat_g1v2"}
    
]
