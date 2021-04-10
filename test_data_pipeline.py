import glob
from src.data_pipeline import report_generation
from pandas import read_csv, _testing

def test_reprt_check():
    # get all json filename
    all_files = glob.glob(r'Test_Data\INPUT\transactions\*\*.json')

    # Read customers &  products files1
    customer_data = read_csv(r'Test_Data\INPUT\customers.csv')
    products_data = read_csv(r'Test_Data\INPUT\products.csv')

    #collect data generated by code
    golden_data=report_generation(all_files,customer_data,products_data)

    #read expected output data
    expected_data = read_csv( r'Test_Data\OUTPUT\OutPut_Report.csv',)
    _testing.assert_frame_equal (golden_data[['customer_id','loyalty_score','product_id','product_category','purchase_count']],expected_data[['customer_id','loyalty_score','product_id','product_category','purchase_count']])