from browser_use import Agent, Browser, ChatBrowserUse
import asyncio

async def example():
    browser = Browser(
        # use_cloud=True,  # Uncomment to use a stealth browser on Browser Use Cloud
    )

    llm = ChatBrowserUse()

    agent = Agent(
          task =f"""
          ## **AI Agent Task: Find Cinema Showtimes for "Die Unfassbaren 3 - Now You See Me" (Now You See Me)**  

        #### **Objective:**  
        Check the local cinema schedule for the movie **"Now You See Me" (original title: "Die Unfassbaren 3 - Now You See Me")**, and retrieve available showtimes for tomorrow.  

        ---

        ### **Step 1: Access the Cinema Website**  

        1. Open [Cinemax Berlin](https://www.cinemaxx.de/).  

        ---

        ### **Step 2: Find the Movie "Now You See Me" (Die Unfassbaren 3 - Now You See Me)**  

        1. Click on the "Today" dropdown in the menu and select "Tomorrow" from the options list. 
        1. In the list find the film titled **"Flow"** (original title: "Die Unfassbaren 3 - Now You See Me").  
        2. Open the movie's information page to access details such as its description, duration, and screening schedule.  

        ---

        ### **Step 3: Retrieve Showtimes for Tomorrow**  

        1. Locate the **schedule or showtimes section** on the movie's page.  
        2. Extract the **available screening times** along with relevant details such as:  
        - Cinema hall (if available).  
        - Any special formats (e.g., IMAX, 3D, VIP).  

        ---

        ### **Step 4: Return the Information**  

        1. Provide a **clear and structured summary** of the available showtimes.  
        2. If no showtimes are available for tomorrow, return a message stating that no screenings are scheduled.  
        3. Ensure accuracy by verifying that the extracted data corresponds to the correct date and movie title.  

        ---

        ### **Key Requirements:**  

        - Confirm that the retrieved showtimes are specifically for **tomorrow**.  
        - Provide the information in a **clean and readable format**.  
        - If any steps fail (e.g., the movie is not listed, or no showtimes exist), return an appropriate message.  
        """,
        llm=llm,
        browser=browser,
    )

    history = await agent.run()
    return history

if __name__ == "__main__":
    history = asyncio.run(example())