from ratelimit import limits, sleep_and_retry
import pubchempy as pcp

class PubChem_Scraper:
    def __init__(self):
        pass
    
    def scrape_compound_info(self, attributes, compound_ID):
        
        # compounds is a list of all results for provided string(pubchem_ID)
        compounds = self.get_compounds_with_rate_limit(compound_ID) 
        
        scraped_dict = {}
        if compounds:
            # obtaining first entry of compound list - all compounds *should* be identical
            compound = compounds[0]
            scraped_dict = {}
            
            # parsing attribute list
            for attribute in attributes:
                if hasattr(compound, attribute): # compound for attribute method
                    scraped_dict[attribute] = getattr(compound, attribute) # calls attribute method
                    
                else: 
                    scraped_dict[attribute] = 'no attribute found'

        return scraped_dict
    
    # define rate limit of 10 calls per second
    @sleep_and_retry
    @limits(calls=1, period=1)
    def get_compounds_with_rate_limit(self, compound_ID):
        compounds = pcp.get_compounds(compound_ID, 'name')
        return compounds

import pandas as pd

def process_excel(user_search_key, attributes, input_file, output_file):
    df = pd.read_excel(input_file) # Read input Excel file
    
    # creating new columns for defined attributes
    for attribute in attributes:
        df[attribute] = ''
    
    scraper = PubChem_Scraper() # instatiate pubchem scraper
    
    for index, search_ID in enumerate(df[user_search_key]): # TODO - better define which column is being searched
        
        # scrape information with extenally encapsulated class
        scraped_dict = scraper.scrape_compound_info(attributes, search_ID)
        
        for attribute, value in scraped_dict.items():
            df.at[index, attribute] = value
            
        print(scraped_dict)
    

    df.to_excel(output_file, index=False)
            
        
# defined attributes per pubchemy API documentation
attributes = ['molecular_formula', 
              'monoisotopic_mass', 
              'isomeric_smiles', 
              'iupac_name', 
              'inchi', 
              'inchikey']

# column header which will be used as search key on PubChem
user_search_key = 'CAS No.'

# input and output file directories
input_file = f'C:\\Users\\john.petrini\\Desktop\\Working_Python_Folder\\real_book_1.xlsx'
output_file = f'C:\\Users\\john.petrini\\Desktop\\Working_Python_Folder\\real_book_1_sorted.xlsx'

# execute program
process_excel(user_search_key, attributes, input_file, output_file)
