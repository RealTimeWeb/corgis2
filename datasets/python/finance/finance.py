'''
Hello! Thank you for downloading a CORGIS library. However, you do not
need to open this file. Instead you should make your own Python file and
add the following line:

import finance

Then just place the files you downloaded alongside it.
'''

import os as _os
import pickle as _pickle

__all__ = ['get_record']

def _tifa_definitions():
    return {"type": "ModuleType",
        "fields": {
            'get': {
                "type": "FunctionType",
                "name": 'get',
                "returns": {
                    "type": "ListType", 
                    "empty": False, 
                    "subtype": {"type": "NumType"}
                }
            },
            'get_record': {
                "type": "FunctionType",
                "name": 'get_record',
                "returns": 
				{"type": "ListType", "subtype": 
					{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'State'}, {"type": "LiteralStr", "value": 'Year'}, {"type": "LiteralStr", "value": 'Totals'}, {"type": "LiteralStr", "value": 'Details'}], "values": [
						{"type": "StrType"}, 
						{"type": "NumType"}, 
						{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Capital outlay'}, {"type": "LiteralStr", "value": 'Charges'}, {"type": "LiteralStr", "value": 'Construction'}, {"type": "LiteralStr", "value": 'Employee retirement revenue'}, {"type": "LiteralStr", "value": 'Equipment and land'}, {"type": "LiteralStr", "value": 'Expenditure'}, {"type": "LiteralStr", "value": 'Federal intergovernmental'}, {"type": "LiteralStr", "value": 'General expenditure'}, {"type": "LiteralStr", "value": 'General revenue'}, {"type": "LiteralStr", "value": 'Insurance trust  revenue'}, {"type": "LiteralStr", "value": 'Intergovernmental'}, {"type": "LiteralStr", "value": 'License tax'}, {"type": "LiteralStr", "value": 'Local intergovernmental'}, {"type": "LiteralStr", "value": 'Miscellaneous'}, {"type": "LiteralStr", "value": 'Miscellaneous commercial activity'}, {"type": "LiteralStr", "value": 'Other insurance trust revenue'}, {"type": "LiteralStr", "value": 'Revenue'}, {"type": "LiteralStr", "value": 'Sales tax'}, {"type": "LiteralStr", "value": 'Selective sales tax'}, {"type": "LiteralStr", "value": 'State intergovernmental'}, {"type": "LiteralStr", "value": 'Tax'}, {"type": "LiteralStr", "value": 'Unemployment comp revenue'}, {"type": "LiteralStr", "value": 'Utility revenue'}, {"type": "LiteralStr", "value": "Worker's comp revenue"}], "values": [
							{"type": "NumType"}, 
							{"type": "NumType"}, 
							{"type": "NumType"}, 
							{"type": "NumType"}, 
							{"type": "NumType"}, 
							{"type": "NumType"}, 
							{"type": "NumType"}, 
							{"type": "NumType"}, 
							{"type": "NumType"}, 
							{"type": "NumType"}, 
							{"type": "NumType"}, 
							{"type": "NumType"}, 
							{"type": "NumType"}, 
							{"type": "NumType"}, 
							{"type": "NumType"}, 
							{"type": "NumType"}, 
							{"type": "NumType"}, 
							{"type": "NumType"}, 
							{"type": "NumType"}, 
							{"type": "NumType"}, 
							{"type": "NumType"}, 
							{"type": "NumType"}, 
							{"type": "NumType"}, 
							{"type": "NumType"}]}, 
						{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Correction'}, {"type": "LiteralStr", "value": 'Education'}, {"type": "LiteralStr", "value": 'Employment'}, {"type": "LiteralStr", "value": 'Financial Aid'}, {"type": "LiteralStr", "value": 'Health'}, {"type": "LiteralStr", "value": 'Insurance Trust'}, {"type": "LiteralStr", "value": 'Intergovernmental'}, {"type": "LiteralStr", "value": 'Natural Resources'}, {"type": "LiteralStr", "value": 'Public Welfare'}, {"type": "LiteralStr", "value": 'Transportation'}, {"type": "LiteralStr", "value": 'Utilities'}, {"type": "LiteralStr", "value": 'Waste'}, {"type": "LiteralStr", "value": 'Welfare'}], "values": [
							{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Correction Institutions Total'}, {"type": "LiteralStr", "value": 'Correction Intergovernmental'}, {"type": "LiteralStr", "value": 'Correction NEC Intergovernmental'}, {"type": "LiteralStr", "value": 'Correction NEC Total'}, {"type": "LiteralStr", "value": 'Correction Total'}], "values": [
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}]}, 
							{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Edcation Assistance and Subsidies'}, {"type": "LiteralStr", "value": 'Education Construction'}, {"type": "LiteralStr", "value": 'Education Equipment'}, {"type": "LiteralStr", "value": 'Education Equipment and Land'}, {"type": "LiteralStr", "value": 'Education Intergovernmental'}, {"type": "LiteralStr", "value": 'Education Other Current Operation'}, {"type": "LiteralStr", "value": 'Education Total'}, {"type": "LiteralStr", "value": 'Education-NEC Expenditure Total'}, {"type": "LiteralStr", "value": 'Education-NEC Intergovernmental'}, {"type": "LiteralStr", "value": 'Elementary Secondary Intergovernmental'}, {"type": "LiteralStr", "value": 'Elementary Secondary Total Expenditure'}, {"type": "LiteralStr", "value": 'Higher Education-Auxilliary Total Expenditure'}, {"type": "LiteralStr", "value": 'Higher Education-NEC Intergovernmental'}, {"type": "LiteralStr", "value": 'Higher Education-NEC Total Expenditure'}], "values": [
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}]}, 
							{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Employee Retirement Total Cash and Securities'}, {"type": "LiteralStr", "value": 'Employee Retirement Total Expenditure'}, {"type": "LiteralStr", "value": 'Employment Security Administration Expenditure Total'}, {"type": "LiteralStr", "value": 'Employment Security Administration Intergovernmental'}, {"type": "LiteralStr", "value": 'Unemployment Comp Total Cash and Securities'}, {"type": "LiteralStr", "value": 'Unemployment Comp Total Expenditure'}], "values": [
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}]}, 
							{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Assistance and Subsidies'}, {"type": "LiteralStr", "value": 'Beginning Long Term Debt Total Outstanding'}, {"type": "LiteralStr", "value": 'Bond Fund Total'}, {"type": "LiteralStr", "value": 'Borrowing Total'}, {"type": "LiteralStr", "value": 'Cash Assistance Intergovernmental'}, {"type": "LiteralStr", "value": 'Cash Assistance Total Expenditure'}, {"type": "LiteralStr", "value": 'Cash and Deposits Total'}, {"type": "LiteralStr", "value": 'Cash and Securities Total'}, {"type": "LiteralStr", "value": 'Categorical Assistance Intergovernmental'}, {"type": "LiteralStr", "value": 'Categorical Assistance Total Expenditure'}, {"type": "LiteralStr", "value": 'Federal Agency Securities Total'}, {"type": "LiteralStr", "value": 'Securities Total'}, {"type": "LiteralStr", "value": 'Sinking Fund Total'}], "values": [
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}]}, 
							{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Health Intergovernmental'}, {"type": "LiteralStr", "value": 'Health Total Expenditure'}, {"type": "LiteralStr", "value": 'Hospitals'}], "values": [
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Hospital-Other Intergovernmental'}, {"type": "LiteralStr", "value": 'Hospital-Other Total Expenditure'}, {"type": "LiteralStr", "value": 'Hospitals Total Construction'}, {"type": "LiteralStr", "value": 'Hospitals Total Current'}, {"type": "LiteralStr", "value": 'Hospitals Total Equipment and land'}, {"type": "LiteralStr", "value": 'Hospitals Total Expenditure'}, {"type": "LiteralStr", "value": 'Hospitals Total Intergovernmental'}, {"type": "LiteralStr", "value": 'Own Hospitals Total Expenditure'}], "values": [
									{"type": "NumType"}, 
									{"type": "NumType"}, 
									{"type": "NumType"}, 
									{"type": "NumType"}, 
									{"type": "NumType"}, 
									{"type": "NumType"}, 
									{"type": "NumType"}, 
									{"type": "NumType"}]}]}, 
							{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Insurance Trust'}, {"type": "LiteralStr", "value": 'Insurance Trust Cash and Deposits'}, {"type": "LiteralStr", "value": 'Insurance Trust Cash and Securities'}, {"type": "LiteralStr", "value": 'Insurance Trust Federal Agency Securities'}, {"type": "LiteralStr", "value": 'Insurance Trust Federal Securities'}, {"type": "LiteralStr", "value": 'Insurance Trust Other Securities'}, {"type": "LiteralStr", "value": 'Insurance Trust Securities Total'}, {"type": "LiteralStr", "value": 'Insurance Trust State and Local Securities Total'}, {"type": "LiteralStr", "value": 'Insurance Trust Total Expenditure'}], "values": [
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}]}, 
							{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Intergovernmental Expenditure'}, {"type": "LiteralStr", "value": 'Intergovernmental to Combined and Unallocable'}, {"type": "LiteralStr", "value": 'Intergovernmental to Counties'}, {"type": "LiteralStr", "value": 'Intergovernmental to Federal'}, {"type": "LiteralStr", "value": 'Intergovernmental to Local'}, {"type": "LiteralStr", "value": 'Intergovernmental to Municipalities'}, {"type": "LiteralStr", "value": 'Intergovernmental to School Districts'}, {"type": "LiteralStr", "value": 'Intergovernmental to Special Districts'}, {"type": "LiteralStr", "value": 'Intergovernmental to State'}, {"type": "LiteralStr", "value": 'Intergovernmental to Townships'}], "values": [
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}]}, 
							{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Natural Resources Construction'}, {"type": "LiteralStr", "value": 'Natural Resources Direct'}, {"type": "LiteralStr", "value": 'Natural Resources Equipment and Land'}, {"type": "LiteralStr", "value": 'Natural Resources Intergovernmental'}, {"type": "LiteralStr", "value": 'Natural Resources NEC Total Expenditure'}, {"type": "LiteralStr", "value": 'Natural Resources Total'}, {"type": "LiteralStr", "value": 'Agriculture'}, {"type": "LiteralStr", "value": 'Fish and Game'}, {"type": "LiteralStr", "value": 'Forestry'}, {"type": "LiteralStr", "value": 'Parks'}], "values": [
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Agriculture Intergovernmental'}, {"type": "LiteralStr", "value": 'Agriculture Total Expenditure'}, {"type": "LiteralStr", "value": 'Federal Agriculture Farm Income Intergovernmental'}, {"type": "LiteralStr", "value": 'Federal Agriculture Farm Income Total'}, {"type": "LiteralStr", "value": 'Federal Farm Credit Intergovernmental'}, {"type": "LiteralStr", "value": 'Federal Farm Credit Total'}], "values": [
									{"type": "NumType"}, 
									{"type": "NumType"}, 
									{"type": "NumType"}, 
									{"type": "NumType"}, 
									{"type": "NumType"}, 
									{"type": "NumType"}]}, 
								{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Fish and Game Intergovernmental'}, {"type": "LiteralStr", "value": 'Fish and Game Total Expenditure'}], "values": [
									{"type": "NumType"}, 
									{"type": "NumType"}]}, 
								{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Forestry Intergovernmental'}, {"type": "LiteralStr", "value": 'Forestry Total Expenditure'}], "values": [
									{"type": "NumType"}, 
									{"type": "NumType"}]}, 
								{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Parks Intergovernmental'}, {"type": "LiteralStr", "value": 'Parks Total Expenditure'}], "values": [
									{"type": "NumType"}, 
									{"type": "NumType"}]}]}, 
							{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Public Welfare Assistance and Subsidies'}, {"type": "LiteralStr", "value": 'Public Welfare Construction'}, {"type": "LiteralStr", "value": 'Public Welfare Direct Expenditure'}, {"type": "LiteralStr", "value": 'Public Welfare Equipment and Land'}, {"type": "LiteralStr", "value": 'Public Welfare Intergovernmental'}, {"type": "LiteralStr", "value": 'Public Welfare Other Current Operation'}, {"type": "LiteralStr", "value": 'Public Welfare Total Expenditure'}], "values": [
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}]}, 
							{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Transit Subsidy Intergovernmental'}, {"type": "LiteralStr", "value": 'Transit Subsidy Total Expenditure'}, {"type": "LiteralStr", "value": 'Airports'}, {"type": "LiteralStr", "value": 'Highways'}, {"type": "LiteralStr", "value": 'Parking'}, {"type": "LiteralStr", "value": 'Water Transport'}], "values": [
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Airports Intergovernmental'}, {"type": "LiteralStr", "value": 'Airports Total Expenditure'}], "values": [
									{"type": "NumType"}, 
									{"type": "NumType"}]}, 
								{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Highways Construction Total'}, {"type": "LiteralStr", "value": 'Highways Direct'}, {"type": "LiteralStr", "value": 'Highways Intergovernmental'}, {"type": "LiteralStr", "value": 'Highways Land and Equipment'}, {"type": "LiteralStr", "value": 'Highways Total Expenditure'}, {"type": "LiteralStr", "value": 'Regular Highways Intergovernmental'}, {"type": "LiteralStr", "value": 'Regular Highways Total Expenditure'}, {"type": "LiteralStr", "value": 'Toll Highways Total Expenditure'}], "values": [
									{"type": "NumType"}, 
									{"type": "NumType"}, 
									{"type": "NumType"}, 
									{"type": "NumType"}, 
									{"type": "NumType"}, 
									{"type": "NumType"}, 
									{"type": "NumType"}, 
									{"type": "NumType"}]}, 
								{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Parking Intergovernmental'}, {"type": "LiteralStr", "value": 'Parking Total'}], "values": [
									{"type": "NumType"}, 
									{"type": "NumType"}]}, 
								{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Water Transport Intergovernmental'}, {"type": "LiteralStr", "value": 'Water Transport Total Expenditure'}], "values": [
									{"type": "NumType"}, 
									{"type": "NumType"}]}]}, 
							{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Electric Utility Total Expenditure'}, {"type": "LiteralStr", "value": 'Gas Utility Total Expenditure'}, {"type": "LiteralStr", "value": 'Transit Utility Total Expenditure'}, {"type": "LiteralStr", "value": 'Utilities Construction'}, {"type": "LiteralStr", "value": 'Utilities Current Operation'}, {"type": "LiteralStr", "value": 'Utilities Equipment and Land'}, {"type": "LiteralStr", "value": 'Utilities Interest Total'}, {"type": "LiteralStr", "value": 'Utilities Total Expenditure'}, {"type": "LiteralStr", "value": 'Water Utility Total Expenditure'}], "values": [
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}]}, 
							{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Sewerage Intergovernmental'}, {"type": "LiteralStr", "value": 'Sewerage Total Expenditure'}, {"type": "LiteralStr", "value": 'Solid Waste Management Intergovernmental'}, {"type": "LiteralStr", "value": 'Solid Waste Management Total Expenditure'}], "values": [
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}]}, 
							{"type": "DictType", "literals": [{"type": "LiteralStr", "value": 'Welfare Institution Total Expenditure'}, {"type": "LiteralStr", "value": 'Welfare NEC Intergovernmental'}, {"type": "LiteralStr", "value": 'Welfare NEC Total Expenditure'}, {"type": "LiteralStr", "value": 'Welfare Vendor Payments Total'}], "values": [
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}, 
								{"type": "NumType"}]}]}]}}
            },
        }
    }

class _Constants(object):
    '''
    Global singleton object to hide some of the constants; some IDEs reveal
    internal module details very aggressively, and there's no other way
    to hide stuff.
    '''

class DatasetException(Exception):
    ''' Thrown when there is an error loading the dataset for some reason.'''
    
_Constants._DATABASE_NAME = _os.path.join(_os.path.dirname(__file__),
                                          "finance.data")
if not _os.access(_Constants._DATABASE_NAME, _os.F_OK):
    raise DatasetException(("Error! Could not find a \"{0}\" file. "
                           "Make sure that there is a \"{0}\" in the "
                           "same directory as \"{1}.py\"! Spelling is "
                           "very important here."
                           ).format(_Constants._DATABASE_NAME, __name__))
elif not _os.access(_Constants._DATABASE_NAME, _os.R_OK):
    raise DatasetException(("Error! Could not read the \"{0}\" file. "
                            "Make sure that it readable by changing its "
                            "permissions. You may need to get help from "
                            "your instructor."
                            ).format(_Constants._DATABASE_NAME, __name__))


_Constants._DATASET = None

def get_record():
    """
    Retrieves all of the record.
    """
    if _Constants._DATASET is None:
        with open(_Constants._DATABASE_NAME, 'rb') as _:
            _Constants._DATASET = _pickle.load(_)
    return _Constants._DATASET

if __name__ == '__main__':
    from pprint import pprint as _pprint
    from timeit import default_timer as _default_timer
    
    print(">>> get_record()")
    
    start_time = _default_timer()
    result = get_record()
    print("Time taken: {}".format(_default_timer() - start_time))
    _pprint(result[0])