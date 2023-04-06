from scrapper import Scrapp

async def analyze_urls(text: str):
    results = []
    for element in text:
        result = await Scrapp(element)
        if len(result) == 0:
            results.append(element + ", PASS")
        else:
            results.append(element + ", FAIL," + " ".join(result))
    
    return results