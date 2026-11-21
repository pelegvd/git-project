from playwright.sync_api import Playwright

def test_get_post_from_api(playwright: Playwright):
    # יצירת קונטקסט לבקשות API (ללא פתיחת דפדפן)
    api_context = playwright.request.new_context(base_url="https://jsonplaceholder.typicode.com")
    
    # שליחת בקשת GET
    response = api_context.get("/posts/1")
    
    # אימות קוד סטטוס 200 ותוכן ה-JSON שחזר
    assert response.status == 200
    data = response.json()
    assert data["id"] == 1
    assert "title" in data
