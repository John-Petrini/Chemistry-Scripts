"""This class function is intended to modularize pubchhem scraping. It accepts a compound ID 
as an input, which can be a common name, IUPAC name, CAS, or PubChem CID, and outputs a 
dictionary of all related compound information defined within an attribute list comprised of
pubchempy compound class methods

Example attributes and a test case are provided"""

import pubchempy as pcp

# defined attributes per pubchemy API documentation
attributes = ['molecular_formula', 
              'monoisotopic_mass', 
              'isomeric_smiles', 
              'iupac_name', 
              'inchi', 
              'inchikey']


class PubChem_Scraper:
    def __init__(self):
        pass
    
    def scrape_compound_info(self, pubchem_ID):
        
        # compounds is a list of all results for provided string(pubchem_ID)
        compounds = pcp.get_compounds(pubchem_ID, 'name') # idk why 'name here'
        print('compounds found')
        
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

# TEST CASE
scraper = PubChem_Scraper()
scraped_data = scraper.scrape_compound_info('1,2-dichloroethylene')
print(scraped_data)
