import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    #header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}  error
    # Access the keys
    PROXYCURL_API_KEY = os.getenv("PROXYCURL_API_KEY")
    header_dic = {"Authorization": f'Bearer {PROXYCURL_API_KEY}'}

    print(header_dic)
    response = requests.get(api_endpoint, params={"url": linkedin_profile_url}, headers=header_dic)

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


