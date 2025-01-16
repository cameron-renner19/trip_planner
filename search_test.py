import tkinter as tk
from tkinter import Listbox, StringVar
import sqlite3
import time  # Import the time module


def update_results(*args):
    """
    Updates the search results dynamically as the user types.
    """
    query = search_var.get().strip()  # Get the current value in the search bar
    if query:
        start_time = time.perf_counter()  # Start timing

        # Fetch matching cities from the database
        cursor.execute("""
        SELECT city, country, population, lat, lng
        FROM cities
        WHERE city LIKE ?
        LIMIT 10
        """, (f"{query}%",))
        results = cursor.fetchall()

        end_time = time.perf_counter()  # End timing
        query_time = (end_time - start_time) * 1000  # Convert to milliseconds

        # Clear the current list and insert new results
        result_list.delete(0, tk.END)
        for city, country, population, lat, lng in results:
            result_list.insert(
                tk.END, f"{city} ({country}) - Population: {population}, Lat: {lat}, Lng: {lng}"
            )

        # Display query time in the title bar
        root.title(f"Interactive City Search - Query Time: {query_time:.2f} ms")
    else:
        # Clear the list if no input
        result_list.delete(0, tk.END)
        root.title("Interactive City Search")


# Connect to the SQLite database
conn = sqlite3.connect("city.db")
cursor = conn.cursor()

# Create the main window
root = tk.Tk()
root.title("Interactive City Search")
root.geometry("500x400")  # Increased size to fit more details

# Create a search bar
search_var = StringVar()
search_var.trace("w", update_results)  # Calls update_results whenever the input changes
search_entry = tk.Entry(root, textvariable=search_var, font=("Arial", 14))
search_entry.pack(pady=10, padx=10, fill=tk.X)

# Create a listbox to display results
result_list = Listbox(root, font=("Arial", 12), height=15)
result_list.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Start the GUI event loop
root.mainloop()

# Close the database connection
conn.close()
