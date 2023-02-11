"""Main code for API"""

from fastapi import FastAPI, HTTPException
import controller as ctrl

# Init FastAPI application
app = FastAPI()

# Connection to the mogoDB database
collection = ctrl.init_collection()

@app.get("/get", response_description="Get informations from articles category")
async def fetch_article_info(category: str):
    """
    Retrieve an article's information from the database based on its category.
    Args:
        category (str): Article's category to retrieve.
    Returns:
        list[dict]: A list of dictionaries 
    Raises:
        HTTPException: If there is 0 articles with the category 
    """

    category = category.lower()
    # Search a category in the database 
    cursor = collection.find({"category": category}, {"_id": False})

    # Iterate over the dictionnaries
    results = [{k: str(v) for k, v in article.items()} for article in cursor]

    # Cehck if there are articles with the category
    if len(results) > 0:
        return results
    else:
        raise HTTPException(
            status_code=404, detail=f"Category : {article} -> not found")
