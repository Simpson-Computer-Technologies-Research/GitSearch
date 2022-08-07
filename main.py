import queue, json, asyncio, aiohttp

class GitHubFinder:
    # // Initialize global variables
    def __init__(self):
        # // Get starting user (ex: realTristan)
        user = input(" >> Starting User: ") # -> MAKE SURE CAPS ARE CORRECT

        # // Global Class Variables
        self.profile_queue = queue.Queue() # -> Queue to track each profile url (Makes it thread safe)
        self.profile_queue.put(f"https://api.github.com/users/{user}") # -> Put the starting profile into the queue
        self.max_profiles = int(input(" >> Max Profiles: ")) # -> Get the max amount of profiles per following/followed (rec: 2-10)
        self.github_ratelimit = 60 # -> Github ratelimits ip past 60 requests
        self.result = {} # -> Result map
        self.profile_data_key_list = [
            "email",
            "bio",
            "twitter_username",
            "name",
            "location",
            "blog",
            "company"
        ] # -> Profile Url Data Keys to add to the result[user]["data"]
        
        # // Request Headers
        self.request_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
            "Accept": "application/vnd.github+json"
        }

    # // Remove any content past "{" if present in url
    def clean_url(self, url: str):
        if "{" in url:
            return url.split("{")[0]
        return url
    
    # // Write data to the "data.json" file
    def write_to_json(self, data: dict):
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)

    # // Get the followers / following of a profile
    async def get_follow_profiles(self, url: str, came_from: str):
        """
        This method gets the follower and followed's profile urls and adds them to the queue
            then for each profile url, a new key in the 'result' map is created
                with who the profile came_from and the came_from's past came_from profiles

        Args:
            url (str): the following/follower url
            came_from (str): the profile url of the 'url (str)'
        """
        url = self.clean_url(url)
        
        # // Send request and get resp json data
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=None)) as session:
            resp = await session.get(url, headers=self.request_headers)
            json = await resp.json()
        
        # // Iterate through the profiles
        for i, profile in enumerate(json):
            if i < self.max_profiles:
                if profile["url"] not in self.result:
                    self.profile_queue.put(profile["url"])
                    self.result[profile["url"]] = {"came_from": [came_from]}
                    [self.result[profile["url"]]["came_from"].append(p) for p in self.result[came_from]["came_from"]]
    
    # // Start the program
    async def start(self):
        """
        This method iterates through the profile queue to get the data
            and the profiles following/follower urls
        
        It will then run the "self.get_follow_profiles" function to get the profile urls of each
            follower / followed and add them to the profile_queue
        """
        while not self.profile_queue.empty() and len(self.result) < self.github_ratelimit:
            try:
                profile = self.profile_queue.get()
                
                # // Send request and get resp json data
                async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=None)) as session:
                    resp = await session.get(profile, headers=self.request_headers)
                    json = await resp.json()
                
                # // Add profile and it's data to result
                if not profile in self.result:
                    self.result[profile] = {"came_from": []}
                self.result[profile]["data"] = [json[key] for key in self.profile_data_key_list]
                
                # // Add Followers/Following to profile queue
                for key in ["followers_url", "following_url"]:
                    await self.get_follow_profiles(json[key], profile)
            except Exception as e:
                print(f" >> Error (95): {e}")
                break
        self.write_to_json(self.result)


# // Run the program
if __name__ == "__main__":
    github_finder = GitHubFinder()
    asyncio.run(github_finder.start())