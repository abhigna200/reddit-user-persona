import praw
import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Setup OpenAI and Reddit API
openai.api_key = os.getenv("OPENAI_API_KEY")

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="RedditPersonaScript"
)

def fetch_reddit_content(username):
    redditor = reddit.redditor(username)
    posts = [f"Title: {p.title}\nText: {p.selftext}" for p in redditor.submissions.new(limit=20)]
    comments = [c.body for c in redditor.comments.new(limit=50)]
    return posts, comments

def generate_persona(username, posts, comments):
    joined_data = "\n\n".join(posts + comments)
    prompt = f"""
Given the Reddit activity below, generate a detailed user persona. Include: 
- Age estimate
- Location (if possible)
- Interests & hobbies
- Personality traits
- Writing style
- Beliefs or political leaning
For each trait, cite the post/comment used to infer it.

Reddit Data:
{joined_data[:12000]}  # Keep under GPT token limit
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def save_output(username, persona_text):
    filename = f"personas/{username}_persona.txt"
    os.makedirs("personas", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(persona_text)

def main():
    url = input("Enter Reddit profile URL: ").strip()
    username = url.rstrip('/').split('/')[-1]
    posts, comments = fetch_reddit_content(username)
    persona = generate_persona(username, posts, comments)
    save_output(username, persona)
    print(f"✅ Persona saved to: personas/{username}_persona.txt")

if __name__ == "__main__":
    main()
  import praw
import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Setup OpenAI and Reddit API
openai.api_key = os.getenv("OPENAI_API_KEY")

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="RedditPersonaScript"
)

def fetch_reddit_content(username):
    redditor = reddit.redditor(username)
    posts = [f"Title: {p.title}\nText: {p.selftext}" for p in redditor.submissions.new(limit=20)]
    comments = [c.body for c in redditor.comments.new(limit=50)]
    return posts, comments

def generate_persona(username, posts, comments):
    joined_data = "\n\n".join(posts + comments)
    prompt = f"""
Given the Reddit activity below, generate a detailed user persona. Include: 
- Age estimate
- Location (if possible)
- Interests & hobbies
- Personality traits
- Writing style
- Beliefs or political leaning
For each trait, cite the post/comment used to infer it.

Reddit Data:
{joined_data[:12000]}  # Keep under GPT token limit
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def save_output(username, persona_text):
    filename = f"personas/{username}_persona.txt"
    os.makedirs("personas", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(persona_text)

def main():
    url = input("Enter Reddit profile URL: ").strip()
    username = url.rstrip('/').split('/')[-1]
    posts, comments = fetch_reddit_content(username)
    persona = generate_persona(username, posts, comments)
    save_output(username, persona)
    print(f"✅ Persona saved to: personas/{username}_persona.txt")

if __name__ == "__main__":
    main()
  import praw
import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Setup OpenAI and Reddit API
openai.api_key = os.getenv("OPENAI_API_KEY")

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="RedditPersonaScript"
)

def fetch_reddit_content(username):
    redditor = reddit.redditor(username)
    posts = [f"Title: {p.title}\nText: {p.selftext}" for p in redditor.submissions.new(limit=20)]
    comments = [c.body for c in redditor.comments.new(limit=50)]
    return posts, comments

def generate_persona(username, posts, comments):
    joined_data = "\n\n".join(posts + comments)
    prompt = f"""
Given the Reddit activity below, generate a detailed user persona. Include: 
- Age estimate
- Location (if possible)
- Interests & hobbies
- Personality traits
- Writing style
- Beliefs or political leaning
For each trait, cite the post/comment used to infer it.

Reddit Data:
{joined_data[:12000]}  # Keep under GPT token limit
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def save_output(username, persona_text):
    filename = f"personas/{username}_persona.txt"
    os.makedirs("personas", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(persona_text)

def main():
    url = input("Enter Reddit profile URL: ").strip()
    username = url.rstrip('/').split('/')[-1]
    posts, comments = fetch_reddit_content(username)
    persona = generate_persona(username, posts, comments)
    save_output(username, persona)
    print(f"✅ Persona saved to: personas/{username}_persona.txt")

if __name__ == "__main__":
    main()
  
