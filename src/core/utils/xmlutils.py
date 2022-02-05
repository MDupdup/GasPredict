import logging
from typing import List
import xml.etree.ElementTree as ET
from datetime import datetime as dt

from src.core.utils.consoleutils import ConsoleUtils


class XmlUtils:
    
    @staticmethod
    def load_file(file_name:str) -> List[dict]:
        logging.info(f"Loading file {file_name}...")
        with open(file_name, "r", encoding="ISO-8859-1") as xmlfile:
            tree = ET.fromstring(xmlfile.read())
            xmlfile.close()
            
        entries = []
        
        i = 0
        for child in tree:
            ConsoleUtils.print_progressbar(i, len(tree), '0', len(tree) - i)
            i += 1
            
            prices = {}
            for item in child:
                if item.tag == "prix":
                    if "maj" not in item.attrib: continue
                    date_issued = dt.strptime(item.attrib["maj"].split('T')[0], "%Y-%m-%d").strftime("%Y%m%d")
                    if date_issued not in prices:
                        prices[date_issued] = []
                        
                    if len(list(filter(lambda it: it["id"] == item.attrib["id"], prices[date_issued]))) == 0:
                        prices[date_issued].append({
                            "id": int(item.attrib["id"]),
                            "name": item.attrib["nom"],
                            "value": float(item.attrib["valeur"]) / 1000
                        })
                        
            entries.append({
                "id": child.attrib["id"],
                "zipcode": child.attrib["cp"],
                "address": child[0].text,
                "city": child[1].text,
                "prices": prices
            })
        
        logging.info("File loaded successfully!")
        
        return entries
