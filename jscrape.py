import requests
import pandas as pd

# Authe and profile data grab
def get_user_profile(access_token, user_id):
    url = f"https://graph.facebook.com/v14.0/{user_id}"
    params = {
        'fields': 'id,username,account_type,media_count,biography',
        'access_token': access_token
    }
    response = requests.get(url, params=params)
    return response.json()

# followers data extracted
def get_user_followers(access_token, user_id):
    url = f"https://graph.facebook.com/v14.0/{user_id}/followers"
    params = {
        'access_token': access_token
    }
    response = requests.get(url, params=params)
    return response.json()

# Filter accounts based on whatever
def filter_accounts_by_criteria(accounts, criteria):
    filtered_accounts = []
    for account in accounts:
        if criteria(account):
            filtered_accounts.append(account)
    return filtered_accounts

# Define criteria for filters
def criteria(data):
    # Example : Check if the biography contains the word 'post-partum'
    return 'influencer' in data.get('biography', '').lower()

def save_accounts_to_csv(accounts, filename='similar_accounts.csv'):
    df = pd.DataFrame(accounts)
    df.to_csv(filename, index=False)
    print(f"Accounts saved to {filename}")

# 
def main():
    access_token = 'YOUR_ACCESS_TOKEN'
    initial_accounts = [{'id': '17841400008460056', 'username': 'account1'}, ...]  # Replace with actual accounts
    exclusion_list = ['account1', 'account2', 'account3']  # Replace with actual exclusion list

    filtered_initial_accounts = [acc for acc in initial_accounts if acc['username'] not in exclusion_list]
    
    similar_accounts = []
    for account in filtered_initial_accounts:
        followers = get_user_followers(access_token, account['id'])
        filtered_followers = filter_accounts_by_criteria(followers['data'], criteria)
        similar_accounts.extend(filtered_followers)

    save_accounts_to_csv(similar_accounts)

if __name__ == "__main__":
    main()
