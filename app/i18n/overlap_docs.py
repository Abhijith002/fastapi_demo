tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

tag_items = [
    {
        "summary": "Cart Items"
    },
    {
        "get_response_description": "Getting cart Items",
        "post_response_description": "Adding new item",
        "q": "Item Id to filter"
    }
]
