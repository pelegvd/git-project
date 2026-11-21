from playwright.sync_api import Playwright

def test_get_post_from_api(playwright: Playwright):
    api_context = playwright.request.new_context(base_url="https://jsonplaceholder.typicode.com")
    response = api_context.get("/posts/1")
    
    assert response.status == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data
