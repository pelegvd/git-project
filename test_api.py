from playwright.sync_api import Playwright

def test_get_post_from_api(playwright: Playwright):
    api_context = playwright.request.new_context(base_url="https://jsonplaceholder.typicode.com")
    response = api_context.get("/posts/1")
    
    # שינוי בכוונה ל-201 כדי לדמות באג / שינוי חוזה API
    assert response.status == 201
    data = response.json()
    assert data["id"] == 1
